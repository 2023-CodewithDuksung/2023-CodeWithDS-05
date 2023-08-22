from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from board.models import Category, College, Major, Number, User, Challenge
from .forms import UserForm
from django.core.paginator import Paginator

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
def user_detail(request, username):
    user = User.objects.get(username=username)
    challenge_keep_list = Challenge.objects.filter(user=user).filter(status="0")
    challenge_success_list = Challenge.objects.filter(user=user).filter(status="1")
    challenge_failure_list = Challenge.objects.filter(user=user).filter(status="2")

    page = request.GET.get("page", "1")
    paginator_keep = Paginator(challenge_keep_list, 10)
    paginator_success = Paginator(challenge_success_list, 10)
    paginator_failure = Paginator(challenge_failure_list, 10)
    page_keep = paginator_keep.get_page(page)
    page_success = paginator_success.get_page(page)
    page_failure = paginator_failure.get_page(page)


    return render(request, 'mypage/my_detail.html', {
        'challenge_keep_list': page_keep,
        'challenge_success_list': page_success,
        'challenge_failure_list': page_failure,
        'user':user,
        'categories': Category.objects.all()
    })
