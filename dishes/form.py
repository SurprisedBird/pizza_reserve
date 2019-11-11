from django import forms 
from django.forms import ModelForm
from dishes.models import Dishes, Ingredient
		
class IngredientForm(ModelForm):

	class Meta():
		model = Ingredient
		fields = ['name', 'price']

class DishesForm(ModelForm):

	class Meta():
		model = Dishes
		fields = ['name', 'price', 'ingridients']