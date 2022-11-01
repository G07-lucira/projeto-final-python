import uuid

from django.db import models


class Anime(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=127)
    total_eps = models.CharField(max_length=20)
    animeImg = models.CharField(max_length=127)
    synopsis = models.TextField()
    release_date = models.CharField(max_length=6)
    current_status = models.CharField(max_length=20)

    genres = models.ManyToManyField("genres.Genre", related_name="animes")
