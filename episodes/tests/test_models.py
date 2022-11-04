from django.test import TestCase

from django.test import TestCase

from model_bakery import baker

from animes.models import Anime
from genres.models import Genre
from episodes.models import Episode

class EpisodeTestModel(TestCase):
    @classmethod
    def setUp(self):
        self.anime = baker.make("animes.Anime")
        self.episode_data =  {
            "name": "um macaco no navio",
            "epi_number": 1,
            "duration": "22:30",
            "anime": self.anime_x
            }
        self.episode = Episode.objects.create(**self.episode_data)
    def test_episode_is_positive(self):
        positive = self.anime.epi_number > 0 
        negative = self.anime.epi_number < 0 

        self.assertTrue(positive)
        self.assertFalse(negative)  

