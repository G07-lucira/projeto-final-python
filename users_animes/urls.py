from django.urls import path
from .views import UserAnimeView

urlpatterns=[
    path('animes/<str:anime_id>/fav/', UserAnimeView.as_view()),
]