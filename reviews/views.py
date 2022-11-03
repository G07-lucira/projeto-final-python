from django.shortcuts import get_object_or_404

from rest_framework.views import APIView, Request, Response, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination

from .models import Review
from animes.models import Anime
from .serializers import ReviewSerializer
from .permissions import CustomReviewPermission, CustomIdReviewPermission
import ipdb

class ReviewView(APIView):
    authentication_classes = [TokenAuthentication]
    permissions_classes = [CustomReviewPermission]

    def post(self, request: Request, anime_id: int) -> Response:
        anime = get_object_or_404(Anime, pk=anime_id)
        ipdb.set_trace()
        review_exist = Review.objects.filter(
            anime=anime, user=request.user).exists()
        if review_exist:
            return Response({"detail": "Review already exists."}, status.HTTP_403_FORBIDDEN)
        serializer = ReviewSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save(anime=anime, user=request.user)
        return Response(serializer.data, status.HTTP_201_CREATED)


    def get(self, request: Request, anime_id: int) -> Response:
        reviews = Review.objects.filter(anime_id=anime_id)
        if not reviews:
            return Response({"detail": "Not found."}, status.HTTP_404_NOT_FOUND)

        result_page = self.paginate_queryset(reviews, request, view=self)

        serializer = ReviewSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

class ReviewIdView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CustomReviewPermission, CustomIdReviewPermission]

    def get(self, request: Request, anime_id: int, review_id: int) -> Response:
        review = get_object_or_404(Review, id=review_id, anime_id=anime_id)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    def delete(self, request: Request, anime_id: int, review_id: int) -> Response:
        review = get_object_or_404(Review, id=review_id, anime_id=anime_id)
        self.check_object_permissions(request, review.critic)
        review.delete()
        return Response({}, status.HTTP_204_NO_CONTENT)