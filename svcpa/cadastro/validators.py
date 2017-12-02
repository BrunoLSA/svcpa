from django.core.exceptions import ValidationError


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números.', 'digits')
    if len(value) != 11:
        raise ValidationError('CPF deve conter 11 números.', 'length')

def validate_cep(value):
    if not value.isdigit():
        raise ValidationError('CEP deve conter apenas números.', 'digits')
    if len(value) != 8:
        raise ValidationError('CEP deve conter 8 números.', 'length')