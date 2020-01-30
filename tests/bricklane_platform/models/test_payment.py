import unittest
from datetime import datetime

from bricklane_platform.models.payment import PaymentByCard, PaymentByBank
from bricklane_platform.models.card import Card
from bricklane_platform.models.bank import Bank


class TestPaymentByCard(unittest.TestCase):

    def test_init(self):
        payment = PaymentByCard()

        self.assertIsNone(payment.customer_id)
        self.assertIsNone(payment.date)
        self.assertIsNone(payment.amount)
        self.assertIsNone(payment.fee)
        self.assertIsNone(payment.card_id)

    def test_init_with_data(self):

        data = {
            "amount": "2000",
            "card_id": "45",
            "card_status": "processed",
            "customer_id": "123",
            "date": "2019-02-01",
        }

        payment = PaymentByCard(data)

        self.assertEqual(payment.customer_id, 123)
        self.assertEqual(payment.date, datetime(2019, 2, 1))
        self.assertEqual(payment.amount, 1960)
        self.assertEqual(payment.fee, 40)

        card = payment.card

        self.assertIsInstance(card, Card)
        self.assertEqual(card.card_id, 45)
        self.assertEqual(card.status, "processed")

    def test_is_successful(self):
        card = Card()
        card.status = "processed"
        payment = PaymentByCard()
        payment.card = card

        self.assertTrue(payment.is_successful())

    def test_is_successful_declined(self):
        card = Card()
        card.status = "declined"
        payment = PaymentByCard()
        payment.card = card

        self.assertFalse(payment.is_successful())

    def test_is_successful_errored(self):
        card = Card()
        card.status = "errored"
        payment = PaymentByCard()
        payment.card = card

        self.assertFalse(payment.is_successful())

class TestPaymentByBank(unittest.TestCase):

    def test_init(self):
        payment = PaymentByBank()

        self.assertIsNone(payment.customer_id)
        self.assertIsNone(payment.date)
        self.assertIsNone(payment.amount)
        self.assertIsNone(payment.fee)
        self.assertIsNone(payment.bank_account_id)

    def test_init_with_data(self):

        data = {
            "amount": "150",
            "customer_id": "111",
            "date": "2019-06-30",
            "bank_account_id": "455"
        }

        payment = PaymentByBank(data)

        self.assertEqual(payment.customer_id, 111)
        self.assertEqual(payment.date, datetime(2019, 6, 30))
        self.assertEqual(payment.amount, 147)
        self.assertEqual(payment.fee, 3)

        bank = payment.bank

        self.assertIsInstance(bank, Bank)
        self.assertEqual(bank.bank_account_id, 455)
