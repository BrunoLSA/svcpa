from django.contrib import admin
from svcpa.cadastro.models import Member


class MemberModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'city', 'state', 'since', 'paid')
    search_fields = ('name', 'email', 'phone', 'cpf', 'neighborhood', 'city', 'state')
    list_filter = ('city',)
    fields = ('name',
              ('date_of_birth', 'rg', 'cpf'),
              ('email', 'phone'),
              ('address', 'neighborhood'),
              ('city', 'state', 'cep'),
              'paid')

    def since(self, obj):
        return '{:02}/{:02}/{:4}'.format(obj.created_at.day,
                                         obj.created_at.month,
                                         obj.created_at.year)

    since.short_description = 'cadastrado em'

admin.site.register(Member, MemberModelAdmin)
