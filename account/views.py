from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, JsonResponse

from .decorators import isAuthenticated

@isAuthenticated
def loginUser(request) : 
    context = {
        "next" : "/"
    }
    if request.method == 'POST' : 
        return JsonResponse(request.POST)
    else : 
        return render(request, 'auth/login.html')

@isAuthenticated
def register(request) : 
    context = {}
    if request.method == "POST" : 
        pass
    else : 
        return render(request, 'auth/signup.html', context)

