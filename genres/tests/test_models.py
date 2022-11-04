from django.test import TestCase

from genres.serializers import GenreSerializer

from genres.models import Genre

class GenreTestModel(TestCase):
    @classmethod
    def setUp(self):
        self.genre_data = {"name":"jojo"}
        self.genre = Genre.objects.create(**self.genre_data)
    def test_genre_name_max_length(self):
        max_length = self.genre._meta.get_field('name').max_length

        self.assertEqual(max_length, 127)