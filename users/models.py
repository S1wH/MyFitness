import string
import random
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models
from fitness_app.models import Tariff


def generate_activation_code() -> str:
    return ''.join(random.choice(string.digits) for _ in range(6))


class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class ActivationCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='user_code')
    code = models.CharField(max_length=6, default=generate_activation_code)


class Coach(models.Model):
    experience = models.IntegerField(validators=[MinValueValidator(1)], verbose_name='experience')
    specialization = models.TextField(verbose_name='specialization')
    achievements = models.TextField(verbose_name='achievements')
    photo = models.ImageField(upload_to='coach_photos')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='coach')

    class Meta:
        verbose_name = 'Coache'

    def __str__(self):
        return f'Coach {self.user.name} with {self.experience} experience years'


class Client(models.Model):
    LEVEL_NEWBIE = 'Нет опыта'
    LEVEL_BEGINNER = 'Начинающий уровень (до 1 года опыта)'
    LEVEL_INTERMEDIATE = 'Средний уровень (от 1 до 3 лет опыта)'
    LEVEL_ADVANCED = 'Продвинутый уровень (более 3 лет опыта)'
    LEVEL_CHOICES = [
        (LEVEL_NEWBIE, 'Нет опыта'),
        (LEVEL_BEGINNER, 'Начинающий уровень (до 1 года опыта)'),
        (LEVEL_INTERMEDIATE, 'Средний уровень (от 1 до 3 лет опыта)'),
        (LEVEL_ADVANCED, 'Продвинутый уровень (более 3 лет опыта)'),
    ]

    SEX_MALE = 'Мужской'
    SEX_FEMALE = 'Женский'
    SEX_CHOICES = [
        (SEX_MALE, 'Мужской'),
        (SEX_FEMALE, 'Женский'),
    ]

    sex = models.CharField(max_length=50, choices=SEX_CHOICES)
    birthday = models.DateField()
    height = models.IntegerField()
    weight = models.IntegerField()
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES, default=LEVEL_NEWBIE)
    contraindications = models.TextField(verbose_name='contraindications', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    tariff = models.ForeignKey(Tariff, on_delete=models.SET_NULL, default=None, blank=True, null=True,
                               related_name='clients')

    def __str__(self):
        return f'Client {self.user.name}'
