import random
from django.core.management.base import BaseCommand
from django.utils.timezone import now, timedelta
from faker import Faker
from AuthenticationApp.models import CustomUser
from DashboardApp.models import Lesson

fake = Faker()

class Command(BaseCommand):
    help = "Seeds the database with fake lessons"

    def handle(self, *args, **options):
        users = list(CustomUser.objects.all())

        if not users:
            self.stdout.write(self.style.ERROR("❌ No users found. Create some users first!"))
            return

        self.seed_lessons(users)

    def seed_lessons(self, users):
        """Generates fake lessons and assigns valid creators"""
        if not users:
            self.stdout.write(self.style.ERROR("❌ No users found. Cannot create lessons."))
            return

        difficulties = ["Beginner", "Intermediate", "Advanced"]
        categories = ["Technology", "Business", "Marketing", "Design", "Finance", "Education"]

        lessons = []
        for _ in range(80):
            lesson = Lesson(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(),
                content=fake.text(),
                category=random.choice(categories),
                difficulty=random.choice(difficulties),
                duration=random.randint(30, 180),  # Duration in minutes
                resources=fake.url() if random.choice([True, False]) else None,
                creator=random.choice(users),  # Ensure a valid user is assigned
            )
            lessons.append(lesson)

        Lesson.objects.bulk_create(lessons)
        self.stdout.write(self.style.SUCCESS("✅ Created 80 lessons!"))

        # Enroll users in lessons randomly
        for lesson in Lesson.objects.all():
            enrolled_users = random.sample(users, random.randint(0, len(users)))
            lesson.enrolled_users.add(*enrolled_users)
