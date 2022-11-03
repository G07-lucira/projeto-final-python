import uuid

from django.db import models


class Anime(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=127)
    total_eps = models.PositiveIntegerField(max_length=20)
    anime_img = models.CharField(max_length=127)
    synopsis = models.TextField()
    author = models.CharField(max_length=127, null=True)
    release_date = models.DateField()
    is_finished = models.BooleanField()

    genres = models.ManyToManyField("genres.Genre", related_name="animes")
