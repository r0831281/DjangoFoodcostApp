from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("recipes", views.ShowRecipes, name="recipes"),
    path("recipes/<int:recipe_id>", views.recipeById, name="recipeById"),
    path("cost/recipes/<int:recipe_id>/delete", views.deleteRecipe, name="deleteRecipe"),
    path("recipes/<int:recipe_id>/edit", views.editRecipe, name="editRecipe"),
    path("ingredients", views.showIngredients, name="ingredients"),
    path("ingredients/<int:ingredient_id>", views.ingredientById, name="ingredientById"),
]
