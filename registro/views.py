from django.shortcuts import render, redirect
from django.contrib import auth
from .models import *
from .forms import NewCourse


def index(request):
    return render(request, 'registro/index.html')

def courses(request):
    return render(request, 'registro/courses/index.html', {
        'courses': Course.objects.all()
    })

def subjects(request):
    return render(request, 'registro/subjects/index.html', {
        'subjects': Course.objects.all()
    })


def lessons(request):
    return render(request, 'registro/lessons/index.html', {
        'lessons': Course.objects.all()
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


def register(request):
    return render(request, 'registro/registration/register.html')


def new_course(request):
    if request.method == 'POST':
        f = NewCourse(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/')

    return render(request, 'registro/courses/new_course.html', {
        'form': NewCourse
    })
