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

    return render(request, 'community/index.html', context)

@login_required
def detail(request, pk):

    movie_data = get_object_or_404(Movie_data, pk=pk)

    movie_data = movie_data.objects.filter(review_id=movie_data.pk)
    
    context = {
        'movie_data': movie_data,
    }

    return render(request, 'community/detail.html', context)
