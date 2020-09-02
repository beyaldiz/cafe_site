from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Customer
from phonenumber_field.formfields import PhoneNumberField

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(max_length = 30, required = True)
    last_name  = forms.CharField(max_length = 30, required = True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class CustomerInfoForm(forms.ModelForm):
    phone_number = PhoneNumberField(required = True)
    address = forms.CharField(required = True)
    class Meta:
        model = Customer
        fields = ['phone_number', 'address']

