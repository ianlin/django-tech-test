from django.contrib import admin

# Register your models here.

from .models import Borrower, Business, Loan

class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')

class BusinessAdmin(admin.ModelAdmin):
    list_display = ('owner_name', 'company_name', 'address',
                    'registered_number', 'business_sector')

class LoanAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'amount', 'days',
                    'reason')

admin.site.register(Borrower, BorrowerAdmin)
admin.site.register(Business, BusinessAdmin)
admin.site.register(Loan, LoanAdmin)
