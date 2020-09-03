from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save

class UserProfile(models.Model) : 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to="images/%Y/%m", default='default.png')
    location = models.CharField(max_length=200)
    website = models.URLField(blank=True, null=True)
    joined_on = models.DateTimeField(default=timezone.now())

    def __str__(self) : 
        return self.user.username

    #   overriding the save method
    def save(self, *args, **kwargs) : 
        try : 
            this = UserProfile.objects.get(id=self.id)
            if this.profile_image != self.profile_image and this.profile_image != 'default.png': 
                this.profile_image.delete()

        except : 
            pass
    
        return super().save(*args, **kwargs)

    
    #   overriding the delete method
    def delete(self, *args, **kwargs) : 
        self.profile_image.delete()
        return super().delete(*args, **kwargs)

    #   function to get the total number of Notifications
    def countNotifications(self) : 
        total = Notification.objects.filter(user=self.user).exclude(is_read=True).count()
        print("total = ", total)
        return total

    #    method to get the notifications
    def getNotifications(self) : 
        return Notification.objects.filter(user=self.user).exclude(is_read=True)


def createProfile(sender, **kwargs) : 
    if kwargs['created'] : 
        UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(createProfile, sender=User)

#   model for notification for the user to track comments or likes on the posts
class Notification(models.Model) : 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, blank=False, null=False)
    link = models.CharField(max_length=200)
    time = models.DateTimeField(default=timezone.now())
    is_read = models.BooleanField(default=False)    

    def __str__(self) : 
        return self.title

    

