from rest_framework import serializers

from .models import Client

# Валидатор правильности ввода тел. номера
class PhoneNumberValidator:
    def __call__(self, value):
        if not value.startswith('7'):
            raise serializers.ValidationError("Телефонный номер должен начинаться с 7")

        if len(value) != 11 or not value.isdigit():
            raise serializers.ValidationError("Телефонный номер должен содержать 11 символов и состоять только из цифр")

# Валидатор существования тел. номера
class PhoneExistanceValidator:
    def __call__(self, value):
        if Client.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("Пользователь с таким номером телефона уже существует")
        return value