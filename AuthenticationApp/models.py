from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    MEMBERSHIP_CHOICES = [
       ('Community', 'Community Member'),
        ('Key Access', 'Key Access Member'),
        ('Workspace', 'Creative Workspace Member'),
    ]

    
    phonenumber = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    membership = models.CharField(max_length=20, choices=MEMBERSHIP_CHOICES, default='Community')
    interest = models.CharField(max_length=255, default='Technology')
    firstname = models.CharField(max_length=20, default='Guest')
    lastname = models.CharField(max_length=20, default="-")
    approvedmember = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now())
    security_question = models.CharField(max_length=255, blank=True, null=True)
    security_answer = models.CharField(max_length=255, blank=True, null=True)
    
    email = models.EmailField(unique=True)
    
    def save(self, *args, **kwargs):
        if not self.username:  # If username is empty, generate from email
            base_username = self.email.split("@")[0]
            unique_username = base_username
            counter = 1
            
            # Ensure the username is unique
            while CustomUser.objects.filter(username=unique_username).exists():
                unique_username = f"{base_username}{counter}"
                counter += 1

            self.username = unique_username

        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.username
