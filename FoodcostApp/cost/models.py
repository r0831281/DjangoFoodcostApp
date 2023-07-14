from django.db import models

# Create your models here.
class unit(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
    
class ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    unit = models.ForeignKey('unit', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def recipes(self):
        return recipe.objects.filter(ingredients__id=self.id)
    def price(self):
        return ingredientPrice.objects.filter(ingredient=self).order_by('-date')[0].price
    def priceHistory(self):
        return ingredientPrice.objects.filter(ingredient=self).order_by('-date')
    def totalPrice(self):
        return ingredientPrice.objects.filter(ingredient=self).order_by('-date')[0].price * recipe_ingredient.objects.filter(ingredient=self).order_by('-recipe__portions')[0].quantity

class ingredientPrice(models.Model):
    id = models.AutoField(primary_key=True)
    ingredient = models.ForeignKey('ingredient', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.ingredient.name + " - " + str(self.price) + " - " + str(self.date)

class recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField('ingredient', through='recipe_ingredient')
    description = models.TextField()
    portions = models.IntegerField()
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def totalPrice(self):
        total = 0
        for ingredient in self.ingredients.all():
            total += ingredient.totalPrice()
        return total
    
class recipe_ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey('recipe', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('ingredient', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self):
        return self.recipe.name + " - " + self.ingredient.name + " - " + str(self.quantity)
    def Amountprice(self):
        return self.ingredient.price * self.quantity