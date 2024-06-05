from django.db import models
from django.core.validators import MinValueValidator


class MuscleGroup(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f'Muscle group {self.name}'


class Tariff(models.Model):
    name = models.CharField(unique=True, max_length=20)
    description = models.TextField()
    price = models.IntegerField(validators=[MinValueValidator(1)])
    bonuses = models.TextField()

    def __str__(self):
        return f'Tariff {self.name}'


class Exercise(models.Model):
    name = models.CharField(unique=True, max_length=20)
    description = models.TextField()
    duration = models.DurationField()
    muscle_group = models.ManyToManyField(MuscleGroup, related_name='exercises')
    contraindications = models.TextField(verbose_name='contraindications', blank=True, null=True)

    def __str__(self):
        return f'Exercise {self.name}'
