from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, JsonResponse

def home(request) :    
    return render(request, 'index.html')
