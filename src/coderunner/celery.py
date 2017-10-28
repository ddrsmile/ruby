from __future__ import absolute_import
from celery import Celery
from .config import CeleryConfig

app = Celery('coderunner', include=['coderunner.tasks'])
app.config_from_object(CeleryConfig, namespace='CELERY')
