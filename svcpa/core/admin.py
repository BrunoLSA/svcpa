from django.contrib import admin
from svcpa.cadastro.models import Member


class MemberModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'city', 'state', 'created_at')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'phone', 'cpf', 'neighborhood', 'city', 'state')
    list_filter = ('city',)

admin.site.register(Member, MemberModelAdmin)
