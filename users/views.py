from rest_framework import generics

from users.models import User
from users.serializers import RegisterUserSerializer

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
