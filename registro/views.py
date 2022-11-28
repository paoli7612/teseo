from django.shortcuts import render
from .models import Course

# Create your views here.
def index(request):
    return render(request, 'registro/index.html')

def courses(request):
    return render(request, 'registro/courses/index.html', {
        'courses': Course.objects.all()
    })

def login(request):
    return render(request, 'registro/login.html')