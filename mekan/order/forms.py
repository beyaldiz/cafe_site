from django import forms
from products.models import Product, Ingredient
from order.models import Item, Order

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['ingredients', 'quantity'] 
        widgets = {
            'ingredients': forms.CheckboxSelectMultiple(),
            'quantity': forms.NumberInput(attrs = {'min': 1, 'max': 100})
        }