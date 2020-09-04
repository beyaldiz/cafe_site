from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Customer

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(max_length = 30, required = True)
    last_name  = forms.CharField(max_length = 30, required = True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class CustomerInfoForm(forms.ModelForm):
    phone_number = forms.CharField(
        required = True,
        max_length = 10,
        min_length = 10,
        widget = forms.TextInput(attrs = {'type': 'tel', 'pattern': '[0-9]{10}', 'placeholder': 'ex. 5554443322', 'maxlength': '10'})
    )
    address = forms.CharField(required = True, max_length = 400)
    class Meta:
        model = Customer
        fields = ['phone_number', 'address']

