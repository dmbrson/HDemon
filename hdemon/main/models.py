from django.db import models
from django.urls import reverse

class Films(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    time_created = models.DateTimeField(auto_now_add=True)
    year = models.CharField(max_length=100, null=True)
    director = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    actors = models.TextField(blank=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)

    class  Meta:
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('film', kwargs={'slug': self.slug})

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)


    class  Meta:
        verbose_name_plural = 'Жанры'
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})
