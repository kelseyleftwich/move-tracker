from django.db import models
from django.contrib.auth.models import User

class Box(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

	def __str__(self):
		return self.name

class Thing(models.Model):
	box = models.ForeignKey(Box, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

	def __str__(self):
		return self.name