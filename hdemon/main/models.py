from django.db import models
from django.urls import reverse

class Films(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='img/')
    time_created = models.DateTimeField(auto_now_add=True)
    director = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    actors = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    age_restrictions = models.TextField(max_length=255)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('film', kwargs={'film_id': self.pk})

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
