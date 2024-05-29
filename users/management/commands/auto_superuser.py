import os
from dotenv import load_dotenv
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = "script that creates a superuser"

    def __init__(self):
        super().__init__()
        self.ADMIN_NAME = 'ADMIN_NAME'
        self.ADMIN_EMAIL = 'ADMIN_EMAIL'
        self.ADMIN_PASSWORD = 'ADMIN_PASSWORD'
        self.ADMIN_FIRST_NAME = 'ADMIN_FIRST_NAME'
        self.ADMIN_LAST_NAME = 'ADMIN_LAST_NAME'

    def handle(self, *args, **kwargs):
        load_dotenv()
        username = os.getenv(self.ADMIN_NAME)
        try:
            user = User.objects.get(username=username, is_superuser=True)
            print(f"Superuser {user} already exists\n")
        except ObjectDoesNotExist:
            print("\nCreating superuser...\n")
            email = os.getenv(self.ADMIN_EMAIL)
            password = os.getenv(self.ADMIN_PASSWORD)
            first_name = os.getenv(self.ADMIN_FIRST_NAME)
            last_name = os.getenv(self.ADMIN_LAST_NAME)
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                is_verified=True,
                is_staff=True,
                is_active=True,
                is_superuser=True,
            )
            print(f"Superuser {user} successfully created\n")
        print(f"email is {user.email}")
        print("password is admin123\n")
