from django.urls import path

from .views import CreateCommentView, RetrieveUpdateDestroyCommentView

urlpatterns = [
    path("/episode/<str:episode_id>/comments/", CreateCommentView.as_view()),
    path("/comments/<str:comment_id>/", RetrieveUpdateDestroyCommentView.as_view()),
]
