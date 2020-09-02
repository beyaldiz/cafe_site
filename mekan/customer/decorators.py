from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user_only(redirect_to):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to)
            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator