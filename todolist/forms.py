from django import forms
from .models import TodoList


class TodoLisForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['description', 'due_date', 'done']
