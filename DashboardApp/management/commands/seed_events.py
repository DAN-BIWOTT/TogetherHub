import random
import os
from django.core.management.base import BaseCommand
from django.utils.timezone import now, timedelta
from faker import Faker
from AuthenticationApp.models import CustomUser
from DashboardApp.models import Event

fake = Faker()

class Command(BaseCommand):
    help = "Seeds the database with fake events"

    def handle(self, *args, **options):
        users = list(CustomUser.objects.all())

        if not users:
            self.stdout.write(self.style.ERROR("❌ No users found. Create some users first!"))
            return

        self.seed_events(users)

    def seed_events(self, users):
        events = []
        image_files = [f"event_posters/1 ({i}).jpg" for i in range(1, 13)]  # List of image files

        for _ in range(80):  # Generate 10 events
            start_date = now() + timedelta(days=random.randint(1, 30))
            end_date = start_date + timedelta(hours=random.randint(1, 48))

            event = Event(
                name=fake.sentence(nb_words=4),
                description=fake.paragraph(),
                start_date=start_date,
                end_date=end_date,
                location=fake.city(),
                poster=random.choice(image_files),  # Randomly select a poster
                organizer=random.choice(users),
            )
            events.append(event)

        Event.objects.bulk_create(events)
        self.stdout.write(self.style.SUCCESS("✅ Created 80 events!"))

        # Assign attendees randomly
        for event in Event.objects.all():
            attendees = random.sample(users, random.randint(0, len(users)))
            event.attendees.add(*attendees)
