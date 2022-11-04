from rest_framework import serializers

from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment

        fields = [
            "id",
            "comment",
            "spoiler",
            "user",
            "episode",
        ]

        read_only_fields = [
            "id",
            "user",
            "episode",
        ]


class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment

        fields = [
            "id",
            "comment",
            "spoiler",
            "user",
            "episode",
        ]

        read_only_fields = [
            "id",
        ]
