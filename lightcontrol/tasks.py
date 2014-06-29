from __future__ import absolute_import

from celery import shared_task

import serial
import time

@shared_task
def set_light(device, status):
    ser = serial.Serial('/dev/ttyS1', 115200, timeout=1)
    time.sleep(0.01)
    ser.write("%d,%d,%d\n" % (
        device.remote.identifier,
        device.identifier,
        status))
    result = ser.readline().strip(' \t\n\r')
    ser.close()
    return result