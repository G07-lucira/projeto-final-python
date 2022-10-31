from django.db import models
import uuid

class Epidsode(models.Models):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=127)
    number = models.IntegerField()
    duration = models.CharField(max_length=10)

    anime = models.ForeignKey(
        "Animes.animes",
        on_delete=models.CASCADE,
        related_name="episodes"
    )