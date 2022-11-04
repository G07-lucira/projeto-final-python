from django.test import TestCase

from model_bakery import baker
from users.models import User

class UserTestModel(TestCase):
    @classmethod
    def setUp(self):
        self.user_data = {
            "email":"raony.teste@gmail.com",
            "password":"teste1",
            "username":"raony",
            "bio":"eu gosto de bolo",
            "birthday":"2003-06-02"
        }
        self.user = User.objects.create(**self.user_data)

    def test_username_max_length(self):
        max_length = self.user._meta.get_field('username').max_length

        self.assertEqual(max_length, 150)

    def test_birthday_can_be_null(self):
        nullable = self.user._meta.get_field("birthday").null

        self.assertTrue(nullable)