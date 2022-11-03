# customers/tests/tests_model.py
from django.test import TestCase

from model_bakery import baker

from animes.serializers import AnimeSerializer
from animes.models import Anime
from genres.models import Genre

import ipdb


class GenreTestModel(TestCase):
    @classmethod
    def setUp(self):
        self.genre_jojo = baker.make(
            Genre,
            name="Jojo",
        )
        self.anime_dungeon = baker.make(
            Anime,
            name = "Dungeon ni Deai o Motomeru no wa Machigatteiru Darou ka",
            total_eps = 50,
            anime_img = "https://animesbr.biz/wp-content/uploads/2019/07/hR4zYTRJZiSYooocDRPW7P3PCTF-185x278.jpg",
            synopsis = "Baseado na light novel de mesmo nome escrita por Fujino Omori e ilustrada por Suzuhito Yasuda, Dungeon ni Deai o Motomeru no wa Machigatteiru Darou ka se passa no mundo de Orario, onde aventureiros se unem para caçar tesouros em labirintos subterrâneos conhecidos como Dungeon. No entanto, para Bell Cranel, fama e dinheiro estão em segundo plano; o que ele mais quer encontrar, na verdade, são garotas! Mas ele logo descobre que dentro de uma Dungeon tudo pode acontecer e, no fim, ele que acaba sendo a donzela em perigo!",
            author = "Fujino Omori",
            release_date = 6,
            is_finished = True
        )
    def test_create_anime(self):
        self.anime_one = self.anime_dungeon
        genres=self.genre_jojo
        self.anime_one.genres.add(genres)
        serializer = AnimeSerializer(self.anime_one)
        self.assertIsInstance(self.anime_one, Anime)
        self.assertEqual(serializer.data["name"], "Dungeon ni Deai o Motomeru no wa Machigatteiru Darou ka")
        self.assertEqual(serializer.data["synopsis"], "Baseado na light novel de mesmo nome escrita por Fujino Omori e ilustrada por Suzuhito Yasuda, Dungeon ni Deai o Motomeru no wa Machigatteiru Darou ka se passa no mundo de Orario, onde aventureiros se unem para caçar tesouros em labirintos subterrâneos conhecidos como Dungeon. No entanto, para Bell Cranel, fama e dinheiro estão em segundo plano; o que ele mais quer encontrar, na verdade, são garotas! Mas ele logo descobre que dentro de uma Dungeon tudo pode acontecer e, no fim, ele que acaba sendo a donzela em perigo!")
        self.assertEqual(serializer.data["total_eps"], 50)
        self.assertEqual(serializer.data["genres"][0]['name'], "Jojo")
    

