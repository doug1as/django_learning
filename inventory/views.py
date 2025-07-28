#############################
from django.shortcuts import render
from django.http import Http404
#############################

#############################
# Import the models below:
from .models import Ingredients, MenuItems, Purchases, RecipeRequirements
from .forms import MenuItemCreateForm, IngredientsCreateForm, PurchasesCreateForm, RecipeRequirementsCreateForm
#############################

#############################
# Import the generic views below:
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#############################

#############################
# Create your views here.
def homepage(request):
    try:
        cardapio = MenuItems.objects.all()
    except MenuItems.DoesNotExist:
        raise Http404()
    
    return render(request, 'inventory/home.html')
#############################

#############################
# List views for each model
class MenuItemList(ListView):
    model = MenuItems
    template_name = 'inventory/menu_items/menu_list.html'
    context_object_name = 'menu_items'

class IngredientsList(ListView):
    model = Ingredients
    template_name = 'inventory/ingredients/ingredients_list.html'
    context_object_name = 'ingredients'

class PurchasesList(ListView):
    model = Purchases
    template_name = 'inventory/purchases/purchase_list.html'
    context_object_name = 'purchases'

class RecipeRequirementsList(ListView):
    model = MenuItems
    template_name = 'inventory/recipe_requirements/recipe_requirement_list.html'
    context_object_name = 'recipe_requirements'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        grouped_recipes = []

        for menu_item in context["recipe_requirements"]:
            ingredients = menu_item.reciperequirements_set.select_related('ingredient')
            grouped_recipes.append({
                "menu_item": menu_item,
                "ingredients": ingredients
            })

        context["grouped_recipes"] = grouped_recipes
        return context
#############################

#############################
# Create views for each model
class MenuItemCreate(CreateView):
    model = MenuItems
    template_name = 'inventory/base_create_form.html'
    # or fields = ['title', 'price']
    form_class = MenuItemCreateForm
    #success_url = '/inventory/menu/list/'

class IngredientsCreate(CreateView):
    model = Ingredients
    template_name = 'inventory/base_create_form.html'
    fields = ['name', 'quantity', 'unit', 'unit_price']
    success_url = '/inventory/ingredients/'

class PurchasesCreate(CreateView):
    model = Purchases
    template_name = 'inventory/base_create_form.html'
    fields = ['timestamp', 'menu_item']
    success_url = '/inventory/purchases/'

class RecipeRequirementsCreate(CreateView):
    model = RecipeRequirements
    template_name = 'inventory/base_create_form.html'
    fields = ['menu_item', 'ingredient', 'quantity']
    success_url = '/inventory/recipe-requirements/'
#############################

#############################
# Update views for each model
class MenuItemUpdate(UpdateView):
    model = MenuItems
    template_name = 'inventory/base_create_form.html'
    fields = ['title', 'price']
    success_url = '/inventory/menu/list/'

class IngredientsUpdate(UpdateView):
    model = Ingredients
    template_name = 'inventory/base_create_form.html'
    fields = ['name', 'quantity', 'unit', 'unit_price']
    success_url = '/inventory/ingredients/'

class PurchasesUpdate(UpdateView):
    model = Purchases
    template_name = 'inventory/base_create_form.html'
    fields = ['timestamp', 'menu_item']
    success_url = '/inventory/purchases/'

class RecipeRequirementsUpdate(UpdateView):
    model = RecipeRequirements
    template_name = 'inventory/base_create_form.html'
    fields = ['menu_item', 'ingredient', 'quantity']
    success_url = '/inventory/recipe-requirements/'
#############################

#############################
# Delete views for each model
class MenuItemDelete(DeleteView):
    model = MenuItems
    template_name = 'inventory/menu_items/menu_delete_form.html'
    success_url = '/inventory/menu/'

class IngredientsDelete(DeleteView):
    model = Ingredients
    template_name = 'inventory/ingredients/ingredient_delete_form.html'
    success_url = '/inventory/ingredients/'

class PurchasesDelete(DeleteView):
    model = Purchases
    template_name = 'inventory/purchases/purchase_delete_form.html'
    success_url = '/inventory/purchases/'  

class RecipeRequirementsDelete(DeleteView):
    model = RecipeRequirements
    template_name = 'inventory/recipe_requirements/recipe_requirement_delete_form.html'
    success_url = '/inventory/recipe-requirements/'
#############################
# End of views
#############################
# This is the end of the views.py file.