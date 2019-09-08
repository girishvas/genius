from django.contrib import admin
from . import models
from .models import *


class RecipeAdmin(admin.ModelAdmin):
	list_display = ('name', 'user', 'createdOn')
	list_filter = ['createdOn']
	search_fields = ['name', 'user__email']

admin.site.register(Recipe, RecipeAdmin)


class StepAdmin(admin.ModelAdmin):
	list_display = ('step', 'recipe', 'createdOn')
	list_filter = ['createdOn']
	search_fields = ['name']

admin.site.register(Step, StepAdmin)


class IngredientAdmin(admin.ModelAdmin):
	list_display = ('ingredient', 'recipe', 'createdOn')
	list_filter = ['createdOn']
	search_fields = ['name']

admin.site.register(Ingredient, IngredientAdmin)
