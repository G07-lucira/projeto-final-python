from rest_framework import generics
from rest_framework.views import Response, status

from django.shortcuts import get_object_or_404

from rest_framework.authentication import TokenAuthentication

from .models import UserAnimes
from .serializers import UserAnimeSerializer

from animes.models import Anime

import ipdb

# Create your views here.
class UserAnimeView(generics.ListCreateAPIView):
    queryset = UserAnimes.objects.all()
    serializer_class = UserAnimeSerializer
    authentication_classes = [TokenAuthentication]

    #ACESSAR ANIME PELO ID USANDO GET 404
    #ACESSAR USUARIO PELO ID USANDO GET 404
    #CRIAR O OBJETO PELO SERIALIZER
    #DAR UM SAVE ASSOCIANDO ANIME E USER
    #USER.ANIMES.ADD(ANIME, through_defaults={"EXTRAS"})

    def create(self, request, *args, **kwargs):
        anime_id = self.kwargs["anime_id"]
        anime = get_object_or_404(Anime, pk=anime_id)
        user = request.user
        user.animes.add(anime, through_defaults=request.data)
        return Response(status.HTTP_200_OK)
