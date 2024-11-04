from django.utils import timezone
from celery import shared_task

from clients.models import Client

from .models import Mailing, Messages
import logging

logger = logging.getLogger(__name__)

@shared_task
def start_mailing_task(mailing_id):
    mailing = Mailing.objects.get(id=mailing_id)

    clients = Client.objects.filter(
                mobile_operator_code=mailing.mobile_operator_code,
                tag=mailing.tag
            )
    
    messages_to_create = []

    for client in clients:

        if timezone.now() > mailing.end_datetime:
                logger.info(f"Текущая дата превышает время завершения рассылки {mailing.id}. Отправка сообщений остановлена")
                break
        
        messages_to_create.append(Messages(mailing=mailing, client=client))

    if messages_to_create:
        created_messages = Messages.objects.bulk_create(messages_to_create)

        for message in created_messages:
            logger.info(f"Сообщение {message.id} отправлено клиенту {message.client.id}. Текст сообщения: {mailing.message_text}")

        
