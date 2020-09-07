from django.urls import path, re_path

from . import views

urlpatterns = [
    path('all/', views.view_notes, name='notes'),

    path('<str:branch>/', views.view_note_by_branch, name='branch')
]