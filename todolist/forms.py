# todolist/forms.py

from django import forms
from .models import Todolist

class TodoListForm(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a task...'
            })
        }
