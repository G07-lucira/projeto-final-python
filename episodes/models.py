from django.db import models
import uuid

class Episode(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=127)
    epi_number = models.PositiveIntegerField()
    duration = models.CharField(max_length=10)

    anime = models.ForeignKey(
        "animes.Anime",
        on_delete=models.CASCADE,
        related_name="episodes"
    )