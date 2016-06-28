from django.shortcuts import render
from packing.models import Box, Thing

def index(request):
	boxes = Box.objects.all()
	return render(
		request,
		'index.html',
		{'boxes': boxes,}
		)