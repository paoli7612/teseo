from django.db import models
from django_extensions.db.fields import AutoSlugField


class Subject(models.Model):
    name = models.CharField(max_length=16)
    slug = AutoSlugField(max_length=16, unique=True, populate_from=('name', ))
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def url(self):
        return '/subjects/' + self.slug


class Course(models.Model):
    name = models.CharField(max_length=16)
    slug = AutoSlugField(max_length=16, unique=True, populate_from=('name', ))
    description = models.TextField(null=True, blank=True)
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.name

    def url(self):
        return '/courses/' + self.slug


class Lesson(models.Model):
    name = models.CharField(max_length=16)
    slug = AutoSlugField(max_length=16, unique=True, populate_from=('name', ))
    description = models.TextField(null=True, blank=True)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.name

    def url(self):
        return '/lessons/' + self.slug
