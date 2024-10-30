from django.contrib import admin
from .models import BillingModel, PaygoConfig, SalesAgent, OutrightConfig,LoanCalculation

@admin.register(PaygoConfig)
class PaygoConfigAdmin(admin.ModelAdmin):
    list_display = ('configuration', 'price')
    search_fields = ('configuration',)

@admin.register(SalesAgent)
class SalesAgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code_number', 'location')
    search_fields = ('name', 'code_number')

@admin.register(OutrightConfig)
class OutrightConfigAdmin(admin.ModelAdmin):
    list_display = ('configuration', 'price')
    search_fields = ('configuration',)

@admin.register(BillingModel)
class BillingModelAdmin(admin.ModelAdmin):
    list_display = ('billing_model', 'client')
    search_fields = ('billing_model',)
    list_filter = ('billing_model',)




@admin.register(LoanCalculation)
class LoanCalculationAdmin(admin.ModelAdmin):
    list_display = ('repayment_plan', 'down_payment_percentage', 'management_fee_percentage', 'recurrent_percentage')
