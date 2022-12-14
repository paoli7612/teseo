from django.shortcuts import render, redirect
from django.contrib import auth
from django import urls
from registro.models import Studente, Indirizzo
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

# STUDENTI
def studenti(request):
    return render(request, 'studente/all.html', {
        'studenti': Studente.objects.all()
    })

def studente(request, slug):
    return render(request, 'studente/show.html', {
        'studente': Studente.objects.get(slug=slug)
    })

#MATERIE
def materie(request):
    return render(request, 'indirizzo/all.html', {
        'materie': Indirizzo.objects.all()
    })

#INDIRIZZI
def indirizzi(request):
    return render(request, 'indirizzo/all.html', {
        'indirizzi': Indirizzo.objects.all()
    })

def indirizzo(request, slug):
    return render(request, 'indirizzo/show.html', {
        'indirizzo': Indirizzo.objects.get(slug=slug)
    })
