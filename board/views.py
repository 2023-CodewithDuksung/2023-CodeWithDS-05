from django.shortcuts import render, redirect
from .models import Category, College, Major, Number, User, Challenge
from django.views.generic import DetailView
from .forms import ChallengeForm
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from datetime import date
from django.core.paginator import Paginator

# Create your views here.
def challenge_new(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChallengeForm(request.POST)
            if form.is_valid():
                challenge = form.save(commit=False)
                challenge.title = request.POST.get('title')
                if request.POST.get('memo'):
                    challenge.memo = request.POST.get('memo')
                else:
                    challenge.memo = ""
                challenge.user = request.user
                challenge.save()
                return redirect(challenge.get_absolute_url())
        else:
            form = ChallengeForm()
        return render(request, 'board/challenge_new.html', {
            'form':form,
            'categories': Category.objects.all(),
        })
    else:
        raise PermissionDenied


def challenge_update(request, pk):
    if request.user.is_authenticated:
        challenge = get_object_or_404(Challenge, pk=pk)
        if(request.user == challenge.user):
            if request.method == 'POST':
                form = ChallengeForm(request.POST, instance=challenge)
                if form.is_valid():
                    challenge = form.save(commit=False)
                    challenge.user = request.user
                    challenge.title = request.POST.get('title')
                    if request.POST.get('memo'):
                        challenge.memo = request.POST.get('memo')
                    else:
                        challenge.memo = ""
                    if request.POST.get('action') == 'progress':
                        challenge.status = "0"
                    elif request.POST.get('action') == 'success':
                        challenge.status = "1"
                        challenge.end_date = date.today()
                    elif request.POST.get('action') == 'failure':
                        challenge.status = "2"
                        challenge.end_date = date.today()
                    challenge.save()
                    return redirect(challenge.get_absolute_url())
            else:
                form = ChallengeForm(instance=challenge)
            return render(request, 'board/challenge_update.html', {
                'form':form,
                'challenge':Challenge.objects.get(pk=pk),
                'categories': Category.objects.all(),
            })
    else:
        raise PermissionDenied

class ChallengeDetail(LoginRequiredMixin, DetailView):
    model = Challenge

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super(ChallengeDetail, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def get_context_data(self, **kwargs):
        context = super(ChallengeDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['colleges'] = College.objects.all()
        context['majors'] = Major.objects.all()
        return context

def like(request, pk):
    challenge = Challenge.objects.get(pk=pk)
    if (challenge.like_users.filter(pk=request.user.pk)):
        challenge.like_users.remove(request.user)
    else:
        challenge.like_users.add(request.user)
    return redirect(challenge.get_absolute_url())

def challenge_list(request, slug_category):
    category = Category.objects.get(slug=slug_category)
    challenge_keep_list = Challenge.objects.filter(category=category).filter(status="0").order_by('-start_date')
    challenge_success_list = Challenge.objects.filter(category=category).filter(status="1").order_by('-start_date')

    page = request.GET.get("page", "1")
    paginator_keep = Paginator(challenge_keep_list, 10)
    paginator_success = Paginator(challenge_success_list, 10)
    page_keep = paginator_keep.get_page(page)
    page_success = paginator_success.get_page(page)

    return render(request, 'board/challenge_list.html', {
        'challenge_keep_list': page_keep,
        'challenge_success_list': page_success,
        'categories': Category.objects.all(),
        'colleges': College.objects.all(),
        'majors': Major.objects.all().order_by('name'),
        'numbers': Number.objects.all().order_by('number')
    })

def challenge_number_list(request, slug_category, number):
    category = Category.objects.get(slug=slug_category)
    number = Number.objects.get(number=number)
    users = User.objects.exclude(number=number)
    challenge_keep_list = Challenge.objects.filter(category=category).filter(status="0").order_by('-start_date')
    challenge_success_list = Challenge.objects.filter(category=category).filter(status="1").order_by('-start_date')
    for u in users:
        challenge_keep_list = challenge_keep_list.exclude(user=u)
        challenge_success_list = challenge_success_list.exclude(user=u)

    page = request.GET.get("page", "1")
    paginator_keep = Paginator(challenge_keep_list, 10)
    paginator_success = Paginator(challenge_success_list, 10)
    page_keep = paginator_keep.get_page(page)
    page_success = paginator_success.get_page(page)

    return render(request, 'board/challenge_number_list.html', {
        'challenge_keep_list': page_keep,
        'challenge_success_list': page_success,
        'categories': Category.objects.all(),
        'colleges': College.objects.all(),
        'majors': Major.objects.all().order_by('name'),
        'numbers': Number.objects.all().order_by('number'),
        'number_now': number
    })

def challenge_major_list(request, slug_category, slug_major):
    category = Category.objects.get(slug=slug_category)
    college = College.objects.filter(slug=slug_major)
    if college:
        college = College.objects.get(slug=slug_major)
        users = User.objects.exclude(college=college)
    else:
        major = Major.objects.get(slug=slug_major)
        users = User.objects.exclude(major=major)
    challenge_keep_list = Challenge.objects.filter(category=category).filter(status="0").order_by('-start_date')
    challenge_success_list = Challenge.objects.filter(category=category).filter(status="1").order_by('-start_date')
    for u in users:
        challenge_keep_list = challenge_keep_list.exclude(user=u)
        challenge_success_list = challenge_success_list.exclude(user=u)

    page = request.GET.get("page", "1")
    paginator_keep = Paginator(challenge_keep_list, 10)
    paginator_success = Paginator(challenge_success_list, 10)
    page_keep = paginator_keep.get_page(page)
    page_success = paginator_success.get_page(page)

    return render(request, 'board/challenge_major_list.html', {
        'challenge_keep_list': page_keep,
        'challenge_success_list': page_success,
        'categories': Category.objects.all(),
        'colleges': College.objects.all(),
        'majors': Major.objects.all().order_by('name'),
        'numbers': Number.objects.all().order_by('number')
    })

def challenge_major_number_list(request, slug_category, slug_major, number):
    category = Category.objects.get(slug=slug_category)
    college = College.objects.filter(slug=slug_major)
    if college:
        college = College.objects.get(slug=slug_major)
        users = User.objects.exclude(college=college)
    else:
        major = Major.objects.get(slug=slug_major)
        users = User.objects.exclude(major=major)
    challenge_keep_list = Challenge.objects.filter(category=category).filter(status="0").order_by('-start_date')
    challenge_success_list = Challenge.objects.filter(category=category).filter(status="1").order_by('-start_date')
    for u in users:
        challenge_keep_list = challenge_keep_list.exclude(user=u)
        challenge_success_list = challenge_success_list.exclude(user=u)

    number = Number.objects.get(number=number)
    users = User.objects.exclude(number=number)
    for u in users:
        challenge_keep_list = challenge_keep_list.exclude(user=u)
        challenge_success_list = challenge_success_list.exclude(user=u)

    page = request.GET.get("page", "1")
    paginator_keep = Paginator(challenge_keep_list, 10)
    paginator_success = Paginator(challenge_success_list, 10)
    page_keep = paginator_keep.get_page(page)
    page_success = paginator_success.get_page(page)

    return render(request, 'board/challenge_major_number_list.html', {
        'challenge_keep_list': page_keep,
        'challenge_success_list': page_success,
        'categories': Category.objects.all(),
        'colleges': College.objects.all(),
        'majors': Major.objects.all().order_by('name'),
        'numbers': Number.objects.all().order_by('number'),
        'number_now': number
    })