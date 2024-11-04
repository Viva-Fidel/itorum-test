from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import MailingViewSet, MessagesList


router = SimpleRouter()
router.register(r'mailing', MailingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("messages/", MessagesList.as_view(), name='messages-list'),
]