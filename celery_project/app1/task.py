# Create your tasks here

from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from celery_project.settings import *


@shared_task
def add(x, y):
    return x + y

@shared_task
def sleep_fun(duration):
    sleep(duration)
    return None

@shared_task
def send_email():
    print(RECIPENT_LIST)
    try:
        send_mail(subject="test email",
              message="welcome to the website",
              from_email=EMAIL_HOST_USER,
              recipient_list= RECIPENT_LIST,
              fail_silently=False)
    except Exception as e:
        print("error :",e)
    return "Done"