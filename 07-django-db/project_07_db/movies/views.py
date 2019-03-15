from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Score

'''
model Movie
'''


def movie_list(request):
    movies = Movie.objects.order_by('-id')
    return render(request, 'movies/list.html', {
        'movies': movies,
    })


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    scores = movie.score_set.order_by('-id')
    colors = [
        'red',
        'orange',
        'yellow',
        'olive',
        'green',
        'teal',
        'blue',
        'violet',
        'purple',
        'pink',
        'brown'
    ]
    color = colors[movie.genre.id-1]
    return render(request, 'movies/detail.html', {
        'movie': movie,
        'scores': scores,
        'color': color,
    })


def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:movie_list')
    else:
        return redirect('movies:movie_detail', movie_id)


'''
model Score
'''
def create_score(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        score = Score.objects.create(
            content=request.POST.get('content'),
            score=int(request.POST.get('ratingNum')),
            movie_id=movie_id
        )
        score.movie_id = movie.id
    return redirect('movies:movie_detail', movie.id)


def delete_score(request, movie_id, score_id):
    movie = get_object_or_404(Movie, id=movie_id)
    score = get_object_or_404(Score, id=score_id)
    if request.method == 'POST':
        score.delete()
    return redirect('movies:movie_detail', movie.id)
