from django.db import models
import uuid

class Review(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=50)
    description = models.TextField()
    recommended = models.BooleanField(default=False)
    
    anime = models.ForeignKey(
        "animes.Anime",
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reviews"
    )
