from django.http import HttpResponse
from django.shortcuts import render
from .models import *
def index(request):
    films = Films.objects.all()
    cats = Category.objects.all()

    context = {
        'films': films,
        'cats': cats,
        'cat_selected': 0,
    }

    return render(request,  'main/index.html', context=context)
def about(request):
    return render(request,  'main/about.html')
def login(request):
    return render(request,  'main/login.html')
def show_film(request, film_id):
    return HttpResponse(f"Отображение фильма с id = {film_id}")
def show_category(request, cat_id):
    return HttpResponse(f"Отображение жанра с id = {cat_id}")