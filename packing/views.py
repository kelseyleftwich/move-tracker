from django.shortcuts import render, redirect
from packing.forms import ThingForm, BoxForm
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

def edit_thing(request, thing_id):
	# grab the object
	thing = Thing.objects.get(id=thing_id)
	# set the form we're using...
	form_class = ThingForm
	# if form has been submitted
	if request.method == 'POST':
		# grab the data from the submitted form
		form = form_class(data=request.POST, instance=thing)
		if form.is_valid():
			# save the new data
			form.save()
			return redirect('thing_detail', thing_id = thing.id)
	# otherwise just create the form
	else:
		form = form_class(instance=thing)
		# and render the template
		return render(request, 'things/edit_thing.html', {'thing': thing, 'form': form,})

def edit_box(request, box_id):
	# grab the object
	box = Box.objects.get(id=box_id)
	# set the form we're using...
	form_class = BoxForm
	# if form has been submitted
	if request.method == 'POST':
		# grab the data from the submitted form
		form = form_class(data=request.POST, instance=box)
		if form.is_valid():
			# save the new data
			form.save()
			return redirect('box_detail', box_id = box.id)
	# otherwise just create the form
	else:
		form = form_class(instance=box)
		# and render the template
		return render(request, 'boxes/edit_box.html', {'box': box, 'form': form,})