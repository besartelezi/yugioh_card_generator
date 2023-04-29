from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class MonsterCard(models.Model):
    name= models.CharField(max_length=90)
    attribute = models.CharField(max_length=90)
    stars = models.PositiveIntegerField(default=4, validators=[MinValueValidator(1), MaxValueValidator(12)])
    type = ArrayField(models.CharField(max_length=20))
    description = models.CharField(max_length=250)
    attack = models.PositiveBigIntegerField()
    defense = models.PositiveIntegerField()

    def __str__(self):
        return self.task