from .views import *
from django.urls import path

urlpatterns = [
    path("",home,name="home"),
    path("Teacher/",Teach,name="Teach"),
        path("staff/",staff,name="staff"),


]
