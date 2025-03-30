import random
from django.core.management.base import BaseCommand
from AuthenticationApp.models import CustomUser
from DashboardApp.models import Event, Lesson  # Import Event & Lesson models
from django.utils.timezone import now, timedelta
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help = "Seeds the database with fake events and lessons"

    def handle(self, *args, **options):
        users = list(CustomUser.objects.all())

        if not users:
            self.stdout.write(self.style.ERROR("❌ No users found. Create some users first!"))
            return

        self.seed_events(users)
        self.seed_lessons(users)

    def seed_events(self, users):
        """Generates fake events and assigns random organizers & attendees"""
        events = []
        for _ in range(10):  # Fixed 10 events
            start_date = now() + timedelta(days=random.randint(1, 30))
            end_date = start_date + timedelta(hours=random.randint(1, 48))

            event = Event(
                name=fake.sentence(nb_words=4),
                description=fake.paragraph(),
                start_date=start_date,
                end_date=end_date,
                location=fake.city(),
                poster="event.jpg",
                organizer=random.choice(users),
            )
            events.append(event)

        Event.objects.bulk_create(events)
        self.stdout.write(self.style.SUCCESS("✅ Created 80 events!"))

        # Assign attendees randomly
        for event in Event.objects.all():
            attendees = random.sample(users, random.randint(0, len(users)))
            event.attendees.add(*attendees)

    def seed_lessons(self, users):
        """Generates fake lessons and enrolls users"""
        difficulties = ["Beginner", "Intermediate", "Advanced"]
        categories = ["Technology", "Business", "Marketing", "Design", "Finance", "Education"]

        lessons = []
        for _ in range(80):  # Fixed 10 lessons
            lesson = Lesson(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(),
                content=fake.text(),
                category=random.choice(categories),
                difficulty=random.choice(difficulties),
                duration=random.randint(30, 180),  # Duration in minutes
                resources=fake.url() if random.choice([True, False]) else None,
            )
            lessons.append(lesson)

        Lesson.objects.bulk_create(lessons)
        self.stdout.write(self.style.SUCCESS("✅ Created 80 lessons!"))

        # Enroll users in lessons randomly
        for lesson in Lesson.objects.all():
            enrolled_users = random.sample(users, random.randint(0, len(users)))
            lesson.enrolled_users.add(*enrolled_users)
