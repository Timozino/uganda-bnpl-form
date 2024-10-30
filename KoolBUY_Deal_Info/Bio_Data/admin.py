from django.contrib import admin
from .models import BioData

@admin.register(BioData)
class BioDataAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'product_usage')

