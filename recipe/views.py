from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer


class RecipeViewSet(viewsets.ModelViewSet):
	queryset 			= Recipe.objects.all()
	serializer_class	= RecipeSerializer


class StepViewSet(viewsets.ModelViewSet):
	queryset 			= Step.objects.all()
	serializer_class=	 StepSerializer


class IngredientViewSet(viewsets.ModelViewSet):
	queryset 			= Ingredient.objects.all()
	serializer_class	= IngredientSerializer