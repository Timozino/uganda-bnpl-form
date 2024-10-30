from django.db import models
from Bio_Data.models import BioData  

# Choices for Product Usage
PRODUCT_USAGE_CHOICES = [
    ('C', 'Commercial'),
    ('D', 'Domestic'),
]

# Store Detail Model
class StoreDetail(models.Model):
    # Reference to the BioData model
    bio_data = models.ForeignKey(BioData, on_delete=models.CASCADE, related_name="store_details")

    # Sales Agent Name
    sales_agent_name = models.CharField(max_length=100)

    # Product Usage (choices are already defined)
    product_usage = models.CharField(max_length=1, choices=PRODUCT_USAGE_CHOICES)

    # Store Name
    store_name = models.CharField(max_length=255)

    # Product Brand
    product_brand = models.CharField(max_length=100)

    # Freezer Size
    freezer_size = models.CharField(max_length=100)

    # Reference or KB Number
    reference_kb_number = models.CharField(max_length=50)

    # Category (no predefined choices now)
    category = models.CharField(max_length=255)

    # Who are you selling for?
    selling_for = models.CharField(max_length=255)

    def __str__(self):
        return f"Store Detail for {self.bio_data.first_name} {self.bio_data.last_name} with nin {self.bio_data.NIN} - {self.store_name}"
