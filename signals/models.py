from django.db import models
from django.dispatch import receiver 
from django.db.models.signals import post_save
import time
import threading
import logging
from django.db import transaction
# Create your models here.
logger = logging.getLogger(__name__)






class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()

    def __str__(self):
        return self.name

@receiver(post_save, sender=Teacher)
def teacher_saved(sender,instance,created,**kwargs):
    print("Signal Handler Thread:", threading.current_thread().name)


class Staff(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()

    def __str__(self):
        return self.name

@receiver(post_save, sender=Staff)
def staff_saved(sender,instance,created,**kwargs):
    logger.info("Inside signal handler")
    if created:
        instance.name="Updated by signal"
        instance.save()
    




@receiver(post_save, sender=Student)
def student_saved(sender,instance,created,**kwargs):
    print('Handler Started')
    time.sleep(30)
    print("Handler ended")


