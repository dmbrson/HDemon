from django.shortcuts import render
from .models import *
def index(request):
    posts = Films.objects.all()
    return render(request,  'main/index.html', {'posts': posts})
def about(request):
    return render(request,  'main/about.html')