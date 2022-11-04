from django.test import TestCase

from model_bakery import baker
from users.models import User

class UserTestModel(TestCase):
    @classmethod
    def setUp(self):
        self.user_joe = baker.make("users.User")
        self.anime_x = baker.make("animes.Anime")
        self.episode_y = baker.make("episodes.Episode")
        self.comment_z= baker.make("comments.Comment")

    def test_create_user(self):
        user_one = self.user_joe
        self.assertIsInstance(user_one, User)