import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bit_app.settings")
app = Celery("bit")
app.config_from_object("bit_app.settings.celery_config")
app.autodiscover_tasks()
