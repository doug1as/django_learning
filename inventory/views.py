#############################
from django.shortcuts import render

#############################
# Import the models below:
from .models import Ingredients, MenuItems, Purchases, RecipeRequirements

#############################
# Import the generic views below:
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


#############################
# Create your views here.
def homepage(request):
    return render(request, 'inventory/home.html')

# List views for each model
class IngredientsListView(ListView):
    model = Ingredients
    template_name = 'inventory/ingredients/ingredients_list.html'
    context_object_name = 'ingredients'

class MenuItemListView(ListView):
    model = MenuItems
    template_name = 'inventory/menu_items/menu_list.html'
    context_object_name = 'menu_items'

class PurchasesListView(ListView):
    model = Purchases
    template_name = 'inventory/purchases/purchases_list.html'
    context_object_name = 'purchases'

class RecipeRequirementsListView(ListView):
    model = RecipeRequirements
    template_name = 'inventory/recipe_requirements/recipe_requirements_list.html'
    context_object_name = 'recipe_requirements'


#############################
# Create views for each model
class IngredientsCreateView(CreateView):
    model = Ingredients
    template_name = 'inventory/ingredients/ingredient_form.html'
    fields = ['name', 'quantity', 'unit', 'unit_price']
    success_url = '/ingredients/'