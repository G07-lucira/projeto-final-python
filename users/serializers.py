from rest_framework import serializers

from users.models import User

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = [
            "id",
            "email",
            "password",
            "username"
        ]

        read_only_fields=[
            "id"
        ]

        extra_kwargs={
            "password":{"write_only": True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)