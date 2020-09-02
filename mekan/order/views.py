from django.shortcuts import render
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import ItemForm
from .models import Item, Order, OrderStatus, item_count
from products.models import Product
from products.views import home_view

# Create your views here.

@login_required(login_url = 'login')
def item_view(request, pk):
    try:
        product_pk = Product.objects.get(pk = pk)
    except:
        raise Http404("Product with the index of " + str(pk) + " does not exist.")

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit = False)
            item.product = product_pk
            order_queryset = Order.objects.filter(customer = request.user.customer, status = OrderStatus.objects.get(status = 'on_cart'))
            if order_queryset.count() == 0:
                item.order = Order.objects.create(customer = request.user.customer, status = OrderStatus.objects.get(status = 'on_cart'))
            else:
                item.order = order_queryset[0]
            item.save()
            form.save_m2m()
            messages.info(request, 'Item added to the cart successfully!')
            
    product_pk_ingredients = product_pk.ingredients.all()
    form = ItemForm(initial = {'ingredients': product_pk_ingredients})
    form.fields['ingredients'].queryset = product_pk_ingredients
    context = {
        'form': form,
        'product': product_pk,
        'items_count': item_count(request),
    }
    return render(request, 'item.html', context)

@login_required(login_url = 'login')
def cart_view(request):
    context = {}
    total_price = 0
    order_queryset = Order.objects.filter(customer = request.user.customer, status = OrderStatus.objects.get(status = 'on_cart'))
    if order_queryset.count() != 0:
        item_queryset = Item.objects.filter(order = order_queryset[0])
        for item in item_queryset:
            total_price += item.quantity * item.product.price
        context['items'] = item_queryset
        context['total_price'] = total_price
    context['items_count'] = item_count(request)
    return render(request, 'cart.html', context)