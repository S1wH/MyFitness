import os
import django
from celery import Celery
from django.core import mail

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myfitness.settings')
django.setup()

from users.models import User

app = Celery('myfitness')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task
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
