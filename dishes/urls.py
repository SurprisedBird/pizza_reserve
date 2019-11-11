from django.urls import path
from . import views
from dishes.models import Dishes

urlpatterns = [
	path('dishes/', views.DishesTamplateView.as_view(), ),
	path('', views.DishesListView.as_view(), name='dishes_list'),
	path('ingredients/<int:pk>/edit', views.IngredientFormEddit.as_view()),
	path('dishes/<int:pk>/edit', views.DishesFormEddit.as_view())
]