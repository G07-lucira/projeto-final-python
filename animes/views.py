from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from utils.permissions import isAdminOrOwner

from animes.models import Anime
from animes.serializers import AnimeDetailsSerializer, AnimeSerializer

# Create your views here.
# class CreateDB(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [isAdmin]

#     # headers
#     def get(self, request, *args, **kwargs):

#         # call another api for GET
#         url = "https://gogoanime.consumet.org/top-airing"
#         api_call = requests.get(url, headers={})
#         api_json = api_call.json()

#         anime_db = []

#         for anime in api_json:
#             anime_id = anime.pop("animeId")
#             url = f"https://gogoanime.consumet.org/anime-details/{anime_id}"
#             anime = requests.get(url, headers={})
#             anime_db.append(anime.json())
#         for anime in anime_db:
#             genres = anime.pop("genres")

#             new_anime = {
#                 "name": anime["animeTitle"],
#                 "total_eps": anime["totalEpisodes"],
#                 "release_date": anime["releasedDate"],
#                 "animeImg": anime["animeImg"],
#                 "synopsis": anime["synopsis"],
#                 "current_status": anime["status"],
#             }

#             ipdb.set_trace()
#             anime_instance = Anime.objects.create(**new_anime)

#             for genre in genres:
#                 genre_instance, _ = Genre.objects.get_or_create(name=genre)
#                 anime_instance.genres.add(genre_instance)

#         anime_list = Anime.objects.all()
#         return Response(anime_list)


class AnimesView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isAdminOrOwner]

    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer


class AnimesDetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isAdminOrOwner]
    
    queryset = Anime.objects
    serializer_class = AnimeDetailsSerializer

    lookup_url_kwarg = "anime_id"
