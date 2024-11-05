import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_project.settings')

app = Celery('celery_project')

# Configure Celery with the Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# # Set the task pool to 'solo'
# app.conf.task_pool = 'solo'

# Set the worker pool to 'solo' (used for debugging)
# app.conf.worker_pool = 'solo'

# celery_beat_settings
app.conf.beat_schedule = {

}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


