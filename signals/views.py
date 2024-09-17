from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,Teacher,Staff
import time
import threading
from django.db import transaction
import logging

logger = logging.getLogger(__name__)
# Create your views here.


def home(request):
    print('Started To Create Student Record')
    current_time=time.time()
    Student.objects.create(name="adi",age=20)
    print("Student object Created")
    print(f"time taken:{time.time()-current_time} seconds")

    return HttpResponse('Welcome to home page !!!')

def Teach(request):
    print("View Thread:", threading.current_thread().name)
    Teacher.objects.create(name="Arun",age=30)
    return HttpResponse('Welcome to teacher page !!!')

def staff(request):
    try:
        with transaction.atomic():  
            staffmem = Staff.objects.create(name="Ajay", age=30)
            logger.info("Staff object created")
            raise Exception("Triggering rollback")
    except Exception:
        
        logger.info("Transaction rolled back")

    return HttpResponse('Welcome to staff page !!!')