from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def mypage(request):
    return render(request, 'mypage.html')
    
def qna(request):
    return render(request, 'qna.html')
    
def signup(request):
    return render(request, 'signup.html')
    
def not_found(request, not_found):
    context = { 'path': not_found }
    return render(request, '404.html', context)