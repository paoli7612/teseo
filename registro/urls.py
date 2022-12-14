from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('account', views.account, name="account"),
    path('studenti', views.studenti, name="studenti"),
    path('studenti/<slug:slug>', views.studente, name="studente"),
    path('indirizzi', views.indirizzi, name="indirizzi"),
    path('indirizzi/<slug:slug>', views.indirizzo, name="indirizzo"),
    path('materie', views.materie, name="materie")
]
