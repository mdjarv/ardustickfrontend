from django.db import models
import rabbitpy

class Remote(models.Model):
    name = models.CharField(max_length=256)
    identifier = models.BigIntegerField()


class Device(models.Model):
    name = models.CharField(max_length=256)
    identifier = models.IntegerField()
    remote = models.ForeignKey(Remote)

    def on(self):
        rabbitpy.publish(exchange='ardustick',
                         routing_key='',
                         body={
                             'remote': self.remote.identifier,
                             'device': self.identifier,
                             'status': 1
                         })

    def off(self):
        rabbitpy.publish(exchange='ardustick',
                         routing_key='',
                         body={
                             'remote': self.remote.identifier,
                             'device': self.identifier,
                             'status': 0
                         })
