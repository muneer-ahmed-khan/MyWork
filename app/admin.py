from django.contrib import admin
from .models import Account, AccountDetail
# Register your models here.


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass


@admin.register(AccountDetail)
class AccountDetailAdmin(admin.ModelAdmin):
    list_display = ['date','customer','description','qty','brand','pattern','size','origin','destination','unit_price','credit','debit','balance']
    readonly_fields = ['credit','balance']
