from django.forms import ModelForm
from packing.models import Thing, Box

class ThingForm(ModelForm):
	class Meta:
		model = Thing
		fields = ('name', 'description','box')

class BoxForm(ModelForm):
	class Meta:
		model = Box
		fields = ('name', 'description',)