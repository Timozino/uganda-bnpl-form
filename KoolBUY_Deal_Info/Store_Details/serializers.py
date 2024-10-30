from rest_framework import serializers
from .models import StoreDetail

class StoreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreDetail
        fields = [
            'id',  # ID for referencing the store detail
            'bio_data',  # ForeignKey field to BioData
            'sales_agent_name',
            'product_usage',
            'store_name',
            'product_brand',
            'freezer_size',
            'reference_kb_number',
            'category',
            'selling_for',
        ]

    
    # def validate_reference_kb_number(self, value):
    #     if not value.startswith("KB"):
    #         raise serializers.ValidationError("Reference or KB Number should start with 'KB'.")
    #     return value
