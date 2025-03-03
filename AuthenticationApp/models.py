from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    MEMBERSHIP_CHOICES = [
        ('Basic', 'Basic'),
        ('Premium', 'Premium'),
        ('Enterprise', 'Enterprise'),
    ]

    INTEREST_CHOICES = [
        ('Technology', 'Technology'),
        ('Design', 'Design'),
        ('Business', 'Business'),
    ]

    membership = models.CharField(max_length=20, choices=MEMBERSHIP_CHOICES, default='Basic')
    interest = models.CharField(max_length=20, choices=INTEREST_CHOICES, default='Technology')
    firstname = models.CharField(max_length=20, default='Guest')
    lastname = models.CharField(max_length=20, default="-")

    def __str__(self):
        return self.username
