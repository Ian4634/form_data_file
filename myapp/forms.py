from django import forms
from django.forms import ModelForm
from .models import Lesson

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('name', 'time', 'image')

        widgets = {
            'time':forms.TextInput(attrs={'type':'datetime-local'}),
    
        }