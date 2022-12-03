from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from . import views
from .forms import LoginForm

urlpatterns = [
    path('', views.index, name='home'),
    path('courses', views.courses, name='courses'),
    path('courses/<slug:slug>', views.course, name='course'),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('account/', views.account, name='account'),
]
