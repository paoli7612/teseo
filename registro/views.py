from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse
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


def subject(request, slug):
    return render(request, 'subjects/show.html', {
        'subject': Subject.objects.get(slug=slug)
    })

def course(request, slug):
    return render(request, 'courses/show.html', {
        'course': Course.objects.get(slug=slug)
    })

def lesson(request, slug):
    return render(request, 'lessons/show.html', {
        'lesson': Lesson.objects.get(slug=slug)
    })


def new_course(request):
    if request.method == 'POST':
        f = NewCourse(request.POST)
        if f.is_valid():
            f.save()
            return redirect(reverse('courses'))

    return render(request, 'courses/new.html', {
        'form': NewCourse
    })

def new_lesson(request):
    if request.method == 'POST':
        f = NewLesson(request.POST)
        if f.is_valid():
            f.save()
            return redirect(reverse('lessons'))

    return render(request, 'lessons/new.html', {
        'form': NewLesson()
    })
