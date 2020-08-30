from django.urls import path, re_path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('signup/', views.register, name='signup'),

   #    password resetting views
   path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

   path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

   path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

   path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')

]