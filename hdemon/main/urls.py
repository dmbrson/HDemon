from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about', views.about, name = 'about'),
    path('login', views.login, name = 'login'),
    path('register', views.RegisterUser, name = 'register'),
    path('addpage', views.add_film, name = 'addpage'),
    path('film/<int:film_id>', views.show_film, name = 'film'),
    path('category/<int:cat_id>', views.show_category, name = 'category')
]