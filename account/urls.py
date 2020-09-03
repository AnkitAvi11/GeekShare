from django.urls import path, re_path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('signup/', views.register, name='signup'),
    path('setting/', views.setting, name='setting'),

   #    password resetting views
   path('password_reset/', auth_views.PasswordResetView.as_view(template_name='auth/password_reset.html'), name='password_reset'),

   path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'), name='password_reset_done'),

   path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='auth/reset.html'), name='password_reset_confirm'),

   path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='auth/reset_done.html'), name='password_reset_complete')

]