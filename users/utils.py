from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


def create_user(data):
    username = data.get('username', None)
    if not username:
        raise ValidationError('Введите пожайлуста имя.')
    password = data.get('password', None)
    if not password:
        raise ValidationError('Введите пожайлуста пароль.')
    return User.objects.create(username=username, password=password)
