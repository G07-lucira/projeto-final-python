import ipdb

from animes.models import Anime


def get_total_eps_count(anime: Anime):

    return anime.episodes.count()
