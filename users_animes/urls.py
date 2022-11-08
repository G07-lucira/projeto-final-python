from django.urls import path
from .views import UserAnimeView, ListUserAnimeWatchlist, UpdateDeleteUserAnime

urlpatterns=[
    path('watchlist/<str:anime_id>/fav/', UserAnimeView.as_view()),
    path('watchlist/', ListUserAnimeWatchlist.as_view()),
    path('watchlist/<pk>/', UpdateDeleteUserAnime.as_view()),
]