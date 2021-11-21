from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST, require_GET, require_http_methods, require_safe
from django.contrib.auth.decorators import login_required
from .models import Community_review, Community_comment
from movies.models import Genre
from .forms import Community_reviewForm, Community_commentForm
import requests
from bs4 import BeautifulSoup
# Create your views here.

@require_safe
def index(request):
    
    community_review = Community_review.objects.all()

    context = {
        'community_review': community_review,
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
        # print(tt)
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

def recommend(request):
    return render(request, 'community/recommend.html')

def choose(request):
    genres = Genre.objects.all()
    context = {
            'genres':genres,
        }
    return render(request, 'community/choose.html', context)

def like_choose(request, username, id):
    genres = get_object_or_404(Genre, pk=id)
    print(request)
    if genres.like_users.filter(id=request.user.pk).exists():
        genres.like_users.remove(request.user)
        genres.save()
        print('aa')
    else:
        genres.like_users.add(request.user)
        genres.save()
        print('bb')
    print(genres.like_users.all())
    return redirect('community:choose')