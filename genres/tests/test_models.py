# customers/tests/tests_model.py
from django.test import TestCase

from model_bakery import baker

from genres.serializers import GenreSerializer
from genres.models import Genre

class GenreTestModel(TestCase):
    @classmethod
    def setUp(self):
        self.genre_jojo = baker.make(
            Genre,
            name="Jojo",
        )

    def test_create_genre(self):
        self.genre_one = self.genre_jojo
        serializer = GenreSerializer(self.genre_one)
        self.assertIsInstance(self.genre_one, Genre)
        self.assertEqual(serializer.data["name"], "Jojo")
