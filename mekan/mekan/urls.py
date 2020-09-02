"""mekan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from products.views import home_view 
from order.views import item_view, cart_view
from customer.views import user_register_view, user_login_view, user_logout, customer_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name = 'home'),
    path('item/<int:pk>', item_view, name = 'item'),
    path('register', user_register_view, name = 'register'),
    path('login', user_login_view, name = 'login'),
    path('logout', user_logout, name = 'logout'),
    path('cart', cart_view, name = 'cart'),
    path('customer', customer_view, name = 'customer_view')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)