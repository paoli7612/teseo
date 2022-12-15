from django.db import models
from django_extensions.db.fields import AutoSlugField

# Create your models here.

class Student(models.Model):

    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32, null=True)
    birth = models.DateField()
    slug = AutoSlugField(max_length=32, unique=True, populate_from=('name',))

    def complete_name(self):
        return self.surname + " " + self.name

    def __str__(self):
        return self.complete_name()
    
class Course(models.Model):

    name = models.CharField(max_length=32)
