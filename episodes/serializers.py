from rest_framework import serializers

from episodes.models import Episode

class RegisterEpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode

        fields = [
            "id",
            "name",
            "number",
            "duration",
            "anime_id"
        ]

        read_only_fields=[
            "id"
        ]

class EpisodeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode

        fields = [
            "id",
            "name",
            "number",
            "duration",
        ]

        read_only_fields=[
            "id"
        ]