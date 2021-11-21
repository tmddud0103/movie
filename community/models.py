from django.db import models
from accounts.models import User
from django.conf import settings
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
    video = models.TextField()
    genre_ids = models.ManyToManyField(Genre)

class Community_review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Community_comment(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review_id = models.ForeignKey(Community_review, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Combinding(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)