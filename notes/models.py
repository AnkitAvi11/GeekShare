from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Note(models.Model) : 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(blank=False, null=False, max_length=300)
    description = models.TextField(blank=True, null=True)
    note_image = models.ImageField(upload_to='notes/%Y/%m/', blank=True, null=True)
    note_file = models.FileField(upload_to='notes/%Y/%m/', blank=False, null=False)
    tag_choices = [
        ('CS', 'Computer Science'),
        ('MECH', 'Mechanical Engineering'),
        ('EEE', 'Electrical'),
        ('IT', 'Information Technology'),
        ('COM', 'Communication Technology'),
        ('PROG', 'Programming'),
        ('OT', 'Other')
    ]

    branch = models.CharField(
        max_length = 4,
        choices = tag_choices,
        default = 'OT'
    )

    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title

