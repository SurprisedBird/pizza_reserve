from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from dishes.models import Dishes, Drink, Discount, Size, Ingredient
from dishes.form import IngredientForm, DishesForm

# Create your views here.
class DishesListView(ListView):
	model = Dishes
	template_name = 'dishes_list.html'

#	def get_queryset(self, *args, **kwargs):

class DishesTamplateView(TemplateView):
	template_name = 'dishes.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['name'] = Dishes.objects.all()[:5]
		return context

class IngredientFormEddit(UpdateView):
	form_class = IngredientForm
	model = Ingredient
	success_url = "/"
	template_name = 'dish_form.html'

class DishesFormEddit(UpdateView):
	form_class = DishesForm
	model = Dishes
	success_url = "/"
	template_name = 'dish_form.html'