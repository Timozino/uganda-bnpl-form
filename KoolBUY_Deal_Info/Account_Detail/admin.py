from django.contrib import admin
from .models import AccountDetail

class AccountDetailAdmin(admin.ModelAdmin):
    # Define the fields to display in the admin list view
    list_display = (
        'client',             # Display the client's name
        'smart_phone',        # Whether the client has a smartphone
        'product',            # Product associated with the client
        'outstanding_loan',   # Whether the client has an outstanding loan
        'monthly_income',     # The client's monthly income
        'bank_name',          # The selected bank
        'bank_account_name',  # Bank account name
        'bvn',                # BVN number
        'other_bank_name',    # Display the other bank name if applicable
    )
    
    # Enable search functionality by the following fields
    search_fields = ('client__name', 'bvn', 'bank_account_name', 'bank_name')
    
    # Enable filtering by bank, smartphone ownership, and outstanding loan status
    list_filter = ('bank_name', 'smart_phone', 'outstanding_loan')

    # Define the form layout in the detail view (add/edit form)
    fieldsets = (
        (None, {
            'fields': ('client', 'smart_phone', 'product', 'outstanding_loan', 'monthly_income')
        }),
        ('Bank Information', {
            'fields': ('bank_name', 'bank_account_name', 'bvn', 'other_bank_name')
        }),
    )

admin.site.register(AccountDetail, AccountDetailAdmin)
