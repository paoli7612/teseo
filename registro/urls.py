from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('subjects', views.subjects, name='subjects'),
    path('courses', views.courses, name='courses'),
    path('lessons', views.lessons, name='lessons'),
    path('subjects/<slug:slug>', views.subject, name='subject'),
    path('courses/<slug:slug>', views.course, name='course'),
    path('lessons/<slug:slug>', views.lesson, name='lesson'),
    path('new-course/', views.new_course, name='new-course'),
    path('new-lesson/', views.new_lesson, name='new-lesson')
]
