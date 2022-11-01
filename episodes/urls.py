from django.urls import path

from episodes.views import CreateEpisodeView

urlpatterns=[
    path('animes/<int:anime_id>/episode/', CreateEpisodeView.as_view()),
]