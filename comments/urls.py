from django.urls import path

from .views import ListCreateCommentView, RetrieveUpdateDestroyCommentView

urlpatterns = [
    path("/episode/<str:episode_id>/comments/", ListCreateCommentView.as_view()),
    path("/comments/<str:comment_id>/", RetrieveUpdateDestroyCommentView.as_view()),
]
