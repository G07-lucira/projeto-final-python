from rest_framework import generics

from users.models import User
from users.serializers import RegisterUserSerializer

class CreateUserView(generics.CreateAPIView, generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    
class ListUpdateUSerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    lookup_field = "id"

