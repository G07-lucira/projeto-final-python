from django.test import TestCase

from django.test import TestCase

from model_bakery import baker

from comments.models import Comment


class GenreTestModel(TestCase):
    @classmethod
    def setUp(self):
        self.comment = baker.make(Comment)
    def test_create_comment_episode(self):
        comment = self.comment
        self.assertIsInstance(comment, Comment)

