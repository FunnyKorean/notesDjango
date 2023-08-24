from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from .models import Note


class RegisterForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['username', 'email']


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'due_date']

        widgets = {
            'due_date': forms.TextInput(attrs={'type': 'datetime-local'}),
        }
