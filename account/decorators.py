from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def isAuthenticated(view_function) : 
    def wrapper_function(request, *args, **kwargs) : 
        if request.user.is_authenticated : 
            redirect('/')

        view_function(request, *args, **kwargs)

    return wrapper_function