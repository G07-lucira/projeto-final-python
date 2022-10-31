import uuid

from django.db import models
from traitlets import default


# Create your models here.
class Genres(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=127)
