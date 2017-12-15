from django.core import mail
from django.test import TestCase

from svcpa.cadastro.models import Member, Payment


class PaymentSendMail(TestCase):
    def setUp(self):
        self.member = Member(
            name='Bruno Santana',
            date_of_birth='1982-09-28',
            rg='520449',
            cpf='12345678901',
            email='santanasta@gmail.com',
            phone='92-994104333',
            address='Av André Araújo, 870, apto 603 RS',
            neighborhood='Aleixo',
            city='Manaus',
            state='AM',
            cep='69060-000',
            member_since='2005-04-10',
            payment_due='2018-01-30'
        )
        self.member.save()

        self.payment = Payment.objects.create(
            member = self.member,
            kind = 'M',
            date = '2017-12-10',
            value = 100.00
        )

    def test_send_payment_mail(self):
        """Must send an e-mail when saving a new payment for the member"""
        self.assertEqual(1, len(mail.outbox))

    def test_payment_mail_subject(self):
        email = mail.outbox[0]
        expect = 'Confirmação de pagamento'
        self.assertEqual(expect, email.subject)

    def test_payment_mail_from(self):
        email = mail.outbox[0]
        expect = 'svcpa@hotmail.com'
        self.assertEqual(expect, email.from_email)

    def test_payment_mai_to(self):
        email = mail.outbox[0]
        expect = ['svcpa@hotmail.com', 'santanasta@gmail.com']
        self.assertEqual(expect, email.to)

    def test_payment_mai_body(self):
        email = mail.outbox[0]

        self.assertIn('Bruno Santana', email.body)
        self.assertIn('12345678901', email.body)
        self.assertIn('2017-12-10', email.body)