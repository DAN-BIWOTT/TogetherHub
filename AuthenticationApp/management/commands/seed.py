import random
import datetime
from django.core.management.base import BaseCommand
from AuthenticationApp.models import CustomUser
from django.utils.timezone import now
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help = "Seeds the database with fake users and an admin user"

    def handle(self, *args, **options):
        MEMBERSHIP_CHOICES = [choice[0] for choice in CustomUser.MEMBERSHIP_CHOICES]
        INTEREST_CHOICES = [choice[0] for choice in CustomUser.INTEREST_CHOICES]

        users = []
        for i in range(100):
            birthdate = fake.date_of_birth(minimum_age=18, maximum_age=65)
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = f"user{i}_{random.randint(100, 999)}@gmail.com"
            username = email.split("@")[0]

            users.append(CustomUser(
                username=username,
                phonenumber=fake.phone_number(),
                location=fake.city(),
                occupation=fake.job(),
                skills=", ".join(fake.words(nb=5)),
                birthdate=birthdate,
                membership=random.choice(MEMBERSHIP_CHOICES),
                interest=random.choice(INTEREST_CHOICES),
                firstname=first_name,
                lastname=last_name,
                approvedmember=random.choice([True, False]),
                created_at=now(),
                email=email,
            ))

        CustomUser.objects.bulk_create(users)
        self.stdout.write(self.style.SUCCESS("✅ Successfully created 100 users!"))

        # Ensure the admin user exists
        if not CustomUser.objects.filter(email="admin@gmail.com").exists():
            CustomUser.objects.create_superuser(
                email="admin@gmail.com",
                password="123",
                membership="admin",
                username="admin",
                approvedmember=True,
            )
            self.stdout.write(self.style.SUCCESS("✅ Superuser created successfully!"))
        else:
            self.stdout.write(self.style.WARNING("⚠️ Admin user already exists."))
