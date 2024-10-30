from django.db import models
from django.core.exceptions import ValidationError

# Choices for Gender
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]

# Choices for Marital Status
MARITAL_STATUS_CHOICES = [
    ('S', 'Single'),
    ('M', 'Married'),
    ('W', 'Widowed'),
]

# Choices for Product Usage
PRODUCT_USAGE_CHOICES = [
    ('C', 'Commercial'),
    ('D', 'Domestic'),
]

# Choices for Lead Source
LEAD_SOURCE_CHOICES = [
    ('AD', 'Advertisement'),
    ('ER', 'Employee Referral'),
    ('FB', 'Facebook'),
    ('GS', 'Google Search'),
    ('CH', 'Chat'),
    ('WC', 'Walk-in Client'),
]

class BioData(models.Model):
    # Applicant's Basic Info
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()  # Format: dd-MMM-yyyy
    
    # Phone numbers with validation
    phone_number = models.CharField(max_length=14)  # Length includes +234 prefix
    alternate_phone_number = models.CharField(max_length=14, blank=True, null=True)  # Optional
    
    email = models.EmailField(unique=True)
    
    # Home Address
    street_name = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100, default='Uganda')

    # Marital Status
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES)

    # Product Usage
    product_usage = models.CharField(max_length=1, choices=PRODUCT_USAGE_CHOICES)
    
    # Fields specific to commercial use
    business_name = models.CharField(max_length=255, blank=True, null=True)
    business_type = models.CharField(max_length=100, blank=True, null=True)
    business_size = models.CharField(max_length=50, blank=True, null=True)
    business_address = models.TextField(blank=True, null=True)

    # Additional Info
    number_of_dependents = models.PositiveIntegerField(default=0)
    NIN = models.CharField(max_length=20, unique=True)  # National Identification Number
    occupation = models.CharField(max_length=100)

    # Lead Source
    lead_source = models.CharField(max_length=2, choices=LEAD_SOURCE_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone_number}"

    # Validate phone numbers
    def clean(self):
        super().clean()
        if not self.phone_number.startswith("+256"):
            raise ValidationError("Phone number must start with +256.")
        if len(self.phone_number) != 14 or not self.phone_number[4:].isdigit():
            raise ValidationError("Phone number must be 10 digits long after the +256.")
        
        if self.alternate_phone_number:
            if not self.alternate_phone_number.startswith("+256"):
                raise ValidationError("Alternate phone number must start with +256.")
            if len(self.alternate_phone_number) != 14 or not self.alternate_phone_number[4:].isdigit():
                raise ValidationError("Alternate phone number must be 10 digits long after the +256.")

    # Ensure that business fields are filled only for commercial product usage
    def save(self, *args, **kwargs):
        if self.product_usage == 'D':  # Domestic use
            self.business_name = None
            self.business_type = None
            self.business_size = None
            self.business_address = None
        super(BioData, self).save(*args, **kwargs)

