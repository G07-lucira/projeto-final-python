from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    bio = models.TextField(null=True)
    birthday = models.DateTimeField(null=True)

    animes = models.ManyToManyField(
        "animes.Anime",
        through="users_animes.UserAnimes",
        related_name="users",
        null=True
    )
