from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(pre_save, sender=User)
def user_post_save(**kwargs):
    if 'update_fields' in kwargs.keys():
        if kwargs['update_fields'] is not None:
            model = kwargs['instance']
            if model.pk is None:
                token = Token.objects.create(user=model)
                print(f'token: {token}')
