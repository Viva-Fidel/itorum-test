from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ClientViewSet

router = SimpleRouter()
router.register(r'clients', ClientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]