from django.db import models
import uuid


class Comment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    comment = models.TextField()
    spoiler = models.BooleanField(default=False)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="comments"
    )
    episode = models.ForeignKey(
        "episodes.Episode", on_delete=models.CASCADE, related_name="comments"
    )
