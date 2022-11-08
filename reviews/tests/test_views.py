from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from users.models import User
from reviews.serializers import ReviewSerializer

from model_bakery import baker


class ReviewViewTests(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = baker.make("users.User")
        cls.user_token = Token.objects.create(user=cls.user)

        cls.non_owner = baker.make("users.User")
        cls.non_owner_token = Token.objects.create(user=cls.non_owner)

        cls.admin_data = {"username": "admin", "password": "1234"}
        cls.admin = User.objects.create_superuser(**cls.admin_data)
        cls.admin_token = Token.objects.create(user=cls.admin)

        cls.anime = baker.make("animes.Anime")
        cls.anime2 = baker.make("animes.Anime")

        cls.review = baker.make("reviews.Review", anime=cls.anime, user=cls.user)
        cls.review_data = {
            "title": "One of the best",
	        "description": "pretty good!!",
	        "recommended": True,
        }
        cls.review_uri = f"/api/reviews/{cls.anime.id}/"
        cls.detailed_review_uri = f"/api/reviews/{cls.review.id}/del/" 

    # OWNER-ROUTE BASED TESTS
    def test_can_create_new_review_as_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)
        post = self.client.post(f"/api/reviews/{self.anime2.id}/", self.review_data, format="json")
        self.assertEqual(post.status_code, 201)

    def test_cannot_create_new_review_if_already_reviewed(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)
        post = self.client.post(self.review_uri, self.review_data, format="json")
        self.assertEqual(post.status_code, 403)

    def test_owner_can_list_review_by_id(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)
        get = self.client.get(self.detailed_review_uri)
        self.assertEqual(get.status_code, 200)
    
    def test_owner_can_edit_review(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)
        patch = self.client.patch(self.detailed_review_uri, {"recommended": True}, format="json")
        self.assertFalse(self.review.recommended)
        self.assertEqual(patch.status_code, 200)
        get = self.client.get(self.detailed_review_uri)
        self.assertTrue(get.data["recommended"])

    def test_owner_can_delete_review(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)
        delete = self.client.delete(self.detailed_review_uri)
        self.assertEqual(delete.status_code, 204) 

    # ADMIN BASED TESTS
    def test_cannot_edit_review_if_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_token.key)
        patch = self.client.patch(self.detailed_review_uri, {"recommended": True}, format="json")
        self.assertEqual(patch.status_code, 403)
        
    def test_can_delete_review_if_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_token.key)
        delete = self.client.delete(self.detailed_review_uri)
        self.assertEqual(delete.status_code, 204)  

    # "CANNOT" TESTS
    def test_cannot_create_new_review_without_necessary_infos(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)
        post = self.client.post(f"/api/reviews/{self.anime2.id}/", {}, format="json")
        self.assertEqual(post.status_code, 400)
        for key, value in post.data.items():
            self.assertEqual(value[0][:], "This field is required.")

    def test_non_owner_cannot_edit_review(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.non_owner_token.key)
        patch = self.client.patch(self.detailed_review_uri, {"recommended": True}, format="json")
        self.assertEqual(patch.status_code, 403)

    def test_non_owner_cannot_delete_review(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.non_owner_token.key)
        delete = self.client.delete(self.detailed_review_uri)
        self.assertEqual(delete.status_code, 403)  

    def test_cannot_create_new_review_without_auth(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ')
        post = self.client.post(self.review_uri, self.review_data, format="json")
        self.assertEqual(post.status_code, 401)
        
    def test_cannot_edit_existing_review_without_auth(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ')
        patch = self.client.patch(self.detailed_review_uri, {"recommended": True}, format="json")
        self.assertEqual(patch.status_code, 401)

    def test_cannot_delete_existing_review_without_auth(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ')
        delete = self.client.delete(self.review_uri)
        self.assertEqual(delete.status_code, 401)