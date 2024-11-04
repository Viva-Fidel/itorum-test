from datetime import datetime
from rest_framework import serializers
from django.utils import timezone

class MailingTimeValidator:
    def __call__(self, data):
        start_datetime = data.get('start_datetime')
        end_datetime = data.get('end_datetime')

        if end_datetime <= timezone.now():
            raise serializers.ValidationError("Время окончания рассылки должно быть в будущем времени")
        
        if start_datetime >= end_datetime:
            raise serializers.ValidationError("Время старта рассылки должно быть раньше времени конца")
