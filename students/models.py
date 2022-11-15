from django.db import models

# Create your models here.
class Student(models.Model):
    immagine = models.ImageField()
    nome = models.CharField(max_length=16)
    cognome = models.CharField(max_length=32)

    def __str__(self):
        return self.cognome + " " + self.nome
    