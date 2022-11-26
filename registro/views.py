from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'registro/index.html')

def courses(request):
    return render(request, 'registro/courses/index.html')

def login(request):
    return render(request, 'registro/login.html')