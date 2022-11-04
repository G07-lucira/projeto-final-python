from django.test import TestCase
from animes.models import Anime

class GenreTestModel(TestCase):
    @classmethod
    def setUp(self):
        self.anime_data = {
			"name": "Hellsing Ultimate",
			"total_eps": 10,
			"release_date": 2006,
			"is_finished": True,
			"author":"Kouta Hirano",
			"anime_img": "https://gogocdn.net/images/anime/H/hellsing-ultimate.jpg",
			"synopsis": "Vampires exist. It is the duty of Hellsing, a secret organization sponsored by the British government, to hide that frightening fact and protect the blissfully unaware populace. Along with its own personal army, Hellsing has secret weapons. Alucard, an incredibly powerful vampire, has been controlled by Hellsing for years. It is unclear how he feels about being a servant to the Hellsing family, but he certainly enjoys his job as a vampire exterminator. Seras is a fledgling vampire and former police woman. Although reluctant to embrace her new self, she is a valued member of the organization.\n\nIntegra Hellsing, the current leader, is usually fully capable of fulfilling her duty, but lately, vampire activity has been on the rise. Unfortunately, the cause is more alarming than anything she could have imagined. A group long thought dead has been plotting in secret since their apparent destruction over 50 years ago."
		}
        self.anime = Anime.objects.create(**self.anime_data)

    def test_name_max_length(self):
        max_length = self.anime._meta.get_field('name').max_length

        self.assertEqual(max_length, 127)

    def test_episode_is_positive(self):
        positive = self.anime.total_eps > 0 
        negative = self.anime.total_eps < 0 

        self.assertTrue(positive)
        self.assertFalse(negative)

