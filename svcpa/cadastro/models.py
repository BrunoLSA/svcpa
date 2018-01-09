from django.core import mail
from django.db import models
from django.template.loader import render_to_string

from svcpa.cadastro.managers import KindQuerySet
from svcpa.cadastro.validators import validate_cpf, validate_cep


class Member(models.Model):
    name = models.CharField('nome', max_length=100)
    date_of_birth = models.DateField('data de nascimento')
    rg = models.CharField('RG', max_length=20)
    cpf = models.CharField('CPF', max_length=11, validators=[validate_cpf])
    email = models.EmailField('e-mail', blank=True)
    phone = models.CharField('telefone', max_length=20, blank=True)
    address = models.CharField('endereço', max_length=255, blank=True)
    neighborhood = models.CharField('bairro', max_length=20, blank=True)
    city = models.CharField('cidade', max_length=20)
    state = models.CharField('estado', max_length=2)
    cep = models.CharField('CEP', max_length=8, validators=[validate_cep], blank=True)
    member_since = models.DateField('data de admissão')
    member_number = models.IntegerField('sócio número')
    payment_due = models.DateField('vencimento da anuidade', default=None, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'sócio'
        verbose_name_plural = 'sócios'


class Payment(models.Model):
    MONEY = 'M'
    TRANSFER = 'T'
    CHECK = 'C'

    KINDS = (
        (MONEY, 'dinheiro'),
        (TRANSFER, 'transferência bancária'),
        (CHECK, 'cheque')
    )

    member = models.ForeignKey('Member', verbose_name='sócio')
    kind = models.CharField('tipo', max_length=1, choices=KINDS)
    date = models.DateField('data')
    value = models.DecimalField('valor', max_digits=10, decimal_places=2)
    receipt = models.IntegerField('recibo nº')
    message_email = models.BooleanField('enviar e-mail?', default=True)

    objects = KindQuerySet.as_manager()

    class Meta:
        verbose_name = 'pagamento'
        verbose_name_plural = 'pagamentos'

    def save(self, *args, **kwargs):
        super(Payment, self).save(*args, **kwargs)

        if self.message_email:
            first_name = self.member.name.split()[0]
            last_name = self.member.name.split()[-1]
            name = ' '.join([first_name, last_name])

            context = dict(name=name, full_name = self.member.name,
                           cpf=self.member.cpf, date=self.date,
                           value=self.value, receipt=self.receipt)

            body = render_to_string('payments/payment_mail_body.txt',
                                    context)

            mail.send_mail(
                'Confirmação de pagamento',
                body,
                'svcpa@hotmail.com',
                ['svcpa@hotmail.com', self.member.email]
            )
