from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from .utils import *
from .forms import *
from .models import *

class FilmsHome(ListView):
    model = Films
    template_name = 'main/index.html'
    context_object_name = 'films'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.all()
        context['cat_selected'] = 0
        return context
# def index(request):
#     films = Films.objects.all()
#     cats = Category.objects.all()
#
#     context = {
#         'films': films,
#         'cats': cats,
#         'cat_selected': 0,
#     }

    # return render(request,  'main/index.html', context=context)
def about(request):
    return render(request,  'main/about.html')
# def login(request):
#     return render(request,  'main/login.html')
# def add_film(request):
#     if request.method == 'POST':
#         form = AddFilmForm(request.POST, request.FILES)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             try:
#                 Films.objects.create(**form.cleaned_data)
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Ошибка')
#     else:
#         form = AddFilmForm()
#     return render(request,  'main/addpage.html', {'form': form})

class AddPage(CreateView):
    form_class = AddFilmForm
    template_name = 'main/addpage.html'
    success_url = reverse_lazy('home')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# def show_film(request, film_id):
#     film = get_object_or_404(Films, id=film_id)
#
#     context = {
#         'film': film,
#         'cat_selected': film.cat_id,
#     }
#
#     return render(request, 'main/film.html', context=context)

class ShowFilm(DetailView):
    model = Films
    template_name = 'main/film.html'
    context_object_name = 'film'
    slug_field = 'slug'

class CategoryFilms(ListView):
    model = Films
    template_name = 'main/index.html'
    context_object_name = 'films'
    allow_empty = False

    def get_queryset(self):
        return Films.objects.filter(cat__slug=self.kwargs['cat_slug'])
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.all()
        context['cat_selected'] = self.kwargs['cat_slug']
        return context

# def show_category(request, cat_id):
#     films = Films.objects.filter(cat_id=cat_id)
#     cats = Category.objects.all()
#
#     context = {
#         'films': films,
#         'cats': cats,
#         'cat_selected': cat_id,
#     }
#
#     if len(films) == 0:
#         raise Http404()
#
#     return render(request,  'main/index.html', context=context)

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))
    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')