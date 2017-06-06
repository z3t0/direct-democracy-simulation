from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Citizen(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    votes = models.IntegerField(default=0)
    name = models.CharField(max_length=20)

    @receiver(post_save, sender=User)
    def create_user_citizen(sender, instance, created, **kwargs):
        if created:
            Citizen.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_citizen(sender, instance, **kwargs):
        instance.citizen.save()


class Issue(models.Model):
    author = models.ForeignKey(Citizen)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    votes = models.IntegerField(default=0)
