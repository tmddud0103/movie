from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST, require_GET, require_http_methods, require_safe
from django.contrib.auth.decorators import login_required

from movies.models import Movie_data
# Create your views here.

@require_safe
def index(request):
    
    movie_data_all = Movie_data.objects.all()

    context = {
        'movie_data_all': movie_data_all,
    }

    return render(request, 'movies/index.html', context)

@login_required
def detail(request, pk):

    movie_data = get_object_or_404(Movie_data, pk=pk)
    star = []
    star_fill = []
    star_half = []

    for i in range(int(movie_data.vote_average) // 2):
        star_fill.append(1)
    
    if int(movie_data.vote_average) % 2 == 1:
        star_half.append(1)

    for i in range(5-len(star_fill)-len(star_half)):
        star.append(1)

    context = {
        'movie_data': movie_data,
        'star': star,
        'star_fill': star_fill,
        'star_half': star_half,
    }

    return render(request, 'movies/detail.html', context)
