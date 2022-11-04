from django.test import TestCase

from django.test import TestCase

from model_bakery import baker

from comments.models import Comment


class GenreTestModel(TestCase):
    @classmethod
    def setUp(self):
        self.episode = baker.make("episodes.Episode")
        self.user = baker.make("users.User")
        self.comment_data = {
            "comment":"gostei muito, tem bolo",
            "episode_id": self.episode.id,
            "user_id": self.user.id
        }
        self.comment = Comment.objects.create(**self.comment_data)
    def test_spoiler_is_default_false(self):
        default_false = self.comment._meta.get_field('spoiler').default

        self.assertEqual(default_false, False)
