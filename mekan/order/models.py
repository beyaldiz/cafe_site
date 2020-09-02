from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from products.models import Product, Ingredient
from customer.models import Customer

# Create your models here.
class OrderStatus(models.Model):
    status = models.CharField(max_length = 32)

    def __str__(self):
        return self.status

class Order(models.Model):
    customer = models.ForeignKey(Customer, null = True, on_delete = models.CASCADE)
    status = models.ForeignKey(OrderStatus, null = True, on_delete = models.CASCADE)
    note = models.TextField(blank = True, max_length = 200)

    def __str__(self):
        return "%s %s's %s orders" % (self.customer.user.first_name, self.customer.user.last_name, self.status)

class Item(models.Model):
    product = models.ForeignKey(Product, null = True, on_delete = models.CASCADE)
    order = models.ForeignKey(Order, null = True, on_delete = models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)
    quantity = models.IntegerField(default = 1, validators = [MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return "%s (%s)" % (str(self.order), str(self.product))

def item_count(request):
    items_count = 0
    if request.user.is_authenticated:
        order_queryset = Order.objects.filter(customer = request.user.customer, status = OrderStatus.objects.get(status = 'on_cart'))
        if order_queryset.count() != 0:
            items_count = Item.objects.filter(order = order_queryset[0]).count()
    return items_count
