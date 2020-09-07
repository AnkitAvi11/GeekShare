from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth.decorators import login_required


def view_notes(request):
    return HttpResponse('asdad')
