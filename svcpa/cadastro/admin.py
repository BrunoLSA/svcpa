from datetime import date

from django.contrib import admin

from svcpa.cadastro.models import Member, Payment


class ValidAnunityFilter(admin.SimpleListFilter):
    '''filtra os cadastros por vencimento da unidade: válida ou vendcida.'''
    title = ('anuidade')
    parameter_name = 'anuidade'

    def lookups(self, request, model_admin):
        return (
            ('válida', ('Válida')),
            ('vencida', ('Vencida')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'válida':
            return queryset.filter(payment_due__gte=date.today())
        if self.value() == 'vencida':
            return queryset.filter(payment_due__lt=date.today())


class PaymentInLine(admin.TabularInline):
    model = Payment
    extra = 1


class MemberModelAdmin(admin.ModelAdmin):
    inlines = [PaymentInLine,]
    list_display = ('name', 'cpf', 'city', 'state', 'member_since', 'payment_due')
    search_fields = ('name', 'email', 'phone', 'cpf', 'neighborhood', 'city', 'state')
    list_filter = ('city', ValidAnunityFilter)
    fields = ('name',
              ('date_of_birth', 'rg', 'cpf'),
              ('email', 'phone'),
              ('address', 'neighborhood'),
              ('city', 'state', 'cep'),
              ('member_since', 'member_number', 'payment_due'))
    ordering = ('name',)


admin.site.register(Member, MemberModelAdmin)
