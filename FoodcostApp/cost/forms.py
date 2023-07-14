from django import forms
from .models import ingredient, unit

class loginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class addRecipeForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    portions = forms.IntegerField()
    category = forms.CharField(max_length=100)

class addIngredientForm(forms.Form):
    name = forms.CharField(max_length=100)
    unit = forms.ModelChoiceField(queryset=unit.objects.all())

class addIngredientPriceForm(forms.Form):
    ingredient = forms.ModelChoiceField(queryset=ingredient.objects.all())
    price = forms.DecimalField
    date = forms.DateField