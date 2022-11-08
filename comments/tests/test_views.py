from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from users.models import User
from comments.serializers import CommentSerializer, CommentDetailSerializer

from model_bakery import baker

class CommentsTests(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = baker.make("users.User")
        cls.user_token = Token.objects.create(user=cls.user)

        cls.non_owner = baker.make("users.User")
        cls.non_owner_token = Token.objects.create(user=cls.non_owner)

        cls.admin_data = {"username": "admin", "password": "1234"}
        cls.admin = User.objects.create_superuser(**cls.admin_data)
        cls.admin_token = Token.objects.create(user=cls.admin)

        cls.episode = baker.make("episodes.Episode")

        cls.comment = baker.make("comments.Comment", user=cls.user)
        cls.comment_data = {
            "comment": "LETSGOOOOOO",
            "spoiler": False
        }

        cls.all_comments_uri = f"/api/episode/{cls.episode.id}/comments/"
        cls.comment_id_uri = f"/api/comments/{cls.comment.id}/" 
    
    # OPEN ROUTE TESTS
    def test_all_users_can_list_all_comments_by_episode_id(self):
        get = self.client.get(self.all_comments_uri)
        self.assertEqual(get.status_code, 200)

    # OWNER-ROUTE BASED TESTS
    def test_can_create_new_comment_as_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)
        post = self.client.post(self.all_comments_uri, self.comment_data, format="json")
        self.assertEqual(post.status_code, 201)
    
    def test_owner_can_edit_comment(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)
        patch = self.client.patch(self.comment_id_uri, {"spoiler": True}, format="json")
        get = self.client.get(self.comment_id_uri)
        self.assertFalse(self.comment.spoiler)
        self.assertEqual(patch.status_code, 200)
        self.assertTrue(get.data["spoiler"])
    
    def test_owner_can_delete_comment(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)
        delete = self.client.delete(self.comment_id_uri)
        self.assertEqual(delete.status_code, 204)

    # ADMIN-ROUTE BASED TESTS
    def test_admin_cannot_edit_comment(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_token.key)
        patch = self.client.patch(self.comment_id_uri, {"spoiler": True}, format="json")
        self.assertEqual(patch.status_code, 403)
    
    def test_admin_can_delete_comment(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_token.key)
        delete = self.client.delete(self.comment_id_uri)
        self.assertEqual(delete.status_code, 204)

    # NON-OWNER BASED TESTS
    def test_cannot_edit_comment_without_ownership(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.non_owner_token.key)
        patch = self.client.patch(self.comment_id_uri, {"spoiler": True}, format="json")
        self.assertEqual(patch.status_code, 403)
    
    def test_cannot_delete_comment_without_ownership(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.non_owner_token.key)
        delete = self.client.delete(self.comment_id_uri)
        self.assertEqual(delete.status_code, 403)
    
    # NON-AUTH BASED TESTS
    def test_cannot_create_comment_without_auth(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ')
        post = self.client.post(self.all_comments_uri, self.comment_data, format="json")
        self.assertEqual(post.status_code, 401)
    
    def test_cannot_edit_comment_without_auth(self):
        patch = self.client.patch(self.comment_id_uri, {"spoiler": True}, format="json")
        self.assertEqual(patch.status_code, 401)
    
    def test_cannot_delete_comment_without_auth(self):
        delete = self.client.delete(self.comment_id_uri)
        self.assertEqual(delete.status_code, 401)