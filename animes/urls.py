from django.urls import path

from .views import AnimesView, CreateDB

urlpatterns = [
    path("animes/createdb/", CreateDB.as_view()),
    path("animes/", AnimesView.as_view()),
]
