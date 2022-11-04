from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from users.models import User
from episodes.serializers import RegisterEpisodeSerializer, EpisodeDetailSerializer

from model_bakery import baker

import ipdb

class UserTestViews(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.register_uri = "/api/accounts/"

        cls.login_uri = "/api/login/"

        cls.valid_user = {
            "username": "kenzinho",
            "email": "kenzinho@kenzinho.com",
            "password": "1234"
        }

        cls.valid_user2 = {
            "username": "kenzinho1",
            "email": "kenzinho1@kenzinho1.com",
            "password": "1234"
        }

        cls.valid_owner = {
            "username": "kenzinho2",
            "password": "1234"
        }

        cls.admin_data = {
            "username": "admin",
            "password": "1234"
        }

        cls.invalid_user = {
            "username": "",
            "password": ""
        }

        cls.episode_data_1={
	        "name": "Episodio 1",
	        "epi_number": 1,
	        "duration": "20:00"
        }

        cls.episode_updated={
            "name": "Episodio 1 Atualizado",
	        "duration": "20:30"
        }

        cls.anime_created_1 = baker.make('animes.Anime')

        cls.episode_create_1 = baker.make_recipe('episodes.new_episode')

        cls.owner = User.objects.create_user(**cls.valid_owner)

        cls.owner_token = Token.objects.create(user=cls.owner)

        cls.admin = User.objects.create_superuser(**cls.admin_data)

        cls.admin_token = Token.objects.create(user=cls.admin)

        cls.episode_create_uri = f'/api/animes/{cls.anime_created_1.id}/episode/'

        cls.episode_updated_uri = f'/api/episode/{cls.episode_create_1.id}/'

        cls.episode_delete_uri = f'/api/episode/{cls.episode_create_1.id}/'


    def test_can_not_register_a_episode_admin_only(self):

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.owner_token.key)
        
        response_post = self.client.post(self.episode_create_uri, self.episode_data_1, format="json")
       
        self.assertEqual(response_post.status_code, 403) 

    def test_can_register_a_episode_admin_only(self):

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_token.key)
        
        response_post = self.client.post(self.episode_create_uri, self.episode_data_1, format="json")
       
        self.assertEqual(RegisterEpisodeSerializer(instance=response_post.data).data, response_post.data)
        self.assertEqual(response_post.status_code, 201)

    def test_can_update_a_episode_admin_only(self):

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_token.key)
        
        response_patch = self.client.patch(self.episode_updated_uri, self.episode_updated, format="json")
        
        self.assertEqual(EpisodeDetailSerializer(instance=response_patch.data).data, response_patch.data)
        self.assertEqual(response_patch.data['name'], self.episode_updated['name'])
        self.assertEqual(response_patch.data['duration'], self.episode_updated['duration'])
        self.assertEqual(response_patch.status_code, 200)
           
    def test_can_not_update_a_episode_admin_only(self):

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_token.key)
        
        response_patch = self.client.patch(self.episode_updated_uri, self.episode_updated, format="json")
        
        self.assertEqual(response_patch.status_code, 403)

    def test_can_delete_a_episode_admin_only(self):

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_token.key)
        
        response_delete = self.client.delete(self.episode_delete_uri, format="json")
        
        self.assertEqual(response_delete.status_code, 204)
    
    def test_can_not_delete_a_episode_admin_only(self):

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.owner_token.key)
        
        response_delete = self.client.delete(self.episode_delete_uri, format="json")
        
        self.assertEqual(response_delete.status_code, 403)