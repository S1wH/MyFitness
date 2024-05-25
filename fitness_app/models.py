from django.db import models
from django.core.validators import MinValueValidator


class Tariff(models.Model):
    description = models.TextField()
    price = models.IntegerField(validators=[MinValueValidator(1)])
    bonuses = models.TextField()
