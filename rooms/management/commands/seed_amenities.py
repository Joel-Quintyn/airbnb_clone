from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    help = "This command creates all amenities."

    def handle(self, *args, **options):
        amenities = [
            "Air Conditioning",
            "Alarm Clock",
            "Balcony",
            "Bathroom",
            "Bathtub",
            "Bed Linen",
            "Boating",
            "Breakfast",
            "Cable TV",
            "Carbon Monoxide Detectors",
            "Chairs",
            "Children Area",
            "Coffee Maker",
            "Cooking Hob",
            "Dedicated Workspace",
            "Dishwasher",
            "Double Bed",
            "Dryer",
            "En Suite Bathroom",
            "EV Charger",
            "Free Parking",
            "Freezer",
            "Fridge / Freezer",
            "Golf",
            "Gym",
            "Hair Dryer",
            "Heating",
            "Hot Tub",
            "Indoor Fireplace",
            "Indoor Pool",
            "Iron",
            "Kitchen",
            "Microwave",
            "Outdoor Pool",
            "Outdoor Tennis",
            "Oven",
            "Queen Sized Bed",
            "Restaurant",
            "Self Check-In",
            "Shopping Mall",
            "Shower",
            "Smoke Detectors",
            "Sofa",
            "Stereo",
            "Toilet",
            "Towels",
            "TV",
            "Washer",
            "Wifi",
        ]

        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities Created!"))
