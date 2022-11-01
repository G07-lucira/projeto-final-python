from rest_framework import generics

from episodes.models import Episode
from episodes.serializers import EpisodeDetailSerializer, RegisterEpisodeSerializer

class CreateEpisodeView(generics.CreateAPIView):
    queryset = Episode.objects.all()
    serializer_class = RegisterEpisodeSerializer

    lookup_url_kwarg = 'anime_id'

class ListEpisodeDetailView(generics.RetrieveAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeDetailSerializer

