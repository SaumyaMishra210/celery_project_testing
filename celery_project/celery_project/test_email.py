
from celery_project.settings import EMAIL_HOST_USER,RECIPENT_LIST
from django.core.mail import send_mail

send_mail(subject="test email",
              message="welcome to the website",
              from_email=EMAIL_HOST_USER,
              recipient_list=RECIPENT_LIST,
              fail_silently=False)
