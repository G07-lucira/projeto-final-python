from django.test import TestCase

from model_bakery import baker

from users.serializers import UserDetailSerializer
from users.models import User

class UserTestModel(TestCase):
    @classmethod
    def setUp(self):
        self.user_joe = baker.make(
            User,
            email="raony.teste@gmail.com",
            password="teste1",
            username="raony",
            bio="eu estou perdido",
            birthday="2003-06-02",
        )

    def test_create_user(self):
        self.user_one = self.user_joe
        serializer = UserDetailSerializer(self.user_one)
        self.assertIsInstance(self.user_one, User)
        self.assertEqual(serializer.data["username"], "raony")
        self.assertEqual(serializer.data["bio"], "eu estou perdido")
        self.assertEqual(serializer.data["birthday"], "2003-06-02")
