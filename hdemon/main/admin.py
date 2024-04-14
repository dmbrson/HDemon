from django.contrib import admin
from .models import *

class FilmsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'year', 'photo', 'time_created')
    list_filter_links = ('id', 'title')
    search_fields = ('title', 'content')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Films, FilmsAdmin)
admin.site.register(Category, CategoryAdmin)