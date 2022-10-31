from django.db import models
import uuid


class UserAnimes(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    anime = models.ForeignKey("animes.Anime", on_delete=models.CASCADE)
    last_watched = models.DateField()
    last_episode = models.PositiveIntegerField()
