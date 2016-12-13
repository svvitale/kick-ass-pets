from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

from django.conf import settings

celery_app = Celery('kickasspets')

# Using a string here means the worker don't have to serialize the configuration object to child processes.
celery_app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
