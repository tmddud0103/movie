from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/comment/create/', views.comments_create, name='comments_create'),
    path('onair/', views.onair, name='onair'),
    path('recommend/', views.recommend, name="recommend"),
    path('choose/', views.choose, name="choose"),
    path('likechoose/<username>/<int:id>/', views.like_choose, name="like_choose"),
    # path('choose/<username>/<int:pk>/<int:id>/', views.choose, name='choose'),
]
