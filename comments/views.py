import ipdb
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from comments.models import Comment
from comments.serializers import CommentDetailSerializer, CommentSerializer
from episodes.models import Episode
from utils.permissions import isAdminOrOwner

from .permissions import CustomIdCommentsPermission


class ListCreateCommentView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isAdminOrOwner]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    lookup_url_kwarg = "episode_id"

    def perform_create(self, serializer):

        episode_id = self.kwargs["episode_id"]
        episode = get_object_or_404(Episode, pk=episode_id)

        serializer.save(episode=episode, user=self.request.user)


class RetrieveUpdateDestroyCommentView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CustomIdCommentsPermission]

    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer

    lookup_url_kwarg = "comment_id"
