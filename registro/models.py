from django.db import models
from django_extensions.db.fields import AutoSlugField

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=16)
    surname = models.CharField(max_length=16)

    def __str__(self):
        return self.name + " " + self.surname



class Course(models.Model):
    name = models.CharField(max_length=16)
    slug = AutoSlugField(max_length=16, unique=True, populate_from=('name', ))
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def url(self):
        return '/courses/' + self.slug

class Lesson(models.Model):
    name = models.CharField(max_length=32)
    slug = AutoSlugField(max_length=16, unique=True, populate_from=('name', ))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.name
    
