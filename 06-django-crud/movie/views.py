from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def home(request):
    return render(request, 'movie/base.html')
    
def index(request):
    movies = Movie.objects.all()
    return render(request, 'movie/index.html', {'movies':movies})
    
def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movie/detail.html', {'movie':movie})
    
def edit(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movie/edit.html', {'movie':movie})
    
def delete(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.delete()
    return redirect('index')