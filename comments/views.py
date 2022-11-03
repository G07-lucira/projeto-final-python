from rest_framework import generics

from comments.models import Comment
from comments.serializers import CommentSerializer


class CreateCommentView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer