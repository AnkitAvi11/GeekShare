from django.contrib import admin

# Register your models here.
from .models import Note

class NoteAdmin(admin.ModelAdmin) : 
    list_display = ('id', 'title', 'description', 'note_file', 'user')
    list_display_links = ('id', 'title')

admin.site.register(Note, NoteAdmin)