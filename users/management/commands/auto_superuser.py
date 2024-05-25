from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "script that creates a superuser"

    def handle(self, *args, **kwargs):
        try:
            user = User.objects.get(username="admin", is_superuser=True)
            print(f"Superuser {user} already exists\n")
        except ObjectDoesNotExist:
            print("\nCreating superuser...\n")
            user = User.objects.create_user(
                username="admin",
                email="admin@admin.ru",
                password="admin123",
                is_staff=True,
                is_active=True,
                is_superuser=True,
            )
            print(f"Superuser {user} successfully created\n")
        print(f"username is {user.username}")
        print("password is admin123\n")
