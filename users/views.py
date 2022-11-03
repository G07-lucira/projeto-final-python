from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from users.models import User
from users.permissions import IsOwner, ListUsersValidation
from users.serializers import RegisterUserSerializer, UserDetailSerializer

class CreateUserView(generics.CreateAPIView, generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ ListUsersValidation]
    
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    
class ListDetailUSerView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ IsAuthenticated, IsOwner]

    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    lookup_field = "id"
