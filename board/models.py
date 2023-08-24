from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/board/{self.slug}'

    class Meta:
        verbose_name_plural = 'Categories'

class College(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

class Major(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Number(models.Model):
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.number

class User(AbstractUser):
    number = models.ForeignKey(Number, on_delete=models.SET_NULL, null=True)
    college = models.ForeignKey(College, on_delete=models.SET_NULL, null=True)
    major = models.ForeignKey(Major, on_delete=models.SET_NULL, null=True, blank=True)

class Challenge(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(null=True, blank=True)
    start_date = models.DateField()#auto_now_add=True
    end_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    STATUS_CHOICES = (("0", "진행중"), ("1", "성공"), ("2", "실패"))
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default=0)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    like_users = models.ManyToManyField(User, blank=True, related_name='like_challenge')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f'/board/{self.pk}/'

    def get_day(self):
        if (self.status=="0"):
            day = date.today()-self.start_date
        else:
            day = self.end_date-self.start_date
        return day.days

    def get_user_name(self):
        if self.user.major:
            return f'{self.user.major} {self.user.number}'
        else:
            return f'{self.user.college} {self.user.number}'