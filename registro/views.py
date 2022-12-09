from django.shortcuts import render, redirect
from django.contrib import auth
from .models import *
from .forms import NewCourse, NewLesson


def index(request):
    return render(request, 'index.html')


def subjects(request):
    return render(request, 'subjects/index.html', {
        'subjects': Subject.objects.all()
    })


def courses(request):
    return render(request, 'courses/index.html', {
        'courses': Course.objects.all()
    })


def lessons(request):
    return render(request, 'lessons/index.html', {
        'lessons': Lesson.objects.all()
    })


def course(request, slug):
    return render(request, 'courses/show.html', {
        'course': Course.objects.get(slug=slug)
    })


def account(request):
    if request.user.is_authenticated:
        return render(request, 'account.html', {
            'user': request.user
        })
    else:
        return redirect('login')


def register(request):
    return render(request, 'registration/register.html')

def new_course(request):
    if request.method == 'POST':
        f = NewCourse(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/')

    return render(request, 'courses/new.html', {
        'form': NewCourse
    })

def new_lesson(request):
    if request.method == 'POST':
        f = NewLesson(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/')

    return render(request, 'lessons/new.html', {
        'form': NewCourse
    })
