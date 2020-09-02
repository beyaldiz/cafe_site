from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Customer
from .forms import UserRegisterForm, CustomerInfoForm
from .decorators import unauthenticated_user_only

# Create your views here.
@unauthenticated_user_only(redirect_to = 'home')
def user_register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Customer.objects.create(
                user = user,
            )
            messages.success(request, 'Account registered!')
            return redirect('login')
        else:
            messages.info(request, 'An error occured! Check the entered information!')

    form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@unauthenticated_user_only(redirect_to = 'home')
def user_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect!')
        
    return render(request, 'login.html', {})

def user_logout(request):
    logout(request)
    return redirect('home')

def customer_view(request):
    form = CustomerInfoForm()
    return render(request, 'customer.html',{'form': form})