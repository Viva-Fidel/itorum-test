from django.contrib import admin

from .models import Mailing, Messages

# Register your models here.
@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_datetime', 'end_datetime', 'mobile_operator_code', 'tag')
    list_filter = ('mobile_operator_code', 'tag', 'start_datetime', 'end_datetime')
    search_fields = ('id', 'mobile_operator_code', 'tag')
    date_hierarchy = 'start_datetime'

@admin.register(Messages)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sent_datetime', 'mailing', 'client')
    list_filter = ('sent_datetime', 'mailing')
    search_fields = ('id', 'mailing__id', 'client__id')
    date_hierarchy = 'sent_datetime'