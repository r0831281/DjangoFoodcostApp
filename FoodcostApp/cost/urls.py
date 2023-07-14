from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("recipes", views.ShowRecipes, name="recipes"),
    path("recipes/<int:recipe_id>", views.recipeById, name="recipeById"),
    path("cost/recipes/<int:recipe_id>/delete", views.deleteRecipe, name="deleteRecipe"),
    path("cost/recipes/<int:recipe_id>/edit", views.editRecipe, name="editRecipe"),
    path("ingredients", views.showIngredients, name="ingredients"),
    path("ingredients/<int:ingredient_id>", views.ingredientById, name="ingredientById"),
    path("ingredients/<int:ingredient_id>/edit", views.editIngredient, name="editIngredient"),
    path("ingredients/<int:ingredient_id>/delete", views.deleteIngredient, name="deleteIngredient"),
    path("cost/recipes/create", views.addRecipe, name="addRecipe"),
    path("cost/ingredients/add", views.addIngredient , name="addIngredient"),
    path("cost/ingredients/<int:ingredient_id>/addPrice", views.addIngredientPrice, name="addPriceToIngredient"),
    path("costingredients/units" , views.showUnits, name="showUnits"),
    path("signUp", views.signUp, name="signUp"),
    path("signIn", views.signIn, name="signIn"),
]
