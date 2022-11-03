from rest_framework import serializers
from rest_framework.exceptions import APIException
import ipdb

from episodes.models import Episode
from animes.models import Anime
from comments.serializers import CommentSerializer

from django.shortcuts import get_object_or_404


class Error(APIException):
    status_code = 403

class RegisterEpisodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Episode

        fields = [
            "id",
            "name",
            "epi_number",
            "duration",
            "anime_id"
        ]

        read_only_fields=[
            "id",
            "anime_id"
        ]
  

class EpisodeDetailSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True)

    class Meta:
        model = Episode

        fields = [
            "id",
            "name",
            "epi_number",
            "duration",
            "comments"
        ]

        read_only_fields=[
            "id",
            "comments"
        ]