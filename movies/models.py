from django.db import models
from django.conf import settings
from accounts.models import User
# Create your models here.
class Genre(models.Model):
    name = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews', blank=True)

class Movie_data(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    vote_average = models.FloatField()
    release_date = models.DateField()
    poster_path = models.TextField()
    backdrop_path = models.TextField()
    video = models.TextField()
    genre_ids = models.ManyToManyField(Genre)

class Combinding(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)