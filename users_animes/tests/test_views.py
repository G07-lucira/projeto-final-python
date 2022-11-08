from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from users_animes.serializers import UserAnimeSerializer

import ipdb

from model_bakery import baker

class UserAnimeTestViews(APITestCase):
    
    @classmethod
    def setUp(cls):
        cls.user = baker.make("users.User")
        cls.user2 = baker.make("users.User")
        cls.anime = baker.make("animes.Anime")
        cls.anime2 = baker.make("animes.Anime")
        cls.fav = baker.make("users_animes.UserAnimes", is_finished=False, user=cls.user, anime=cls.anime2)
        cls.valid_data = {
	        "current_episode": 1,
	        "is_finished": False
        }
        cls.token = Token.objects.create(user=cls.user)
        cls.invalid_token = Token.objects.create(user=cls.user2)

    def test_can_favorite_anime(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response_post = self.client.post(f"/api/watchlist/{self.anime.id}/fav/", self.valid_data, format="json")
        self.assertEqual(response_post.status_code, 201)
    
    def test_cannot_favorite_anime_without_auth(self):
        response_post = self.client.post(f"/api/watchlist/{self.anime.id}/fav/", self.valid_data, format="json")
        self.assertEqual(response_post.status_code, 401)

    def test_can_update_favorite_anime(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response_patch = self.client.patch(f"/api/watchlist/{self.fav.id}/", {"is_finished": True}, format="json")
        self.assertFalse(self.fav.is_finished)
        self.assertEqual(response_patch.status_code, 200)
        self.assertTrue(response_patch.data["is_finished"])

    def test_can_remove_favorite(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response_delete = self.client.delete(f"/api/watchlist/{self.fav.id}/")
        self.assertEqual(response_delete.status_code, 204)
    
    def test_cannot_update_another_user_fav(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.invalid_token.key)
        response_patch = self.client.patch(f"/api/watchlist/{self.fav.id}/", {"is_finished": True}, format="json")
        self.assertEqual(response_patch.status_code, 403)

    def test_cannot_delete_another_user_fav(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.invalid_token.key)
        response_delete = self.client.delete(f"/api/watchlist/{self.fav.id}/")
        self.assertEqual(response_delete.status_code, 403)