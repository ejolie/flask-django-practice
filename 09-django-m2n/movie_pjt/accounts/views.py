from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST

from .forms import UserCustomCreationForm
from .models import User, User_Followers_User

# Create your views here.
@require_http_methods(["GET", "POST"])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method == 'POST':
        user_form = UserCustomCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            auth_login(request, user)
            return redirect('movies:list')
    else:
        user_form = UserCustomCreationForm()
    return render(request, 'accounts/forms.html', {
        'form': user_form,
    })

def login(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect('movies:list')
    else:
        login_form = AuthenticationForm()
    return render(request, 'accounts/forms.html', {
        'form': login_form,
    })

@login_required
def logout(request):
    auth_logout(request)
    return redirect('movies:list')

def list(request):
    users = User.objects.all()
    return render(request, 'accounts/list.html',{
        'users': users
    })

# 유저 상세보기
def profile(request, user_pk):
    user = User.objects.get(pk=user_pk)
    followings = []
    followers = []
    return render(request, 'accounts/profile.html', {
        'user': user,
        'followers': followers,
        'followings': followings,
    })

# 유저 팔로워 목록 출력
def followers(request, user_pk):
    pass

# 유저 팔로잉 목록 출력
def followings(request, user_pk):
    pass