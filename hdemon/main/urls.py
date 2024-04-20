from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', FilmsHome.as_view(), name = 'home'),
    path('about', views.about, name = 'about'),
    path('login', LoginUser.as_view(), name = 'aboba'),
    path('logout', vlogout_user, name = 'neaboba'),
    path('register', RegisterUser.as_view(), name = 'register'),
    path('addpage', views.AddPage.as_view(), name = 'addpage'),
    path('film/<slug:slug>/', ShowFilm.as_view(), name='film'),
    path('category/<slug:cat_slug>', CategoryFilms.as_view(), name = 'category')
]