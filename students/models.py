from django.db import models

# Create your models here.
class Student(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=16)
    surname = models.CharField(max_length=32)

    def __str__(self):
        return self.surname + " " + self.name
    
    def completename(self):
        return str(self)
    