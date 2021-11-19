from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/comment/create/', views.comments_create, name='comments_create'),
    path('onair/', views.onair, name='onair'),
    path('recommend/', views.recommend, name="recommend"),
]
