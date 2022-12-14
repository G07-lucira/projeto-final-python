from rest_framework import serializers

from django.shortcuts import get_object_or_404

from .models import UserAnimes
from animes.models import Anime

from users.serializers import RegisterUserSerializer
from animes.serializers import AnimeSerializer


class UserAnimeSerializer(serializers.ModelSerializer):
    user = RegisterUserSerializer()
    anime = AnimeSerializer()

    class Meta:
        model = UserAnimes
        fields = ["last_watched","current_episode","is_finished", "user", "anime"]
        read_only_fields = ["user", "anime", "last_watched"]

class DetailedUserAnimeSerializer(serializers.ModelSerializer):
    # anime = AnimeSerializer()
    class Meta:
        model = UserAnimes
        fields = ["id", "anime", "last_watched", "current_episode","is_finished"]
        read_only_fields = ["anime", "last_watched"]