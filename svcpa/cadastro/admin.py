from django.contrib import admin

from svcpa.cadastro.models import Member, Payment


class PaymentInLine(admin.TabularInline):
    model = Payment
    extra = 1


class MemberModelAdmin(admin.ModelAdmin):
    inlines = [PaymentInLine,]
    list_display = ('name', 'cpf', 'city', 'state', 'member_since', 'payment_due')
    search_fields = ('name', 'email', 'phone', 'cpf', 'neighborhood', 'city', 'state')
    list_filter = ('city',)
    fields = ('name',
              ('date_of_birth', 'rg', 'cpf'),
              ('email', 'phone'),
              ('address', 'neighborhood'),
              ('city', 'state', 'cep'),
              ('member_since', 'payment_due'))
    ordering = ('name',)


admin.site.register(Member, MemberModelAdmin)
