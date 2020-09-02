from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    phone_number = PhoneNumberField(blank = True, max_length = 10)
    address = models.TextField(blank = True, max_length = 400)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name