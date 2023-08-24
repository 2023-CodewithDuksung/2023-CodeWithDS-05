from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.ChallengeDetail.as_view()),
    path('<str:slug_category>/', views.challenge_list),
    path('<str:slug_category>/number/<str:number>/', views.challenge_number_list),
    path('<str:slug_category>/major/<str:slug_major>/', views.challenge_major_list),
    path('<str:slug_category>/major/<str:slug_major>/number/<str:number>/', views.challenge_major_number_list),
    path('challenge/new/', views.challenge_new, name='challenge_new'),
    path('<int:pk>/update/', views.challenge_update, name='challenge_update'),
    path('<int:pk>/like/', views.like),
    path('<int:pk>/success/', views.success),
]