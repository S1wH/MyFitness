from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def user_post_save(**kwargs):
    if kwargs.get('created') is True:
        user = kwargs.get('instance')
        Token.objects.create(user=user)
