from django.db import models
from django.conf import settings

#TODO why are there two places with images

class Project(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	detailedDescription = models.TextField()
	technology = models.TextField()
	linkToProject = models.CharField(max_length=100, null=True)
	image = models.FileField(null = True)