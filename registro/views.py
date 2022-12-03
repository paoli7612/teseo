from django.shortcuts import render
from .models import *
from django.shortcuts import redirect


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

def account(request):
    if request.user.is_authenticated:
        return render(request, 'registro/account.html', {
            'user': request.user
        })
    else:
        return redirect('login')

def login(request):
    return render(request, 'registro/registration/login.html')

def register(request):
    return render(request, 'registro/registration/register.html')