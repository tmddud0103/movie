# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    date_joined = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now_add=True)

    followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)
    # related_name : 역참조시 이름 바꿈

class User_genre(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ids = [
    {
        "id": 10770,
        "name": "TV 영화",
        "isprefer": False
    },
    {
        "id": 10752,
        "name": "전쟁",
        "isprefer": False
    },
    {
        "id": 10751,
        "name": "가족",
        "isprefer": False
    },
    {
        "id": 10749,
        "name": "로맨스",
        "isprefer": False
    },
    {
        "id": 10402,
        "name": "음악",
        "isprefer": False
    },
    {
        "id": 9648,
        "name": "미스터리",
        "isprefer": False
    },
    {
        "id": 878,
        "name": "SF",
        "isprefer": False
    },
    {
        "id": 99,
        "name": "다큐멘터리",
        "isprefer": False
    },
    {
        "id": 80,
        "name": "범죄",
        "isprefer": False
    },
    {
        "id": 53,
        "name": "스릴러",
        "isprefer": False
    },
    {
        "id": 37,
        "name": "서부",
        "isprefer": False
    },
    {
        "id": 36,
        "name": "역사",
        "isprefer": False
    },
    {
        "id": 35,
        "name": "코미디",
        "isprefer": False
    },
    {
        "id": 28,
        "name": "액션",
        "isprefer": False
    },
    {
        "id": 27,
        "name": "공포",
        "isprefer": False
    },
    {
        "id": 18,
        "name": "드라마",
        "isprefer": False
    },
    {
        "id": 16,
        "name": "애니메이션",
        "isprefer": False
    },
    {
        "id": 14,
        "name": "판타지",
        "isprefer": False
    },
    {
        "id": 12,
        "name": "모험",
        "isprefer": False
    },
    ]