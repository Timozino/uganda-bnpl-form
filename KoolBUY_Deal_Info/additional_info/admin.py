from django.contrib import admin


from .models import OtherDetails

@admin.register(OtherDetails)
class OtherDetailsAdmin(admin.ModelAdmin):
    list_display = ('client', 'sales_agent', 'guarantor_fullname', 'reason_for_purchase')
    search_fields = ('client__first_name', 'guarantor_fullname', 'reason_for_purchase')
    list_filter = ('sales_agent',)
    ordering = ('-id',)

