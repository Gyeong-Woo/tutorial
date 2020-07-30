
from django.contrib import admin
from django.urls import path, include
from thirdapp import views

urlpatterns = [
    path('hospital/', views.hospital),
   
]
