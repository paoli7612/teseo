from django.db import models
from django_extensions.db.fields import AutoSlugField

# Create your models here.
class Mode(models.Model):
    name = models.CharField(max_length=16, unique=True)
    slud = AutoSlugField(max_length=16, unique=True, populate_from=('name', ))

class Course(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(null=True, blank=True)
    mode = models.ForeignKey(Mode, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):

    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32, null=True)
    birth = models.DateField()
    slug = AutoSlugField(max_length=32, unique=True, populate_from=('name',))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    def complete_name(self):
        return self.surname + " " + self.name

    def __str__(self):
        return self.complete_name()
    

    
