import random, datetime
from django.core.management.base import BaseCommand
from AuthenticationApp.models import CustomUser
from django.utils.timezone import now

class Command(BaseCommand):
    help = "Seeds the database with an admin user"

    def handle(self, *args, **options):
        
        users = [ 
            CustomUser(
            username = f"user{i+1}_{random.randint(1, 100)}",
            phonenumber=f"+44 709 124 123 1{i+1}",
            location=f"CB{i}",
            occupation="",
            skills="",
            birthdate=datetime.date(1990 + i, random.randint(1,12), random.randint(1,28)),
            membership="Community",
            interest="",
            firstname=f"userf{i}",
            lastname=f"userl{i}",
            approvedmember=bool(random.getrandbits(1) ), #get random true or false values
            created_at=datetime.date(2025, random.randint(1,12), random.randint(1,28)),
            email=f"user{i}@gmail.com",
            ) for i in range(10)
         ]
        CustomUser.objects.bulk_create(users)

        if not CustomUser.objects.filter(email="admin@gmail.com").exists():
            CustomUser.objects.create_superuser(
                email="admin@gmail.com",
                password="123",
                membership="admin",
                username="admin",
<<<<<<< HEAD
                approvedmember=True,
=======
                approvedmember=True
>>>>>>> 5559b8e76a04c5b04b7d7f70070990ab04704720
            )
            self.stdout.write(self.style.SUCCESS("✅ Superuser created successfully!"))
        else:
            self.stdout.write(self.style.WARNING("⚠️ Admin user already exists."))
