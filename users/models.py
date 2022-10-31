from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    bio = models.TextField()
    birthday = models.DateTimeField()