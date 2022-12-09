from django import forms
from .models import Course, Subject

class NewCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', )

