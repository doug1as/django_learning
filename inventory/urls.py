from django.urls import path

from . import views

urlpatterns = [
   # List views for each model
   path('home/', views.homepage, name='homepage'),

   # List views for each model
   path('menu/list/', views.MenuItemList.as_view(), name='menu_items'),
   path('ingredients/list/', views.IngredientsList.as_view(), name='ingredients'),
   path('purchases/list/', views.PurchasesList.as_view(), name='purchases'),
   path('recipe-requirements/list/', views.RecipeRequirementsList.as_view(), name='recipe_requirements'),

   # Create views for each model
   path('menu/create/', views.MenuItemCreate.as_view(), name='menu_create'),
   path('ingredients/create/', views.IngredientsCreate.as_view(), name='ingredients_create'),
   path('purchases/create/', views.PurchasesCreate.as_view(), name='purchases_create'),
   path('recipe-requirements/create/', views.RecipeRequirementsCreate.as_view(), name='recipe_requirements_create'),

   # Update views for each model
   path('menu/update/<int:pk>/', views.MenuItemUpdate.as_view(), name='menu_item_update'),
   path('ingredients/update/<int:pk>/', views.IngredientsUpdate.as_view(), name='ingredients_update'),
   path('purchases/update/<int:pk>/', views.PurchasesUpdate.as_view(), name='purchases_update'),
   path('recipe-requirements/update/<int:pk>/', views.RecipeRequirementsUpdate.as_view(), name='recipe_requirements_update'),
   
   # Delete views for each model
   path('menu/delete/<int:pk>/', views.MenuItemDelete.as_view(), name='menu_item_delete'),
   path('ingredients/delete/<int:pk>/', views.IngredientsDelete.as_view(), name='ingredients_delete'),
   path('purchases/delete/<int:pk>/', views.PurchasesDelete.as_view(), name='purchases_delete'),
   path('recipe-requirements/delete/<int:pk>/', views.RecipeRequirementsDelete.as_view(), name='recipe_requirements_delete'),
]