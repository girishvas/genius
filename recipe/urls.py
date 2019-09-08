from rest_framework import routers
from recipe import views
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'recipes', views.RecipeViewSet)
router.register(r'steps', views.StepViewSet)
router.register(r'ingredients', views.IngredientViewSet)


urlpatterns = [
	path('', include(router.urls))
]