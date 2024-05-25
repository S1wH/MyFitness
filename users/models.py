from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from fitness_app.models import Tariff


class Coach(models.Model):
    name = models.CharField(unique=True, max_length=100)
    experience = models.IntegerField(validators=[MinValueValidator(1)], verbose_name='experience')
    specialization = models.TextField(verbose_name='specialization')
    achievements = models.TextField(verbose_name='achievements')
    photo = models.ImageField(upload_to='coach_photos')
    user = models.OneToOneField(User, on_delete=models.CASCADE)


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

    name = models.CharField(unique=True, max_length=100)
    birthday = models.DateField()
    height = models.IntegerField()
    weight = models.IntegerField()
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES, default=LEVEL_NEWBIE)
    contraindications = models.TextField(verbose_name='contraindications', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tariff = models.ForeignKey(Tariff, on_delete=models.SET_NULL, default=None, blank=True, null=True)
