from django.db import models

class Box(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name

class Thing(models.Model):
	box = models.ForeignKey(Box, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name