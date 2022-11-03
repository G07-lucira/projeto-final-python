from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from users_animes.serializers import UserAnimeSerializer

from model_bakery import baker

import ipdb

class UserAnimeTestModels(APITestCase):
    
    @classmethod
    def setUp(cls):
        cls.favorited = baker.make("users_animes.UserAnimes", make_m2m=True)

    def test_verify_many_to_many_relation(self):
        self.assertTrue(self.favorited)
