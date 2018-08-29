from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Location(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()


class Visit(models.Model):
    user = models.ForeignKey('auth.User', related_name='visits', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', default='', blank=True, null=True, related_name='locations', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    ratio = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(0)]
    )
