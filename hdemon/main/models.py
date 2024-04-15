from django.db import models
from django.urls import reverse

class Films(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    time_created = models.DateTimeField(auto_now_add=True)
    year = models.CharField(max_length=100, null=True)
    director = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    actors = models.TextField(blank=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    class  Meta:
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('film', kwargs={'film_id': self.pk})

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    class  Meta:
        verbose_name_plural = 'Жанры'
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
