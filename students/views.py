from django.shortcuts import render
from .models import Student

# Create your views here.
def students(request):
    return render(request, "students/students.html", {'students': Student.objects.all()})

def create(request):
    return render(request, "students/create.html")