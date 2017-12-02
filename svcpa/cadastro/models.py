from django.db import models

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
    created_at = models.DateTimeField('cadastrado em', auto_now_add=True, null=True)
    paid = models.DateField('vencimento da anualidade', default=None, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'sócio'
        verbose_name_plural = 'sócios'