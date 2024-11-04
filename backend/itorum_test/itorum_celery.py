import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "itorum_test.settings")
app = Celery("itorum_test")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


# celery -A itorum_test worker -l INFO