from django.contrib import admin

from .models import Client

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'mobile_operator_code', 'tag')
    search_fields = ('phone_number', 'mobile_operator_code', 'tag')