from django.urls import path

from .views import CreateListEpisodeView, RetrieveUpdateDestroyEpisodeDetailView

urlpatterns=[
    path('animes/<str:anime_id>/episode/', CreateListEpisodeView.as_view()),
    path('episode/<str:episode_id>/', RetrieveUpdateDestroyEpisodeDetailView.as_view()),
]