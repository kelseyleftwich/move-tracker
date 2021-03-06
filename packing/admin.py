from django.contrib import admin
from packing.models import Box, Thing

class BoxAdmin(admin.ModelAdmin):
	model = Box
	list_display = ('name', 'description','user')

class ThingAdmin(admin.ModelAdmin):
	model = Thing
	list_display = ('name', 'description','user')

admin.site.register(Box, BoxAdmin)
admin.site.register(Thing, ThingAdmin)
