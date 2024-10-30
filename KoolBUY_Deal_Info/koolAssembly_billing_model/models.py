from django.db import models
from Bio_Data.models import BioData

# Define choices for billing model
BILLING_MODEL_CHOICES = [
    ('Paygo', 'Paygo (Kool Kredit)'),
    ('Outright', 'Outright'),
]

# Define choices for repayment plan
REPAYMENT_PLAN_CHOICES = [
    ('2_months', '2 months instalment'),
    ('5_months', '5 months instalment'),
    ('11_months', '11 months instalment'),
    ('17_months', '17 months instalment'),
]

class PaygoConfig(models.Model):
    configuration = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.configuration} - UGX{self.price}'

class SalesAgent(models.Model):
    name = models.CharField(max_length=255)
    code_number = models.CharField(max_length=50)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} ({self.code_number})'

class OutrightConfig(models.Model):
    configuration = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.configuration} - UGX{self.price}'

class BillingModel(models.Model):
    
    client=models.ForeignKey(BioData, on_delete=models.CASCADE, null=True, blank=True)
    
    billing_model = models.CharField(
        max_length=20, 
        choices=BILLING_MODEL_CHOICES
    )

    # Fields for Paygo (Kool Kredit)
    paygo_config = models.ForeignKey(PaygoConfig, on_delete=models.SET_NULL, null=True, blank=True)
    paygo_freezer_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    repayment_plan = models.CharField(
        max_length=20,
        choices=REPAYMENT_PLAN_CHOICES,
        null=True,
        blank=True
    )
    down_payment = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    monthly_instalment = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # Fields for Outright
    sales_agent = models.ForeignKey(SalesAgent, on_delete=models.SET_NULL, null=True, blank=True)
    outright_config = models.ForeignKey(OutrightConfig, on_delete=models.SET_NULL, null=True, blank=True)
    outright_freezer_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Override save method to ensure correct fields are filled based on the billing model selected.
        """
        if self.billing_model == 'Paygo':
            # Clear fields for Outright when Paygo is selected
            self.sales_agent = None
            self.outright_config = None
            self.outright_freezer_price = None
        elif self.billing_model == 'Outright':
            # Clear fields for Paygo when Outright is selected
            self.paygo_config = None
            self.paygo_freezer_price = None
            self.repayment_plan = None
            self.down_payment = None
            self.monthly_instalment = None

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.billing_model}'

    

class LoanCalculation(models.Model):
    

    # Fields
    repayment_plan = models.CharField(
        max_length=20, 
        choices=REPAYMENT_PLAN_CHOICES,
        default='2_months'
    )
    down_payment_percentage = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        help_text="Down payment percentage (e.g. 20.00 for 20%)"
    )
    management_fee_percentage = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        help_text="Management fee percentage (e.g. 5.00 for 5%)"
    )
    recurrent_percentage = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        help_text="Recurrent percentage (e.g. 2.50 for 2.5%)"
    )

    def __str__(self):
        return f"{self.repayment_plan} - Down Payment: {self.down_payment_percentage}%"







# class LoanCalculation(models.Model):
#     repayment_plan = models.CharField(
#         max_length=20, 
#         choices=REPAYMENT_PLAN_CHOICES,
#         default='2_months'
#     )
#     down_payment_percentage = models.DecimalField(
#         max_digits=5, 
#         decimal_places=2,
#         help_text="Down payment percentage (e.g. 20.00 for 20%)"
#     )
#     management_fee_percentage = models.DecimalField(
#         max_digits=5, 
#         decimal_places=2,
#         help_text="Management fee percentage (e.g. 5.00 for 5%)"
#     )
#     recurrent_percentage = models.DecimalField(
#         max_digits=5, 
#         decimal_places=2,
#         help_text="Recurrent percentage (e.g. 2.50 for 2.5%)"
#     )

#     def calculate_loan_values(self, paygo_freezer_price):
#         # Mapping repayment plan to numerical value
#         repayment_plan_mapping = {
#             '2_months': 2,
#             '5_months': 5,
#             '11_months': 11,
#             '17_months': 17,
#         }
#         repayment_plan_value = repayment_plan_mapping.get(self.repayment_plan, 1)

#         # Down payment calculation
#         down_payment_value = (paygo_freezer_price * self.down_payment_percentage / 100) + \
#                              (paygo_freezer_price * self.management_fee_percentage / 100)

#         # Remaining price after down payment
#         remaining_price = paygo_freezer_price - (paygo_freezer_price * self.down_payment_percentage / 100)

#         # Recurrent cost calculation
#         recurrent_cost = remaining_price * (self.recurrent_percentage / 100) * repayment_plan_value

#         # Monthly installment calculation
#         monthly_instalment_value = (remaining_price + recurrent_cost) / repayment_plan_value

#         return down_payment_value, monthly_instalment_value
