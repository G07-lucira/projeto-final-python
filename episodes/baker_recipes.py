from model_bakery.recipe import Recipe
from episodes.models import Episode

new_episode = Recipe(
    Episode,
    name='Episode atulizado',
    duration='18:00',
    epi_number=1
)