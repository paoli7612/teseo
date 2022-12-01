from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User as Account

def index(request):
    return render(request, 'registro/index.html')

def courses(request):
    return render(request, 'registro/courses/index.html', {
        'courses': Course.objects.all()
    })

def course(request, slug):
    return render(request, 'registro/courses/show.html', {
        'course': Course.objects.get(slug=slug)
    })

def account(request, email):
    print(email)
    return render(request, 'registro/account/show.html', {
        'account': Account.objects.get(email=email) 
    })


def login(request):
    return render(request, 'registro/login.html')