from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Movie, Score
from .forms import ScoreForm

# 영화 목록
def list(request):
    movies = Movie.objects.order_by('-id')
    return render(request, 'movies/list.html', {
        'movies': movies,
    })

# 영화 상세보기
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    score_form = ScoreForm()
    return render(request, 'movies/detail.html', {
        'movie': movie,
        'score_form': score_form,
    })

# 평점 생성하기
@login_required
@require_POST
def create_score(request, movie_pk):
    score_form = ScoreForm(request.POST)
    if score_form.is_valid():
        score = score_form.save(commit=False)
        score.user = request.user
        score.movie_id = movie_pk
        score.save()
    return redirect('movies:detail', movie_pk)

# 평점 삭제하기
@login_required
@require_POST
def delete_score(request, movie_pk, score_pk):
    score = get_object_or_404(Score, pk=score_pk)
    if score.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this Comment")
    score.delete()
    return redirect('movies:detail', movie_pk)