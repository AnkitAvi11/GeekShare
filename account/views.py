from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .decorators import isAuthenticated
import re 

@isAuthenticated
def loginUser(request) : 
    context = {
        "next" : "/"
    }
    if request.method == 'POST' : 
        return JsonResponse(request.POST)
    else : 
        return render(request, 'auth/login.html')


def isEmail(email) : 
    regex = re.compile('^([a-zA-Z0-9\-\_\.])+\@([a-zA-Z0-9\-\_\.])+\.([a-zA-Z0-9]{2,4})$')
    return regex.match(email)

@isAuthenticated
def register(request) : 
    context = {}
    from django.core.mail import send_mail

    if request.method == "POST" : 
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if isEmail(email) : 
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists(): 
                messages.error(request, 'User with that credentials already exists')
                return render(request, 'auth/signup.html', {
                    "fname" : first_name,
                    "lname" : last_name,
                    "username" : username,
                    "email" : email
                })
            else : 
                User.objects.create_user(first_name=first_name, last_name=last_name, username=username,password=password, email=email)
                send_mail(
                    'User registeration successul',
                    'You have successfully registered on our website.',
                    'GeekShareTeam@geekshare',
                    [email],
                    fail_silently=False
                )
                messages.success(request,'User registeration successful')
                return redirect('/account/login/')
        else : 
            messages.error(request, 'Invalid email address')
            return render(request, 'auth/signup.html', {
                "fname" : first_name,
                "lname" : last_name,
                "username" : username,
                "email" : email
            })
    else : 
        return render(request, 'auth/signup.html', context)

