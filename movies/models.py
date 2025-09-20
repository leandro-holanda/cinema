from django.db import models
from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):
    title = models.CharField(max_length=300)
    genre = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor)
    duration_minutes = models.PositiveIntegerField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    resume = models.TextField(blank=True)
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)
