from django.db import models

class Remote(models.Model):
    name = models.CharField(max_length=256)
    identifier = models.BigIntegerField()

class Device(models.Model):
    name = models.CharField(max_length=256)
    identifier = models.IntegerField()
    remote = models.ForeignKey(Remote)