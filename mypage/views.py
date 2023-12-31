from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from board.models import Category, College, Major, Number, User, Challenge
from .forms import UserForm
from django.core.paginator import Paginator
from .models import LifeQuotes

# Create your views here.
# 회원 가입
def main(request):
    success_first_n = 0
    success_second_n = 0
    success_third_n = 0
    success_first = Major.objects.get(name='컴퓨터공학전공')
    success_second = Major.objects.get(name='소프트웨어전공')
    success_third = Major.objects.get(name='수학전공')
    for m in Major.objects.all():
        n = 0
        users = User.objects.filter(major=m)
        for u in users:
            challenges = Challenge.objects.filter(user=u).filter(status="1")
            n += challenges.count()
        if success_first_n < n:
            success_third_n = success_second_n
            success_third = success_second
            success_second_n = success_first_n
            success_second = success_first
            success_first_n = n
            success_first = m
        elif success_second_n < n:
            success_third_n = success_second_n
            success_third = success_second
            success_second_n = n
            success_second = m
        elif success_third_n < n:
            success_third_n = n
            success_third = m
    failure_first_n = 0
    failure_second_n = 0
    failure_third_n = 0
    failure_first = Major.objects.get(name='컴퓨터공학전공')
    failure_second = Major.objects.get(name='소프트웨어전공')
    failure_third = Major.objects.get(name='수학전공')
    for m in Major.objects.all():
        n = 0
        users = User.objects.filter(major=m)
        for u in users:
            challenges = Challenge.objects.filter(user=u).filter(status="2")
            n += challenges.count()
        if failure_first_n < n:
            failure_third_n = failure_second_n
            failure_third = failure_second
            failure_second_n = failure_first_n
            failure_second = failure_first
            failure_first_n = n
            failure_first = m
        elif failure_second_n < n:
            failure_third_n = failure_second_n
            failure_third = failure_second
            failure_second_n = n
            failure_second = m
        elif failure_third_n < n:
            failure_third_n = n
            failure_third = m
    return render(request, 'mypage/main.html', {
        'categories': Category.objects.all(),
        'success_first': success_first,
        'success_first_n': success_first_n,
        'success_second': success_second,
        'success_second_n': success_second_n,
        'success_third': success_third,
        'success_third_n': success_third_n,
        'failure_first': failure_first,
        'failure_first_n': failure_first_n,
        'failure_second': failure_second,
        'failure_second_n': failure_second_n,
        'failure_third': failure_third,
        'failure_third_n': failure_third_n,
    })

def user_signup(request):
    Major.objects.all().order_by('name')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if request.POST['password'] == request.POST['confirm']:
            if form.is_valid():
                user = form.save(commit=False)
                user.password = request.POST['password']
                number = request.POST.get('number')
                user.number = Number.objects.get(number=number)
                college = request.POST.get('college')
                user.college = College.objects.get(name=college)
                if request.POST.get('major'):
                    major = request.POST.get('major')
                    user.major = Major.objects.get(name=major)
                user.save()
                login(request, user)
                return redirect("user:main")
    else:
        form = UserForm()
    return render(request, 'mypage/signup.html', {
        'form': form,
        'categories': Category.objects.all(),
        'colleges': College.objects.all(),
        'majors': Major.objects.all().order_by('name'),
        'numbers': Number.objects.all().order_by('-number')
    })

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.get(username=username)
        if user.password == password:
            login(request, user)
            print("인증성공")
            return redirect("user:main")  # 로그인 후 이동할 페이지 설정
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
    challenge_keep_list = Challenge.objects.filter(user=user).filter(status="0").order_by('-pk')
    challenge_success_list = Challenge.objects.filter(user=user).filter(status="1").order_by('-pk')
    challenge_failure_list = Challenge.objects.filter(user=user).filter(status="2").order_by('-pk')
    random_quote = LifeQuotes.objects.order_by('?').first()

    page = request.GET.get("page", "1")
    paginator_keep = Paginator(challenge_keep_list, 5)
    paginator_success = Paginator(challenge_success_list, 5)
    paginator_failure = Paginator(challenge_failure_list, 5)
    page_keep = paginator_keep.get_page(page)
    page_success = paginator_success.get_page(page)
    page_failure = paginator_failure.get_page(page)


    return render(request, 'mypage/my_detail.html', {
        'challenge_keep_list': page_keep,
        'challenge_success_list': page_success,
        'challenge_failure_list': page_failure,
        'user':user,
        'categories': Category.objects.all(),
        'life_quotes': random_quote
    })
