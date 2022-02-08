import random
from django.core.management.base import BaseCommand
from django_seed import Seed
import reviews.models as review_models
import users.models as user_models
import rooms.models as room_models


class Command(BaseCommand):

    help = "This command creates fake reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many reviews you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")

        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()

        seeder = Seed.seeder()
        seeder.add_entity(
            review_models.Review,
            number,
            {
                # "review": lambda x: seeder.faker.sentence(),
                "cleanliness_rating": lambda x: random.randint(1, 5),
                "accuracy_rating": lambda x: random.randint(1, 5),
                "communication_rating": lambda x: random.randint(1, 5),
                "location_rating": lambda x: random.randint(1, 5),
                "check_in_rating": lambda x: random.randint(1, 5),
                "value_rating": lambda x: random.randint(1, 5),
                "user": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} Reviews Created!"))
