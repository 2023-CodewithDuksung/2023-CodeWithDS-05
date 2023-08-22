from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from board.models import Category, College, Major, Number, User, Challenge
from .forms import UserForm

# Create your views here.
# 회원 가입
def main(request):
    return render(request, 'mypage/main.html', {
        'categories': Category.objects.all()
    })

def user_signup(request):
    Major.objects.all().order_by('name')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if request.POST['password'] == request.POST['confirm']:
            if form.is_valid():
                user = form.save(commit=False)
                user.password = request.POST['password']
                user.save()
                login(request, user)
                return redirect("user:main")
    else:
        form = UserForm()
    return render(request, 'mypage/signup.html', {
        'form': form,
        'categories': Category.objects.all()
    })

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.get(username=username)
        if user.password == password:
            login(request, user)
            print("인증성공")
            return redirect('user:main')  # 로그인 후 이동할 페이지 설정
        else:
            print("인증실패")
            return render(request, 'mypage/login.html', {'error': 'username or password is incorrect.'})
    return render(request, 'mypage/login.html', {
        'categories': Category.objects.all()
    })

#로그아웃
def user_logout(request):
    logout(request)
    return redirect("user:login")

#진행중
def keep(request):
    return render(request, '')

#성공
def success(request):
    return render(request,'')

#실패
def fail(request):
    return render(request,'')