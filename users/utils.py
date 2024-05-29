from django.core.exceptions import ValidationError
from django.core import mail
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


def send_mail(user_id: int, code: str) -> None:
    with mail.get_connection() as connection:
        user = User.objects.get(id=user_id)
        email_body = (f'Здравствуйте {user.first_name} {user.last_name}!'
                      f' Ваш код подтверждения для завершения регистрации: {code}')
        mail.EmailMessage(
            subject='Подтверждение регистрации',
            body=email_body,
            from_email='settings.EMAIL_HOST_USER',
            to=[user.email],
            connection=connection
        ).send()
