from dataclasses import field
from django import forms
from .models import Todo

class Todoform(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name', 'due_date']