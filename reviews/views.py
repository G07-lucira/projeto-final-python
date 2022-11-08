from django.forms import model_to_dict
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView, Request, Response, status

from animes.models import Anime
import ipdb
from .models import Review
from .permissions import CustomIdReviewPermission, CustomReviewPermission
from .serializers import ReviewSerializer


class ReviewView(APIView):
    authentication_classes = [TokenAuthentication]
    permissions_classes = [CustomReviewPermission]

    def post(self, request: Request, anime_id: int) -> Response:
        anime = get_object_or_404(Anime, pk=anime_id)
        # ipdb.set_trace()
        review_exist = Review.objects.filter(anime=anime, user=request.user).exists()
        if review_exist:
            return Response(
                {"detail": "Review already exists."}, status.HTTP_403_FORBIDDEN
            )
        serializer = ReviewSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save(anime=anime, user=request.user)
        return Response(serializer.data, status.HTTP_201_CREATED)


class ReviewIdView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CustomIdReviewPermission]

    def get(self, request: Request, review_id: str) -> Response:
        review = get_object_or_404(Review, id=review_id)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def delete(self, request: Request, review_id: str) -> Response:
        review = get_object_or_404(Review, id=review_id)
        self.check_object_permissions(request, review.user)
        review.delete()
        return Response({}, status.HTTP_204_NO_CONTENT)

    def patch(self, request: Request, review_id: str) -> Response:

        try:
            review = get_object_or_404(Review, id=review_id)
            self.check_object_permissions(request, review.user)
        except Review.DoesNotExist:
            return Response({"error": "Review not found"}, status.HTTP_404_NOT_FOUND)

        for key, value in request.data.items():
            setattr(review, key, value)

        review.save()

        review_dict = model_to_dict(review)

        return Response(review_dict, status.HTTP_200_OK)
