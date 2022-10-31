import uuid
from platform import release

from django.db import models
from traitlets import default


# Create your models here.
class Animes(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_lenght=127)
    duration = models.DateTimeField()
    total_eps = models.PositiveIntegerField()
    
    release_date = models.DateField()
    current_status = models.BooleanField()

    # FK
    genres = models.ManyToManyField("genres.Genre", related_name="animes")
    
