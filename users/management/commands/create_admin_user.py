from users.models import User

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Create superuser'

    def handle(self, *args, **kwargs):
            User.objects.create_superuser(
                username="kenzieroll",
                password='1234'
            )
