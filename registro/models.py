from django.db import models
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField

class Indirizzo(models.Model):
    class Meta:
        verbose_name_plural = "indirizzi"
        
    nome = models.CharField(max_length=32)
    descrizione = models.TextField(null=True, blank=True)
    liceo = models.BooleanField()
    slug = AutoSlugField(max_length=32, unique=True, populate_from=('nome', ))

    def __str__(self):
        return self.nome

class Studente(models.Model):
    class Meta:
        verbose_name_plural = "studenti"

    nome = models.CharField(max_length=32)
    cognome = models.CharField(max_length=32, null=True)
    nascita = models.DateField()
    slug = AutoSlugField(max_length=32, unique=True, populate_from=('nome','cognome'))
    indirizzo = models.ForeignKey(Indirizzo, on_delete=models.CASCADE, null=True)

    def nome_completo(self):
        return self.cognome + " " + self.nome

    def eta(self):
        import datetime
        return int((datetime.date.today() - self.nascita).days / 365.25  )


    def __str__(self):
        return self.nome_completo()
    

    
