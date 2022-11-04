from django.test import TestCase

from django.test import TestCase

from model_bakery import baker

from comments.models import Comment


class ReviewTestModel(TestCase):
    @classmethod
    def setUp(self):
        self.review = baker.make("reviews.Review")
    def test_recomendation_is_default_false(self):
        default_false = self.review._meta.get_field('recommended').default

        self.assertEqual(default_false, False)
    def test_title_max_length(self):
        max_length = self.review._meta.get_field('title').max_length

        self.assertEqual(max_length, 50)
