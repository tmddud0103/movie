from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    # path('choose/<username>/<int:pk>/<int:id>/', views.choose, name='choose'),
]