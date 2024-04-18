from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', FilmsHome.as_view(), name = 'home'),
    path('about', views.about, name = 'about'),
    path('login', views.login, name = 'login'),
    # path('register', views.RegisterUser, name = 'register'),
    path('addpage', views.add_film, name = 'addpage'),
    path('film/<int:film_id>/', ShowFilm.as_view(), name='film'),
    path('category/<int:cat_id>', CategoryFilms.as_view(), name = 'category')
]