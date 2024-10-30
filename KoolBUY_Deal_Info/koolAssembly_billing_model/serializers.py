from rest_framework import serializers
from .models import BillingModel, PaygoConfig, SalesAgent, OutrightConfig

class PaygoConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaygoConfig
        fields = ['id', 'configuration', 'price']

class SalesAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesAgent
        fields = ['id', 'name', 'code_number', 'location']

class OutrightConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutrightConfig
        fields = ['id', 'configuration', 'price']

class BillingModelSerializer(serializers.ModelSerializer):
    paygo_config = PaygoConfigSerializer(read_only=True)
    sales_agent = SalesAgentSerializer(read_only=True)
    outright_config = OutrightConfigSerializer(read_only=True)

    class Meta:
        model = BillingModel
        fields = [
            'id', 'client', 'billing_model',
            'paygo_config', 'paygo_freezer_price', 'repayment_plan', 'down_payment', 'monthly_instalment',
            'sales_agent', 'outright_config', 'outright_freezer_price'
        ]

    def to_representation(self, instance):
        """
        Customize the serialization output to handle the conditional logic of
        either Paygo or Outright fields based on the billing_model.
        """
        representation = super().to_representation(instance)

        # If billing_model is Paygo, hide Outright fields
        if instance.billing_model == 'Paygo':
            representation.pop('sales_agent', None)
            representation.pop('outright_config', None)
            representation.pop('outright_freezer_price', None)

        # If billing_model is Outright, hide Paygo fields
        elif instance.billing_model == 'Outright':
            representation.pop('paygo_config', None)
            representation.pop('paygo_freezer_price', None)
            representation.pop('repayment_plan', None)
            representation.pop('down_payment', None)
            representation.pop('monthly_instalment', None)

        return representation
