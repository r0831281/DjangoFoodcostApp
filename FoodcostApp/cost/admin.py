from django.contrib import admin
from .models import recipe,ingredient,unit, recipe_ingredient, ingredientPrice
# Register your models here.

admin.site.register(recipe)
admin.site.register(ingredient)
admin.site.register(unit)
admin.site.register(recipe_ingredient)
admin.site.register(ingredientPrice)
admin.site.site_header = "Foodcost Admin"