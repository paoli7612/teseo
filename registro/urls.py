from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('courses', views.courses, name='courses'),
    path('courses/<slug:slug>', views.course, name='course'),
]
