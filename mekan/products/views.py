from django.shortcuts import render
from .models import Product
from order.models import Item, Order, OrderStatus, item_count

# Create your views here.
def home_view(request):
    products = Product.objects.all()
    
    return render(request, 'home.html', {
        "products": products,
        "items_count": item_count(request),
    })