from django.urls import path

from . import views

urlpatterns = [
   path('home/', views.homepage, name='homepage'),
   path('ingredients/', views.IngredientsListView.as_view(), name='ingredients'),
   path('menu/', views.MenuItemListView.as_view(), name='menu'),
   path('purchases/', views.PurchasesListView.as_view(), name='purchases'),
   path('recipe-requirements/', views.RecipeRequirementsListView.as_view(), name='recipe_requirements'),
]