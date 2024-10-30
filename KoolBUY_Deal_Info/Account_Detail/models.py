from django.db import models
from Bio_Data.models import BioData

# Bank choices including "Others"
BANK_CHOICES = [
    ("absa-bank-uganda", "Absa Bank Uganda"),
    ("bank-of-africa-uganda", "Bank of Africa Uganda"),
    ("bank-of-baroda-uganda", "Bank of Baroda Uganda"),
    ("cairo-bank-uganda", "Cairo Bank Uganda"),
    ("centenary-bank", "Centenary Bank"),
    ("dfcu-bank", "DFCU Bank"),
    ("diamond-trust-bank-uganda", "Diamond Trust Bank Uganda"),
    ("equity-bank-uganda", "Equity Bank Uganda"),
    ("exim-bank-uganda", "Exim Bank Uganda"),
    ("finance-trust-bank", "Finance Trust Bank"),
    ("housing-finance-bank", "Housing Finance Bank"),
    ("kcb-bank-uganda", "KCB Bank Uganda"),
    ("nc-bank-uganda", "NC Bank Uganda"),
    ("postbank-uganda", "PostBank Uganda"),
    ("stanbic-bank-uganda", "Stanbic Bank Uganda"),
    ("standard-chartered-bank-uganda", "Standard Chartered Bank Uganda"),
    ("top-finance-bank", "Top Finance Bank"),
    ("tropical-bank", "Tropical Bank"),
    ("uganda-development-bank", "Uganda Development Bank"),
    ("united-bank-for-africa-uganda", "United Bank for Africa Uganda"),
    ("abc-capital-bank", "ABC Capital Bank"),
    ("orient-bank", "Orient Bank"),
    ("ecobank-uganda", "Ecobank Uganda"),
    ("guaranty-trust-bank-uganda", "Guaranty Trust Bank Uganda"),
    ("others", "Others")  # Adding the "Others" option
]




# Yes/No choices for dropdown fields
YES_NO_CHOICES = [
    ('yes', 'Yes'),
    ('no', 'No'),
]

class AccountDetail(models.Model):
    # ForeignKey to BioData model (client details)
    client = models.ForeignKey(BioData, on_delete=models.CASCADE, related_name="account_details")

    # Dropdown for smartphone availability (Yes/No)
    smart_phone = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='no')

    # Product field to capture the product name
    product = models.CharField(max_length=255)

    # Dropdown for outstanding loan (Yes/No)
    outstanding_loan = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='no')

    # Monthly income of the client
    monthly_income = models.DecimalField(max_digits=12, decimal_places=2)

    # Bank name field with choices from BANK_CHOICES, limited to Nigerian banks and including "Others"
    bank_name = models.CharField(max_length=100, choices=BANK_CHOICES)

    # Bank account name field to store the account holder's name
    bank_account_name = models.CharField(max_length=255)

    # Bank Verification Number (BVN) - must be unique
    bvn = models.CharField(max_length=11, unique=True)

    # Optional field for "Other" bank name, activated if "Others" is selected in bank_name
    other_bank_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Account Detail for {self.client.first_name}-{self.client.phone_number}"  # Assuming BioData has a full_name field

