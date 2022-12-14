from django import forms
from .models import Course, Lesson, Subject

class NewCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'subject')
    
class NewLesson(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('name', 'course')



