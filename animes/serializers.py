import ipdb
from genres.models import Genre
from genres.serializers import GenreSerializer
from rest_framework import serializers
from rest_framework.exceptions import APIException

from animes.models import Anime


class Error(APIException):
    status_code = 403


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = "__all__"
        ready_only_fields = ["episodes"]

    genres = GenreSerializer(many=True)
    # episodes = EpisodeSerializer(many=True)

    def create(self, validated_data: dict) -> Anime:
        if Anime.objects.filter(name=validated_data["name"]).exists():
            raise Error({"message": "Anime already exists"})

        genres = validated_data.pop("genres")
        new_anime = Anime.objects.create(**validated_data)

        for genre in genres:
            genre_instance, _ = Genre.objects.get_or_create(**genre)
            new_anime.genres.add(genre_instance)

        return new_anime
