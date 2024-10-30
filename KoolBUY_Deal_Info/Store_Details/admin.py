
from django.contrib import admin
from .models import StoreDetail

class StoreDetailAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = (
        'sales_agent_name', 
        'product_usage', 
        'store_name', 
        'product_brand', 
        'freezer_size', 
        'reference_kb_number', 
        'category', 
        'selling_for',
        'bio_data'
    )

    # Fields to filter by in the right sidebar
    list_filter = ('product_usage', 'product_brand', 'category')

    # Searchable fields
    search_fields = ('sales_agent_name', 'store_name', 'product_brand', 'reference_kb_number')

    # If you want to make the bio_data editable as a dropdown list of existing BioData entries
    raw_id_fields = ('bio_data',)

# Register the StoreDetail model
admin.site.register(StoreDetail, StoreDetailAdmin)
