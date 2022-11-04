from django.urls import path

from .views import AnimesDetailsView, AnimesView

urlpatterns = [
    # path("animes/createdb/", CreateDB.as_view()),
    path("animes/", AnimesView.as_view()),
    path("animes/<anime_id>/", AnimesDetailsView.as_view()),
]
