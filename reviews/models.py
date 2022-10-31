from django.db import models
import uuid

class Reviews(models.Models):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = mdels.CharField(max_length=50)
    description = models.TextField()
    recommended = models.BooleanField(default=False)
    
    anime_id = models.ForeignKey("animes.Anime", on_delete=models.CASCADE, related_name="reviews")
    user_id = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="reviews")
