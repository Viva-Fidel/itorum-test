from rest_framework import serializers
from django.utils import timezone

from .validators import MailingTimeValidator
from .models import Mailing, Messages

class MailingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Mailing
        fields = '__all__'

    validators = [MailingTimeValidator()]

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'