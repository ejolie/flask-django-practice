from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('new/', views.create_movie, name='create_movie'),
    path('<int:movie_id>/edit/', views.update_movie, name='update_movie'),
    path('<int:movie_id>/delete/', views.delete_movie, name='delete_movie'),
    path('<int:movie_id>/scores/new', views.create_score, name='create_score'),
]