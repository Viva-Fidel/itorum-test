from rest_framework import serializers

from .validators import PhoneExistanceValidator, PhoneNumberValidator
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(validators=[PhoneExistanceValidator(), PhoneNumberValidator()])
    mobile_operator_code = serializers.CharField(read_only=True)
    
    class Meta:
        model = Client
        fields = ['id', 'phone_number', 'mobile_operator_code', 'tag']

