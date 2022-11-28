from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=16)
    surname = models.CharField(max_length=16)

    def __str__(self):
        return self.name + " " + self.surname

class Course(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    name = models.CharField(max_length=32)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.name
    
