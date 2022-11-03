from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from comments.models import Comment
from comments.serializers import CommentSerializer, CommentDetailSerializer

from .mixins import SerializerByMethodMixin


class CreateCommentView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Comment.objects.all()
    serializer_class = [CommentSerializer]
    lookup_url_kwarg = "episode_id"


class RetrieveUpdateDestroyCommentView(
    SerializerByMethodMixin,
    generics.RetrieveUpdateDestroyAPIVew,
):
    authentication_classes = [TokenAuthentication]
    queryset = Comment.objects.all()
    lookup_url_kwarg = "comment_id"
    serializer_map = {
        "GET": CommentDetailSerializer,
        "PATCH": CommentSerializer,
    }
