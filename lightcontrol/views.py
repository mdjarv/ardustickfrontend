from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from lightcontrol.models import Device


def set_light(request, device=0, status=0):
    dev = Device.objects.filter(identifier=device)[0]

    if status == "1":
        dev.on()
    else:
        dev.off()

    return HttpResponse(dev.name)

