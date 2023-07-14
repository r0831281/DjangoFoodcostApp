from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import recipe,ingredient,unit, recipe_ingredient
from .forms import loginForm, addRecipeForm, addIngredientForm, addIngredientPriceForm
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

def editIngredient(request, ingredient_id):
    '''edit ingredient'''
    ingredient_obj = ingredient.objects.get(id=ingredient_id)
    return render(request, "cost/editIngredient.html", {"ingredient":ingredient_obj})

def deleteIngredient(request, ingredient_id):
    '''delete ingredient'''
    ingredient.objects.get(id=ingredient_id).delete()
    return HttpResponseRedirect("/ingredients")

def signIn(request):
    '''return sign in template'''
    return render(request, "cost/signIn.html", {"form":loginForm()})

def addRecipe(request):
    '''add recipe'''
    if request.method == "POST":
        form = addRecipeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            description = form.cleaned_data["description"]
            portions = form.cleaned_data["portions"]
            category = form.cleaned_data["category"]
            ingredients = request.POST.getlist("ingredients")
            new = recipe.objects.create(name=name, description=description, portions=portions, category=category)
            for i in ingredients:
                recipe_ingredient.objects.create(recipe=recipe.objects.get(name=new.name), ingredient=i)
            return HttpResponseRedirect("/recipes")
    else:
        '''return with all ingredients'''
        ingredients = ingredient.objects.all()
        return render(request, "cost/addRecipe.html", {"form":addRecipeForm(), "ingredients":ingredients})



def addIngredient(request):
    '''add ingredient'''
    if request.method == "POST":
        form = addIngredientForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            unit = form.cleaned_data["unit"]
            ingredient.objects.create(name=name, unit=unit)
            return HttpResponseRedirect("/ingredients")
    else:
        return render(request, "cost/createIngredient.html", {"form":addIngredientForm()})

def addIngredientPrice(request):
    '''add ingredient price'''
    return render(request, "cost/addIngredientPrice.html", {"form":addIngredientPriceForm()})

def showUnits(request):
    '''return unit template'''
    return render(request, "cost/ingredients/unit.html")


def signUp(request):
    '''return sign up template'''
    return render(request, "cost/signUp.html",
    {"form":loginForm()})

