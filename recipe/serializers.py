from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'url', 'username', 'email', 'first_name', 'last_name']


class StepSerializer(serializers.ModelSerializer):
	class Meta:
		model 	= Step
		fields 	= ('id', 'url', 'step', 'recipe')


class IngredientSerializer(serializers.ModelSerializer):
	class Meta:
		model 	= Ingredient
		fields 	= ('id', 'url', 'ingredient', 'recipe')


class RecipeSerializer(serializers.ModelSerializer):
	steps 		= serializers.StringRelatedField(many=True)
	ingredients = serializers.StringRelatedField(many=True)

	class Meta:
		model 	= Recipe
		fields 	= ['id', 'url', 'name', 'user', 'steps', 'ingredients']

