from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Note

def view_notes(request):
    notes = Note.objects.all().order_by('-created_on')
    return render(
        request, 
        'notes/notes.html',
        {"notes" : notes}
    )

def view_note_by_branch(request, branch) : 
    return render(
        request, 
        'notes/notes.html'
    )