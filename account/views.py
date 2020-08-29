from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, JsonResponse

from .decorators import isAuthenticated

@isAuthenticated
def loginUser(request) : 
    if request.method == 'POST' : 
        return JsonResponse(request.POST)
    else : 
        return HttpResponse('Login')
