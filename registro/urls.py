from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('subjects', views.subjects, name='subjects'),
    path('courses', views.courses, name='courses'),
    path('lessons', views.lessons, name='lessons'),
    path('courses/<slug:slug>', views.course, name='course'),
    path('new-subject/', views.new_course, name='new-subject'),
    path('new-course/', views.new_course, name='new-course'),
    path('new-lesson/', views.new_course, name='new-lesson')
]
