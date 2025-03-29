from django.utils import timezone
from django.db import models
from AuthenticationApp.models import CustomUser

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='event_posters/', default='event.jpg')  # Store images in media/event_posters/
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    organizer = models.ForeignKey(CustomUser, related_name="organized_events", on_delete=models.CASCADE)
    attendees = models.ManyToManyField(CustomUser, related_name="events_attended", blank=True)

    class Meta:
        ordering = ['start_date'] # The meta tag allows us to add extra options. Like how we want the db to behave when queried
                                  # So the odering lets all events queried be ordered descending by date by default.
    def __str__(self):
        return self.name

    def is_ongoing(self):
        return self.start_date <= timezone.now() <= self.end_date

    def is_upcoming(self):
        return self.start_date > timezone.now()

    def is_past(self):
        return self.end_date < timezone.now()
    
class Lesson(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField(default="No content yet.")
    category = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    duration = models.IntegerField()
    resources = models.URLField(blank=True, null=True)
    enrolled_users = models.ManyToManyField(CustomUser, related_name="enrolled_lessons", blank=True)


    def __str__(self):
        return self.title

