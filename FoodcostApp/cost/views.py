from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import recipe,ingredient,unit, recipe_ingredient
# Create your views here.

def index(request):
    '''return index template'''
    return render(request, "cost/index.html")

def ShowRecipes(request):
    '''return recipes template'''
    recipes = recipe.objects.all()
    return render(request, "cost/recipes.html", {"recipes":recipes})

def recipeById(request, recipe_id):
    '''return recipe template'''
    recipe_obj = recipe.objects.get(id=recipe_id)
    ingredients = recipe_ingredient.objects.filter(recipe=recipe_obj)
    return render(request, "cost/recipeById.html", {"recipe":recipe_obj, "ingredients":ingredients})

def deleteRecipe(request, recipe_id):
    '''delete recipe'''
    recipe.objects.get(id=recipe_id).delete()
    return HttpResponseRedirect("/recipes")

def editRecipe(request, recipe_id):
    '''edit recipe'''
    recipe_obj = recipe.objects.get(id=recipe_id)
    ingredients = recipe_ingredient.objects.filter(recipe=recipe_obj)
    return render(request, "cost/editRecipe.html", {"recipe":recipe_obj, "ingredients":ingredients})


def showIngredients(request):
    '''return ingredients template'''
    ingredients = ingredient.objects.all()
    return render(request, "cost/ingredients.html", {"ingredients":ingredients})

def ingredientById(request, ingredient_id):
    '''return ingredient template'''
    ingredient_obj = ingredient.objects.get(id=ingredient_id)
    recipes = recipe.objects.filter(ingredients__id=ingredient_id)
    return render(request, "cost/ingredientById.html", {"ingredient":ingredient_obj, "recipes":recipes})
