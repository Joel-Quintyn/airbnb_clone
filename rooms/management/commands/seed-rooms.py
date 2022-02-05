import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
import rooms.models as room_models
import users.models as user_models


class Command(BaseCommand):

    help = "This command creates rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many rooms you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")

        users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()

        seeder = Seed.seeder(locale="en_US")
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.sentence(nb_words=4),
                "host": lambda x: random.choice(users),
                "room_type": lambda x: random.choice(room_types),
                "price": lambda x: random.randint(30, 300),
                "guests": lambda x: random.randint(1, 15),
                "beds": lambda x: random.randint(1, 10),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        created_rooms = seeder.execute()
        created_rooms = flatten(created_rooms.values())
        # print(created_rooms)
        for room in created_rooms:
            room = room_models.Room.objects.get(pk=room)
            for i in range(3, random.randint(10, 15)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(nb_words=5),
                    room=room,
                    file=f"/room_photos/{random.randint(1, 31)}.webp",
                )

            for a in amenities:
                magic_number = random.randint(0, 40)
                if magic_number % 2 == 0:
                    room.amenities.add(a)

            for f in facilities:
                magic_number = random.randint(0, 40)
                if magic_number % 2 == 0:
                    room.facilities.add(f)

            for r in rules:
                magic_number = random.randint(0, 40)
                if magic_number % 2 == 0:
                    room.house_rules.add(r)

        self.stdout.write(self.style.SUCCESS(f"{number} Room(s) Created!"))
