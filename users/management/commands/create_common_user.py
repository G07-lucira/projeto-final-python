from users.models import User

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Create user'

    def handle(self, *args, **kwargs):
            User.objects.create_user(
                username="kenzinho",
                password='1234'
            )
