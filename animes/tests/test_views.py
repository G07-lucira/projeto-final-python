from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from users.models import User
from animes.serializers import AnimeSerializer, AnimeDetailsSerializer

from model_bakery import baker

import ipdb

class UserTestViews(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.anime_uri = "/api/animes/"
        cls.user = baker.make("users.User")
        cls.admin_data = {
            "username": "admin",
            "password": "1234"
        }
        cls.anime = baker.make("animes.Anime")
        cls.anime_data = {
            "name": "Hellsing Ultimate",
	        "total_eps": 10,
	        "release_date": 2006,
	        "is_finished": True,
            "synopsis": "lorem ipsum",
	        "genres":[
			    {"name": "Action"},
			    {"name": "Horror"},
			    {"name": "Military"},
			    {"name": "Seinen"},
			    {"name": "Supernatural"},
			    {"name": "Vampire"},
			    {"name": "Lucira"},
			    {"name": "Silva"}
		    ],
	        "author":"Kouta Hirano",
            "anime_img": "image"
        }
        cls.user_token = Token.objects.create(user=cls.user)
        cls.admin = User.objects.create_superuser(**cls.admin_data)
        cls.admin_token = Token.objects.create(user=cls.admin)
    
    def test_can_create_new_anime_as_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_token.key)
        post = self.client.post(self.anime_uri, self.anime_data, format="json")
        self.assertEqual(post.status_code, 201)
        self.assertEqual(AnimeSerializer(instance=post.data).data, post.data)

    def test_cannot_create_new_anime_as_non_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)
        post = self.client.post(self.anime_uri, self.anime_data, format="json")
        self.assertEqual(post.status_code, 403)
    
    def test_can_edit_anime_as_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_token.key)
        patch = self.client.patch(f"/api/animes/{self.anime.id}/", {"name": "Réusin"}, format="json")
        self.assertEqual(patch.status_code, 200)

    def test_cannot_edit_anime_as_non_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)
        patch = self.client.patch(f"/api/animes/{self.anime.id}/", {"name": "Réusin"}, format="json")
        self.assertEqual(patch.status_code, 403)
    
    def test_can_delete_anime_as_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_token.key)
        delete = self.client.delete(f"/api/animes/{self.anime.id}/")
        self.assertEqual(delete.status_code, 204)

    def test_cannot_delete_anime_as_non_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)
        delete = self.client.delete(f"/api/animes/{self.anime.id}/")
        self.assertEqual(delete.status_code, 403)
    
    