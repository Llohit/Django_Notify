from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    path('index/',views.func,name='api')
]
