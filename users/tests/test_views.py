from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from users.serializers import RegisterUserSerializer, UserDetailSerializer
from users.models import User

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
        cls.owner = User.objects.create_user(**cls.valid_owner)
        cls.owner_token = Token.objects.create(user=cls.owner)
        cls.admin = User.objects.create_superuser(**cls.admin_data)
        cls.admin_token = Token.objects.create(user=cls.admin)
    
    def test_can_register_user(self):
        response_post = self.client.post(self.register_uri, self.valid_user, format="json")
        self.assertEqual(RegisterUserSerializer(instance=response_post.data).data, response_post.data)
        self.assertEqual(response_post.status_code, 201)

    def test_cannot_register_user(self):
        response_post = self.client.post(self.register_uri, {}, format="json")
        self.assertEqual(response_post.status_code, 400)
        for key, value in response_post.data.items():
            self.assertEqual(value[0][:], "This field is required.")
    
    def test_can_login_user(self):
        response_post = self.client.post(self.register_uri, self.valid_user, format="json")
        login_user = self.client.post(self.login_uri, self.valid_user, format="json")
        self.assertEqual(login_user.status_code, 200)
    
    def test_cannot_login_user(self):
        response_post = self.client.post(self.login_uri, self.invalid_user, format="json")
        self.assertEqual(response_post.status_code, 400)
    
    def test_can_edit_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.owner_token.key)
        response_patch = self.client.patch(f"/api/accounts/{self.owner.id}/", {"bio": "Kenny"}, format="json")
        self.assertEqual(UserDetailSerializer(instance=response_patch.data).data, response_patch.data)
        self.assertEqual(response_patch.status_code, 200)

    def test_can_edit_user_if_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_token.key)
        response_patch = self.client.patch(f"/api/accounts/{self.owner.id}/", {"first_name": "Kenny"}, format="json")
        self.assertEqual(UserDetailSerializer(instance=response_patch.data).data, response_patch.data)
        self.assertEqual(response_patch.status_code, 200)

    def test_cannot_edit_without_token(self):
        response_patch = self.client.patch(f"/api/accounts/{self.owner.id}/", {"first_name": "Kenny"}, format="json")
        self.assertEqual(response_patch.status_code, 401)

    def test_cannot_edit_user(self):
        user = User.objects.create_user(**self.valid_user2)
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token' + token.key)
        response_patch = self.client.patch(f"/api/accounts/{self.owner.id}/", {"first_name": "Kenny"}, format="json")
        self.assertEqual(response_patch.status_code, 401)
    
    def test_can_safe_delete_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.owner_token.key)
        response_delete = self.client.delete(f"/api/accounts/{self.owner.id}/")
        self.assertEqual(response_delete.status_code, 204)

    def test_can_safe_delete_user_if_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_token.key)
        response_delete = self.client.delete(f"/api/accounts/{self.owner.id}/")
        self.assertEqual(response_delete.status_code, 204)
    
    def test_cannot_safe_delete_without_token(self):
        response_delete = self.client.delete(f"/api/accounts/{self.owner.id}/")
        self.assertEqual(response_delete.status_code, 401)
    
    def test_cannot_safe_delete_user(self):
        user = User.objects.create_user(**self.valid_user2)
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token' + token.key)
        response_delete = self.client.delete(f"/api/accounts/{self.owner.id}/")
        self.assertEqual(response_delete.status_code, 401)