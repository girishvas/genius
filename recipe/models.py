from django.db import models
from django.contrib.auth.models import User
import datetime


class Recipe(models.Model):
	name 		= models.CharField(max_length=200, null=False, unique=True, blank=False)
	user 		= models.OneToOneField(User, on_delete=models.CASCADE)

	createdOn 	= models.DateTimeField(auto_now_add=True)
	updatedOn 	= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Step(models.Model):
	step 		= models.TextField()
	recipe 		= models.ForeignKey(Recipe, related_name='steps', on_delete=models.CASCADE)

	createdOn 	= models.DateTimeField(auto_now_add=True)
	updatedOn 	= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.step


class Ingredient(models.Model):
	ingredient 	= models.CharField(max_length=500)
	recipe 		= models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)

	createdOn 	= models.DateTimeField(auto_now_add=True)
	updatedOn 	= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.ingredient