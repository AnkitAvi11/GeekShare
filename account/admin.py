from django.contrib import admin

# Register your models here.
from .models import UserProfile

#   admin setting for the view on the admin
class UserprofileAdmin(admin.ModelAdmin) : 
    list_display = ('id', 'user', 'bio', 'website', 'location')
    list_display_links = ('id', 'user')


admin.site.register(UserProfile, UserprofileAdmin)