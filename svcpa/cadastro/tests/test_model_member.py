from django.test import TestCase
from svcpa.cadastro.models import Member


class MemberModelTest(TestCase):
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
            member_number = 1234,
            payment_due='2018-01-30'
        )

        self.member.save()

    def test_create(self):
        self.assertTrue(Member.objects.exists())

    def test_str(self):
        """Must return the name of the object"""
        self.assertEqual('Bruno Santana', str(self.member))

    def test_email_blank(self):
        field = Member._meta.get_field('email')
        self.assertTrue(field.blank)

    def test_phone_blank(self):
        field = Member._meta.get_field('phone')
        self.assertTrue(field.blank)

    def test_address_blank(self):
        field = Member._meta.get_field('address')
        self.assertTrue(field.blank)

    def test_neighborhood_blank(self):
        field = Member._meta.get_field('neighborhood')
        self.assertTrue(field.blank)

    def test_cep_blank(self):
        field = Member._meta.get_field('cep')
        self.assertTrue(field.blank)