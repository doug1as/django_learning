from django.db import models

## Menu Items
class MenuItems(models.Model):
  ## Define attributes here
  title = models.CharField(max_length=100, unique=True)
  price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

  """Magic method to define string representation of the model"""
  def __str__(self):
    return f"{self.title} - ${self.price}"

  """Meta class to define additional properties for the model"""
  class Meta:
    ordering = ['title']
    verbose_name_plural = "Menu Items"

# Create your models here.
class Ingredients(models.Model):
  ## Define attributes here
  name = models.CharField(max_length=100, unique=True)
  quantity = models.DecimalField(max_digits=5, decimal_places=2)
  unit = models.CharField(max_length=10)
  unit_price = models.DecimalField(max_digits=8, decimal_places=2)
  
  """Magic method to define string representation of the model"""
  def __str__(self):
    return f"{self.name} ({self.quantity} {self.unit}) - ${self.unit_price}"
  
  """Meta class to define additional properties for the model"""
  class Meta:
    ordering = ['name']
    verbose_name_plural = "Ingredients"
    unique_together = ('name', 'unit')

## Inventory Items
class RecipeRequirements(models.Model):
  ## Define attributes here
  menu_item = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
  ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
  quantity = models.DecimalField(max_digits=5, decimal_places=2)

  """Magic method to define string representation of the model"""
  def __str__(self):
    return f"{self.menu_item.title} requires {self.quantity} of {self.ingredient.name}"

## Purchases
class Purchases(models.Model):
  ## Define attributes here
  menu_item = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
  timestamp = models.DateTimeField(auto_now_add=True)

  """Magic method to define string representation of the model"""
  def __str__(self):
    return f"Purchase of {self.menu_item.title} on {self.timestamp}"