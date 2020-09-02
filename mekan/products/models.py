from django.db import models

# Create your models here.

class Ingredient(models.Model):
    title = models.CharField(max_length = 32)

    def __str__(self):
        return self.title
    

class Product(models.Model):
    title = models.CharField(max_length = 32)
    picture = models.ImageField(blank = True)
    description = models.TextField(max_length = 72)
    price = models.DecimalField(max_digits = 9, decimal_places = 2)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.title