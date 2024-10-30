from rest_framework import serializers
from .models import OtherDetails

class OtherDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherDetails
        fields = '__all__'  
