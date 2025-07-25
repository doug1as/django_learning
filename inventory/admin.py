from django.contrib import admin

# Register your models here.
from .models import Ingredients, MenuItems, RecipeRequirements, Purchases

admin.site.register(Ingredients)
admin.site.register(MenuItems)
admin.site.register(RecipeRequirements)
admin.site.register(Purchases)
# The admin interface will now allow you to manage Ingredients, MenuItems, RecipeRequirements, and Purchases models.
# You can add, edit, and delete entries for these models directly from the Django admin interface.
# This makes it easier to manage the inventory and menu items for your restaurant application.
# You can also customize the admin interface further by creating custom admin classes if needed.
# For example, you can define list displays, search fields, and filters for each model to enhance usability.
# This will help you efficiently manage the restaurant's inventory and menu items through the Django admin interface.
# Make sure to run the server and access the admin interface at /admin to see the changes.
# You can log in with the superuser account you created earlier to access the admin 