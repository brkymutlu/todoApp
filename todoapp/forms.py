from django import forms
from .models import *

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['todo']

        widgets = {
            'todo':forms.TextInput(attrs={'class':'form-control w-50 border border-2 border-black'})
        }