from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Location(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()


class Visit(models.Model):
    user_id = models.CharField(max_length=100)
    location_id = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    ratio = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(0)]
    )
