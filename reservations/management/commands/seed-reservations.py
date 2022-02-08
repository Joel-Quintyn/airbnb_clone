# Python base modules imports
import random
from datetime import datetime, timedelta

# Django aps/modules import
from django.core.management.base import BaseCommand
from django_seed import Seed

# Your apps import
import reservations.models as reservation_models
import users.models as user_models
import rooms.models as room_models


class Command(BaseCommand):

    help = "This command creates fake reservations"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many reservations you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")

        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()

        seeder = Seed.seeder()
        seeder.add_entity(
            reservation_models.Reservation,
            number,
            {
                "status": lambda x: random.choice(["pending", "confirmed", "canceled"]),
                "room": lambda x: random.choice(rooms),
                "guest": lambda x: random.choice(users),
                "check_in": lambda x: datetime.now()
                + timedelta(days=random.randint(0, 10)),
                "check_out": lambda x: datetime.now()
                + timedelta(days=random.randint(13, 35)),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} Reservation(s) Created!"))
