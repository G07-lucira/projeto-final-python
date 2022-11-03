from django.urls import path
from . import views

urlpatterns=[
    path("reviews/<str:anime_id>/",views.ReviewView.as_view()),
    path("reviews/<str:anime_id>/<str:review_id>", views.ReviewIdView.as_view())
]