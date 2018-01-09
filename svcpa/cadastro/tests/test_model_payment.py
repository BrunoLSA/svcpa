from django.core import mail
from django.core.exceptions import ValidationError
from django.test import TestCase

from svcpa.cadastro.models import Member, Payment


class PaymentModelTest(TestCase):
    def setUp(self):
        self.member = Member.objects.create(
            name='Bruno Santana',
            date_of_birth='1982-09-28',
            rg='520449',
            cpf='12345678901',
            city='Manaus',
            state='AM',
            member_since='2005-04-10',
            payment_due='2018-01-30'
        )
        self.mail = mail.outbox

    def test_payment_money(self):
        payment = Payment.objects.create(member=self.member, kind=Payment.MONEY,
                                        value='100.00', date='2017-12-02',
                                        receipt='001')
        self.assertTrue(Payment.objects.exists())

    def test_payment_transfer(self):
        payment = Payment.objects.create(member=self.member, kind=Payment.TRANSFER,
                                         value='100.00', date='2017-12-02',
                                         receipt='001')
        self.assertTrue(Payment.objects.exists())

    def test_payment_check(self):
        payment = Payment.objects.create(member=self.member, kind=Payment.CHECK,
                                         value='100.00', date='2017-12-02',
                                         receipt='001')
        self.assertTrue(Payment.objects.exists())

    def test_choices(self):
        """Payment kind should be limited to M, T or C"""
        payment = Payment(member=self.member, kind='A', value='100.00',
                          date='2017-12-02', receipt='001')
        self.assertRaises(ValidationError, payment.full_clean)

    def test_message_mail_sent(self):
        """Send e-mail message advising the payment, if message_mail=True (default)"""
        payment = Payment.objects.create(member=self.member, kind=Payment.MONEY,
                                         value='100.00', date='2017-12-02',
                                         receipt='001')
        self.assertEqual(1, len(mail.outbox))

    def test_message_mail_not_sent(self):
        """Don't send email message if message_mail=False"""
        payment = Payment.objects.create(member=self.member, kind=Payment.MONEY,
                                         value='100.00', date='2017-12-02',
                                         receipt='001', message_email=False)
        self.assertEqual(0, len(mail.outbox))