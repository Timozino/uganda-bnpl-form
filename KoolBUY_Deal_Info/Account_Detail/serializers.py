from rest_framework import serializers
from .models import AccountDetail

class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountDetail
        fields = [
            'id',
            'client',             # Client's foreign key
            'smart_phone',        # Dropdown for smartphone (yes/no)
            'product',            # Product associated with the client
            'outstanding_loan',   # Dropdown for loan status (yes/no)
            'monthly_income',     # Client's monthly income
            'bank_name',          # Bank name (choices from Nigeria)
            'bank_account_name',  # Client's account name
            'bvn',                # Unique Bank Verification Number (BVN)
            'other_bank_name',    # If "Others" is selected for bank_name
        ]

    # Custom validation to check if `other_bank_name` is required
    def validate(self, data):
        if data['bank_name'] == 'others' and not data.get('other_bank_name'):
            raise serializers.ValidationError("Please provide 'other_bank_name' when 'Others' is selected for bank.")
        return data
