from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Score
from .forms import MovieModelForm, ScoreModelForm

def home(request):
    movies = Movie.objects.order_by('-id')
    return render(request, 'movies/list.html', {
        'movies': movies
    })
    
def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    scores = movie.score_set.order_by('-id')
    return render(request, 'movies/detail.html', {
        'movie': movie,
        'scores': scores
    })
    
def create_movie(request):
    if request.method == 'POST':
        form = MovieModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:home')
    else:
        form = MovieModelForm()
        return render(request, 'movies/form.html', {
            'form': form,
            'header': '영화 추가',
            'lead': '영화 정보를 입력해 주세요.',
            'action': 'create_movie',
        })
    
def update_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = MovieModelForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            movie.save()
        return redirect('movies:movie_detail', movie.id)
    else:
        form = MovieModelForm(instance=movie)
        return render(request, 'movies/form.html', {
            'form': form,
            'header': '영화 수정',
            'lead': '수정할 정보를 입력해 주세요.',
            'action': 'update_movie',
        })
        
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return redirect('movies:home')
    
def create_score(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    score = Score(movie=movie)
    if request.method == 'POST':
        form = ScoreModelForm(request.POST, instance=score)
        if form.is_valid():
            form.save()
            return redirect('movies:movie_detail', movie.id)
    else:
        form = ScoreModelForm()
        return render(request, 'movies/score.html', {
            'form': form,
            'movie': movie,
        })