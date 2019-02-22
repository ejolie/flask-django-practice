''' movie/urls.py '''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>/', views.detail, name='detail'),
    path('<int:movie_id>/delete', views.delete, name='delete'),
    path('<int:movie_id>/edit', views.edit, name='edit'),
]