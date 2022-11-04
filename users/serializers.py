from rest_framework import serializers

from users.models import User

from animes.serializers import AnimeSerializer

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = [
            "id",
            "email",
            "password",
            "username",
            "bio",
            "birthday"
        ]

        read_only_fields=[
            "id"
        ]

        extra_kwargs={
            "bio":{"write_only": True},
            "password":{"write_only": True},
            "birthday":{"write_only": True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserDetailSerializer(serializers.ModelSerializer):
    animes = AnimeSerializer(many=True)
    class Meta:
        model = User

        fields = [ "username","date_joined","bio","birthday","animes" ]
