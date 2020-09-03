from django.contrib import admin

# Register your models here.
from .models import UserProfile, Notification

#   admin setting for the view on the admin
class UserprofileAdmin(admin.ModelAdmin) : 
    list_display = ('id', 'user', 'bio', 'website', 'location')
    list_display_links = ('id', 'user')

class NotificationAdmin(admin.ModelAdmin) : 
    list_display = ('id', 'user', 'title')
    list_display_links = ('id', 'user')

admin.site.register(UserProfile, UserprofileAdmin)
admin.site.register(Notification, NotificationAdmin)