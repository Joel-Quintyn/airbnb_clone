from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    help = "This command creates all facilities."

    def handle(self, *args, **options):
        facilities = [
            "Private Entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Free Parking",
            "Gym",
            "Security",
        ]

        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} Facilities Created!"))
