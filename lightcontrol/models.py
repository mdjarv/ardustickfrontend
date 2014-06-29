from django.db import models
from lightcontrol.tasks import set_light

class Remote(models.Model):
    name = models.CharField(max_length=256)
    identifier = models.BigIntegerField()

class Device(models.Model):
    name = models.CharField(max_length=256)
    identifier = models.IntegerField()
    remote = models.ForeignKey(Remote)

    def on(self):
        set_light.delay(self, 1)

    def off(self):
        set_light.delay(self, 0)