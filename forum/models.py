from django.db import models


class Citizen(models.Model):
    votes = models.IntegerField(default=0)
    name = models.CharField(max_length=20)


class Issue(models.Model):
    author = models.ForeignKey(Citizen)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    votes = models.IntegerField(default=0)
