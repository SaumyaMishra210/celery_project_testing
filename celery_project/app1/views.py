from django.shortcuts import render 
from django.http import HttpResponse
from .task import *
from celery_project.settings import *
from django.core.mail import send_mail
# Create your views here.

def index(request):
    # sleep_fun(10)
    send_email.delay()
    # try:
    #     send_mail(subject="test email",
    #           message="welcome to the website",
    #           from_email=EMAIL_HOST_USER,
    #           recipient_list=RECIPENT_LIST,
    #           fail_silently=False)
    #     print('success')
    #     return HttpResponse("<h1>Mail sent </h1>")
    # except Exception as e:
    #     print("Failed :",e)
    #     return HttpResponse("<h1>Mail sent Failed </h1>")
    
    return HttpResponse("<h1>welcome to home page </h1>")