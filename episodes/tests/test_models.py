from django.test import TestCase

from django.test import TestCase

from model_bakery import baker

from animes.models import Anime
from genres.models import Genre
from episodes.models import Episode

class GenreTestModel(TestCase):
    @classmethod
    def setUp(self):
        self.genre_jojo = baker.make(
            Genre,
            name="Jojo",
        )
        self.anime_x = baker.make(
            Anime,
            name = "Dungeon ni Deai o Motomeru no wa Machigatteiru Darou ka",
            total_eps = 50,
            anime_img = "https://animesbr.biz/wp-content/uploads/2019/07/hR4zYTRJZiSYooocDRPW7P3PCTF-185x278.jpg",
            synopsis = "Baseado na light novel de mesmo nome escrita por Fujino Omori e ilustrada por Suzuhito Yasuda, Dungeon ni Deai o Motomeru no wa Machigatteiru Darou ka se passa no mundo de Orario, onde aventureiros se unem para caçar tesouros em labirintos subterrâneos conhecidos como Dungeon. No entanto, para Bell Cranel, fama e dinheiro estão em segundo plano; o que ele mais quer encontrar, na verdade, são garotas! Mas ele logo descobre que dentro de uma Dungeon tudo pode acontecer e, no fim, ele que acaba sendo a donzela em perigo!",
            author = "Fujino Omori",
            release_date = 6,
            is_finished = True,
            genres=[self.genre_jojo]
        )
        self.episode_69 = baker.make(
            Episode,
            name = "um macaco no navio",
            epi_number = 69,
            duration = "22:30",
            anime= self.anime_x
        )
    def test_create_anime_episode(self):
        episode = self.episode_69
        self.assertIsInstance(episode, Episode)

