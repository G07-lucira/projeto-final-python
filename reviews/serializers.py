from rest_framework import serializers


from reviews.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review

        fields = [
            "id",
            "title",
            "description",
            "recommended",
            "anime",
            "user"
        ] 

        read_only_fields = ["id"]

     def create(self, validated_data):
        return Review.objects.create(validated_data)