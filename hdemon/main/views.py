from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
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
    film = get_object_or_404(Films, id=film_id)

    context = {
        'film': film,
        'cat_selected': film.cat_id,
    }

    return render(request, 'main/film.html', context=context)

def show_category(request, cat_id):
    films = Films.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    context = {
        'films': films,
        'cats': cats,
        'cat_selected': cat_id,
    }

    if len(films) == 0:
        raise Http404()

    return render(request,  'main/index.html', context=context)
