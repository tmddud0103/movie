from django.contrib import admin

# Register your models here.
from .models import Genre, Movie_data

# Register your models here.
admin.site.register(Genre)
admin.site.register(Movie_data)