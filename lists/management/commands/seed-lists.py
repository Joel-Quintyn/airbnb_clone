import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
import lists.models as list_models
import users.models as user_models
import rooms.models as room_models


class Command(BaseCommand):

    help = "This command creates fake lists"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many lists you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")

        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()

        seeder = Seed.seeder()
        seeder.add_entity(
            list_models.List,
            number,
            {
                "name": lambda x: seeder.faker.sentence(nb_words=3),
                "user": lambda x: random.choice(users),
            },
        )
        created_lists = seeder.execute()
        created_lists = flatten(created_lists.values())
        # print(created_lists)
        for pk in created_lists:
            for i in range(3, random.randint(4, 9)):
                current_list = list_models.List.objects.get(pk=pk)
                current_list.rooms.add(random.choice(rooms))
                
        self.stdout.write(self.style.SUCCESS(f"{number} Lists Created!"))
