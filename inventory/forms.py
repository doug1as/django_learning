#############################
from django import forms
from.models import MenuItems, Ingredients, Purchases, RecipeRequirements
#############################

#############################
# Create forms for each model
class MenuItemCreateForm(forms.ModelForm):
    class Meta:
        model = MenuItems
        # Or fields = ['title', 'price'] if you want to specify fields explicitly
        fields = '__all__'

class IngredientsCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        # Or fields = ['name', 'quantity', 'unit', 'unit_price' if you want to specify fields explicitly]
        fields = '__all__'

class PurchasesCreateForm(forms.ModelForm):
    class Meta:
        model = Purchases
        # Or fields = ['timestamp', 'menu_item'] if you want to specify fields explicitly
        fields = '__all__'

class RecipeRequirementsCreateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirements
        # Or fields = ['menu_item', 'ingredient', 'quantity'] if you want to specify fields explicitly
        fields = '__all__'
#############################

#############################