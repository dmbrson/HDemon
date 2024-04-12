from django.db import models

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

    def __str__(self):
        return self.title