from django.shortcuts import render, redirect
from django.contrib import auth
from django import urls
from registro.models import Student
# Create your views here.

def home(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username, password = request.POST['username'], request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect(urls.reverse('account'))
    return render(request, 'auth/login.html')

def logout(request):
    auth.logout(request)
    return redirect(urls.reverse('home'))

def account(request):
    return render(request, 'auth/account.html', {
        'user': request.user
    })

def students(request):
    return render(request, 'student/all.html', {
        'students': Student.objects.all()
    })