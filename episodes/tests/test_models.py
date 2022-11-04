from django.test import TestCase
from model_bakery import baker

import ipdb

class AccountModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.episode_create = baker.make_recipe('episodes.new_episode')
        

    def test_name_max_legth(self):

        max_length = self.episode_create._meta.get_field('name').max_length

        self.assertEqual(max_length, 127)

    def test_duration_max_legth(self):

        max_length = self.episode_create._meta.get_field('duration').max_length

        self.assertEqual(max_length, 10)

    def test_has_correct_fields(self):
        self.assertEqual(self.episode_create.name, "Episode atulizado")
        self.assertEqual(self.episode_create.epi_number, 1)
        self.assertEqual(self.episode_create.duration, '18:00')
    
    def test_epi_number_is_positive(self):
        self.assertTrue(self.episode_create.epi_number > 0)

    def test_episode_has_anime_id(self):
        self.assertTrue(self.episode_create.anime_id)
