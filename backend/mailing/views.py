from rest_framework import viewsets
from rest_framework import generics
from django.utils import timezone

from .tasks import start_mailing_task
from .models import Mailing, Messages
from .serializers import MailingSerializer, MessagesSerializer

# Create your views here.
class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

    def perform_create(self, serializer):
        mailing = serializer.save()
        now = timezone.now()

        if  mailing.start_datetime <= now <= mailing.end_datetime:
            start_mailing_task.delay(mailing.id)
        elif mailing.start_datetime > now:
            start_mailing_task.apply_async((mailing.id,), eta=mailing.start_datetime)


class MessagesList(generics.ListAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
