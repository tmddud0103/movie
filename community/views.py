from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST, require_GET, require_http_methods, require_safe
from django.contrib.auth.decorators import login_required
from .models import Community_review, Community_comment
from movies.models import Genre, Movie_data
from accounts.models import User
from .forms import Community_reviewForm, Community_commentForm
from bs4 import BeautifulSoup
import requests
import random
# Create your views here.

@require_safe
def index(request):
    
    community_reviews = Community_review.objects.all()

    context = {
        'community_reviews': community_reviews,
    }

    return render(request, 'community/index.html', context)

@login_required
def detail(request, pk):

    community_review = get_object_or_404(Community_review, pk=pk)

    community_comment = Community_comment.objects.filter(review_id=community_review.pk)
    
    community_commentForm = Community_commentForm()

    context = {
        'community_review': community_review,
        'community_comment': community_comment,
        'community_commentForm': community_commentForm,
    }

    return render(request, 'community/detail.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = Community_reviewForm(request.POST)

        if form.is_valid():
            community_review = form.save(commit=False)
            community_review.user_id = request.user
            community_review.save()
            return redirect('community:detail', community_review.pk)

    else:
        form = Community_reviewForm()
    
    context = {
        'form': form,
    }

    return render(request, 'community/form.html', context)

@login_required
@require_POST
def delete(request, pk):
    
    review = get_object_or_404(Community_review, pk=pk)
    review.delete()

    return redirect('community:index')

@login_required
@require_POST
def comments_create(request, pk):
    
    community_review = get_object_or_404(Community_review, pk=pk)
    
    community_commentForm = Community_commentForm(request.POST)
    
    if community_commentForm.is_valid():
        community_comment = community_commentForm.save(commit=False)
        community_comment.review_id = community_review
        community_comment.user_id = community_review.user_id
        community_comment.save()
        return redirect('community:detail', community_review.pk)

    return redirect('community:index')


def onair(request):
    url = 'https://movie.naver.com/movie/running/current.naver'
    res = requests.get(url)
    data = BeautifulSoup(res.text, 'html.parser')
    uls = data.find("ul", class_="lst_detail_t1").find_all("dt", class_="tit")
    img = data.find("ul", class_="lst_detail_t1").find_all("img")
    movies = []
    for i, title in enumerate(uls):
        temp = []
        tt = " ".join(title.get_text().split()[2:])
        temp.extend([i + 1, tt])
        for j, title in enumerate(img):
            if temp[0] == j+1:
                temp.append(title["src"][:-15])
                break
        movies.append(temp)
    if len(movies) > 18:
        context = {
            'movies':movies[:18],
        }
    else:
        context = {
            'movies':movies,
        }
    return render(request, 'community/onair.html', context)

def choose(request):
    genres = Genre.objects.all()
    profile_user = request.user
    context = {
            'genres':genres,
            'profile_user' : profile_user,
        }
    return render(request, 'accounts/profile.html', context)

def like_choose(request, username, id):
    genres = get_object_or_404(Genre, pk=id)
    if genres.like_users.filter(id=request.user.pk).exists():
        genres.like_users.remove(request.user)
        genres.save()
    else:
        genres.like_users.add(request.user)
        genres.save()
    print(genres.like_users.all())
    return redirect('community:choose')


def recommend(request):
    user =  get_object_or_404(User, pk=request.user.id)
    movie_data = Movie_data.objects.all()
    like_genres = user.like_reviews.all()
    genre_dict = {}
    if len(like_genres)> 0:
        for like_genre in like_genres:
            genre_dict[like_genre.id] = []
    for movie in movie_data:
        # print(movie.genre_ids.all())
        for key in genre_dict.keys():
            if movie.genre_ids.filter(id=key):
                genre_dict[key].append(movie)
    for key, value in genre_dict.items():
        if len(genre_dict[key]) > 6:
            genre_dict[key] = random.sample(genre_dict[key], 6)
        
    context = {
        'like_genres': like_genres, 
        'range': len(like_genres),
        'genre': genre_dict,
    }

    return render(request, 'community/recommend.html', context)


