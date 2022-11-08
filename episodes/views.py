from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
import ipdb

from .permissions import CustomIsAuthenticated

from .models import Episode
from .serializers import EpisodeDetailSerializer, RegisterEpisodeSerializer

from animes.models import Anime
from django.shortcuts import get_object_or_404

class CreateListEpisodeView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ CustomIsAuthenticated ]

    queryset = Episode.objects.all()
    serializer_class = RegisterEpisodeSerializer

    lookup_url_kwarg = 'anime_id'

    def perform_create(self, serializer):
        anime_id = self.kwargs['anime_id']

        anime = get_object_or_404(Anime, pk=anime_id)
        self.check_object_permissions(self.request, anime)
        serializer.save(anime=anime)


class RetrieveUpdateDestroyEpisodeDetailView(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [ CustomIsAuthenticated ]

    queryset = Episode.objects.all()
    serializer_class = EpisodeDetailSerializer

    lookup_url_kwarg = 'episode_id'
