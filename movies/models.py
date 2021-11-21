from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.TextField()

class Movie_data(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    vote_average = models.FloatField()
    release_date = models.DateField()
    poster_path = models.TextField()
    video = models.TextField()
    genre_ids = models.ManyToManyField(Genre)
