import csv

from bricklane_platform.models.payment import PaymentByCard, PaymentByBank


class PaymentProcessor(object):

    def get_method_of_payment(self, source):
        payment_methods = [PaymentByCard, PaymentByBank]
        for method in payment_methods:
            if method.name == source:
                return method
        raise Exception("Not payment method for {}".format(source))

    def get_payments(self, csv_path, source):
        payments = []
        with open(csv_path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                method_of_payment = self.get_method_of_payment(source)
                payments.append(method_of_payment(row))

        return payments

    def verify_payments(self, payments):
        successful_payments = []
        for payment in payments:
            if payment.is_successful():
                successful_payments.append(payment)

        return successful_payments
