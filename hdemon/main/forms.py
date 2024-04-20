from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class AddFilmForm(forms.ModelForm):
    class Meta:
        model = Films
        fields = ['title', 'content', 'photo', 'year', 'director', 'country', 'actors', 'cat']
        labels = {
            'title': 'Название фильма',
            'content': 'Описание',
            'year': 'Год выпуска',
            'director': 'Режиссер',
            'country': 'Страна',
            'actors': 'Актёры',
            'cat': 'Жанр',
        }
        widgets = {
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'actors': forms.Textarea(attrs={'cols': 60, 'rows': 1}),
        }

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.TextInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-input'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-input'})
        # }