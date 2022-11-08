from rest_framework import generics
from rest_framework.views import Response, status

from django.shortcuts import get_object_or_404

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import UserAnimes
from .serializers import UserAnimeSerializer, DetailedUserAnimeSerializer

from animes.models import Anime
from users.models import User

from utils.permissions import isAdminOrOwner


# Create your views here.
class UserAnimeView(generics.CreateAPIView):
    queryset = UserAnimes.objects.all()
    serializer_class = UserAnimeSerializer

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def create(self, request, *args, **kwargs):
        anime_id = self.kwargs["anime_id"]
        anime = get_object_or_404(Anime, pk=anime_id)
        user = request.user
        user.animes.add(anime, through_defaults=request.data)
        return Response(None, status.HTTP_201_CREATED)

class ListUserAnimeWatchlist(generics.ListAPIView):
    serializer_class = DetailedUserAnimeSerializer

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        user = self.request.user
        fav_list = UserAnimes.objects.filter(user=user)
        return fav_list

class UpdateDeleteUserAnime(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = UserAnimes.objects.all()
    serializer_class = DetailedUserAnimeSerializer

    permission_classes = [isAdminOrOwner]
    authentication_classes = [TokenAuthentication]
