from django import forms
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