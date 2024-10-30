from django.db import models
from Bio_Data.models import BioData
from koolAssembly_billing_model.models import SalesAgent  

class OtherDetails(models.Model):
    # ForeignKey to BioData model (client details)
    client = models.ForeignKey(BioData, on_delete=models.CASCADE, related_name="other_details")

    # ForeignKey to SalesAgent model
    sales_agent = models.ForeignKey(SalesAgent, on_delete=models.CASCADE, related_name="other_details")

    # Guarantor's full name
    guarantor_fullname = models.CharField(max_length=255)

    # Guarantor's phone number
    guarantor_phone_number = models.CharField(max_length=15, unique=True)  # Adjust length based on expected phone format

    # Guarantor's NIN
    guarantor_nin = models.CharField(max_length=11, unique=True)  # National Identification Number length in Nigeria

    # Guarantor's NIN image (upload field)
    guarantor_nin_image = models.ImageField(upload_to='guarantor_nin_images/')  # Ensure MEDIA_URL is configured

    # Reason for purchase
    reason_for_purchase = models.TextField()

    # Referee's full name
    referee_fullname = models.CharField(max_length=255)

    # Referee's phone number
    referee_phone_number = models.CharField(max_length=15, unique=True)  # Adjust length based on expected phone format

    # Second referee's full name
    second_referee_fullname = models.CharField(max_length=255)

    # Second referee's phone number
    second_referee_phone_number = models.CharField(max_length=15, unique=True)  # Adjust length based on expected phone format

    # Product photo upload
    product_photo = models.ImageField(upload_to='product_photos/')

    # Client's photo
    client_photo = models.ImageField(upload_to='client_photos/')

    # Client's NIN image
    client_nin_image = models.ImageField(upload_to='client_nin_images/')

    # Bank statements upload fields
    bank_statements_image = models.ImageField(upload_to='bank_statements/images/', blank=True, null=True)
    bank_statements_pdf = models.FileField(upload_to='bank_statements/pdfs/', blank=True, null=True)

    # Home utility bill upload fields
    home_utility_bill_image = models.ImageField(upload_to='utility_bills/home/images/', blank=True, null=True)
    home_utility_bill_pdf = models.FileField(upload_to='utility_bills/home/pdfs/', blank=True, null=True)

    # Business utility bill upload fields
    business_utility_bill_image = models.ImageField(upload_to='utility_bills/business/images/', blank=True, null=True)
    business_utility_bill_pdf = models.FileField(upload_to='utility_bills/business/pdfs/', blank=True, null=True)

    def __str__(self):
        return f"Other Details for {self.client.first_name} - {self.guarantor_fullname}"
