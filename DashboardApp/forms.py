from django import forms
from .models import Lesson, Event

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'description', 'content', 'category', 'difficulty', 'duration', 'resources', 'creator']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'start_date', 'end_date', 'location', 'poster']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "start_date": forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"}),
            "end_date": forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "poster": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
