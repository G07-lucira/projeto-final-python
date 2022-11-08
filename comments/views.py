import ipdb
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from django.shortcuts import get_object_or_404

from comments.models import Comment
from comments.serializers import CommentSerializer, CommentDetailSerializer

from utils.permissions import isAdminOrOwner

from episodes.models import Episode


class ListCreateCommentView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isAdminOrOwner]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    lookup_url_kwarg = "episode_id"

    def perform_create(self, serializer):
        # ipdb.set_trace()
        episode_id = self.kwargs["episode_id"]
        episode = get_object_or_404(Episode, pk=episode_id)
        self.check_object_permissions(self.request, episode)

        serializer.save(episode=episode, user=self.request.user)


class RetrieveUpdateDestroyCommentView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isAdminOrOwner]

    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer

    lookup_url_kwarg = "comment_id"
