from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="index"),
    path('works/', views.works, name="works"),
    path('about/', views.about, name="about"),
    path('contactus/', views.contactus, name="contactus"),
]
