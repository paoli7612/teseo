from django import forms
from .models import Course, Lesson

class NewCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', )
    
class NewLesson(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('name', 'subject')


