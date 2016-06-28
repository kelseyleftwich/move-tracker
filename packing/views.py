from django.shortcuts import render
from packing.models import Box, Thing

def index(request):
	boxes = Box.objects.all()
	return render(
		request,
		'index.html',
		{'boxes': boxes,}
		)

def box_detail(request, box_id):
	box = Box.objects.get(id=box_id)
	return render(
		request,
		'boxes/box_detail.html',
		{'box': box,}
		)

def thing_detail(request, thing_id):
	thing = Thing.objects.get(id=thing_id)
	return render(
		request,
		'things/thing_detail.html',
		{'thing': thing,}
		)