from decimal import Decimal
from dateutil.parser import parse
from abc import abstractmethod, ABCMeta
from bricklane_platform.models.card import Card
from bricklane_platform.config import PAYMENT_FEE_RATE
from bricklane_platform.models.bank import Bank


class Payment(object):

    __metaclass__ = ABCMeta

    customer_id = None
    date = None
    amount = None
    fee = None
    # card_id = None

    # def __init__(self, data=None):

    #     if not data:
    #         return
    @abstractmethod
    def __init__(self, data)
        self.customer_id = int(data["customer_id"])
        self.date = parse(data["date"])

        total_amount = Decimal(data["amount"])
        self.fee = total_amount * PAYMENT_FEE_RATE
        self.amount = total_amount - self.fee

    @abstractmethod
    def is_successful(self):
        pass


Class PaymentByCard(payment)
    name = "card"
    card_id = None

    def __init__(self, data=None);
        if not data:
            return
        super(PaymentByCard, self).__init__(data)
        card = Card()
        card.card_id = int(data["card_id"])
        card.status = data["card_status"]
        self.card = card

    def is_successful(self):
        return self.card.status == "processed"


Class PaymentByBank(payment):
    name = "bank"
    bank_account_id = "None"

    def __init__(self, data=None);
        if not data:
            return
        super(PaymentByBank, self).__init__(data)
        bank = Bank()
        bank.bank_account_id = int(data["bank_account_id"])
        self.bank = bank

    def is_successful(self):
        return self.card.status == "processed"

