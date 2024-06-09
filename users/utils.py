from django.core.exceptions import ValidationError
from .models import User


def create_user(data: dict) -> User:
    email = data.get('email', None)
    if not email:
        raise ValidationError('Введите пожайлуста e-mail.')
    first_name = data.get('first_name', None)
    if not first_name:
        raise ValidationError('Введите пожайлуста имя.')
    second_name = data.get('last_name', None)
    if not second_name:
        raise ValidationError('Введите пожайлуста фамилию.')
    password = data.get('password', None)
    if not password:
        raise ValidationError('Введите пожайлуста пароль.')
    return User.objects.create(email=email, password=password, first_name=first_name, last_name=second_name)


def check_user(request_user: User, url_user: User) -> bool:
    return request_user == url_user or request_user.is_superuser is True
