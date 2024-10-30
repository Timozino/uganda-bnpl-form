from rest_framework import serializers
from .models import BioData

class BioDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BioData
        fields = '__all__'  
