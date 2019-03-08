import json
from .models import Device
from django.shortcuts import render
from django.http import HttpResponse
from .communication import forward_action

def index(request):
	return HttpResponse("CTA CONFIGURADO UHUL BORA CACILDA!")

def devices(request):
	devices = [i for i in Device.objects.all()]

	return HttpResponse(json.dumps([i.asResponse() for i in devices ]), content_type='application/json' )

def device(request, deviceId):
	device = Device.objects.filter(id=deviceId)[0]

	return HttpResponse(json.dumps(device.asResponse()), content_type='application/json' )


def update_device(request, deviceId):
	device = Device.objects.filter(id=deviceId)[0]
	forward_action(device)
	return HttpResponse(json.dumps(device.asResponse()), content_type='application/json' )

