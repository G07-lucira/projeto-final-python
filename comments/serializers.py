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

        read_only_fields = ["id"]

    def create(self, validated_data):
        return Comment.create(validated_data)
