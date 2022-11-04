from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from users_animes.serializers import UserAnimeSerializer

from model_bakery import baker

class UserAnimeTestViews(APITestCase):
    
    @classmethod
    def setUp(cls):
        cls.user = baker.make("users.User")
        cls.anime = baker.make("animes.Anime")
        cls.valid_data = {
            "last_watched": "2022-06-10",
	        "current_episode": 1,
	        "is_finished": False
        }
        cls.token = Token.objects.create(user=cls.user)

    def test_can_favorite_anime(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response_post = self.client.post(f"/api/animes/{self.anime.id}/fav/", self.valid_data, format="json")
        self.assertEqual(response_post.status_code, 204)
    
    def test_cannot_favorite_anime_without_auth(self):
        response_post = self.client.post(f"/api/animes/{self.anime.id}/fav/", self.valid_data, format="json")
        self.assertEqual(response_post.status_code, 401)
    
    def test_can_list_favorite_table(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response_get = self.client.get(f"/api/animes/{self.anime.id}/fav/")
        self.assertEqual(response_get.status_code, 200)