from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    MEMBERSHIP_CHOICES = [
       ('community', 'Community Member'),
        ('key_access', 'Key Access Member'),
        ('workspace', 'Creative Workspace Member'),
    ]

    INTEREST_CHOICES = [
        ('Technology', 'Technology'),
        ('Design', 'Design'),
        ('Business', 'Business'),
    ]
    phonenumber = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    membership = models.CharField(max_length=20, choices=MEMBERSHIP_CHOICES, default='community')
    interest = models.CharField(max_length=20, choices=INTEREST_CHOICES, default='Technology')
    firstname = models.CharField(max_length=20, default='Guest')
    lastname = models.CharField(max_length=20, default="-")

    def __str__(self):
        return self.username
