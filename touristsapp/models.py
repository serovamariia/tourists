from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=30, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


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
