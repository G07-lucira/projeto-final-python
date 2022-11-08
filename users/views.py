from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from users.models import User
from users.permissions import isAdminOrOwner, ListUsersValidation
from users.serializers import RegisterUserSerializer, UserDetailSerializer


class CreateUserView(generics.CreateAPIView, generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ListUsersValidation]

    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer


class ListDetailUSerView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isAdminOrOwner]

    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    lookup_field = "id"
