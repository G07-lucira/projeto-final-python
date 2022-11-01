import uuid
from django.db import models

class Anime(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=127)
    duration = models.TimeField()
    total_eps = models.PositiveIntegerField()
    
    release_date = models.DateField()
    current_status = models.BooleanField()


    genres = models.ManyToManyField(
        "genres.Genre",
        related_name="animes"
    )
    
