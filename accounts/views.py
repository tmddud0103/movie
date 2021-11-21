# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render
from accounts.forms import CustomUserCreationForm
from django.contrib.auth import get_user_model, login as auth_login, logout as auth_logout
from .models import User_genre
from .genre_id import GENRE

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('community:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }

    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('community:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('community:index')


def profile(request, username):
    User = get_user_model()
    profile_user = get_object_or_404(User, username=username)
    genres = GENRE
    usergenre = User_genre
    context = {
        'profile_user' : profile_user,
        'genres' : genres,
        'usergenre' : usergenre,
    }
    return render(request, 'accounts/profile.html', context)


def follow(request, pk):
    User = get_user_model()
    me = request.user
    you = get_object_or_404(User, pk=pk)
    if me in you.followers.all():
        me.followings.remove(you)
    else:
        me.followings.add(you)
    return redirect('accounts:profile', you.username)


# follow() got an unexpected keyword argument 'username'
# typeerror - pk가 와야하는데 username들어옴
# 'User' object has no attribute 'followers'
def prefer(request, username, pk, id):
    genre = User_genre.like_genres
    
    tmd = username
    User = get_user_model()
    profile_user = get_object_or_404(User, username=username)
    
    # for i in range(len(genre)):
    #     if genre[i]['id'] == id:
    #         if genre[i]['isprefer'] == True:
    #             genre[i]['isprefer'] = False
    #         else:
    #             genre[i]['isprefer'] = True
    
    print(pk)
    if id in profile_user.like_genres.all():
        profile_user.like_genres.remove(id)
        profile_user.save()
    else:
        profile_user.like_genres.add(id)
        profile_user.save()
    
    
    
    return redirect('accounts:profile', profile_user.username)

