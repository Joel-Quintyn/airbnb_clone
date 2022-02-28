from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.TimeStampedModel):

    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """
    RoomType Model Definition
        to add and remove a room type.
    """

    class Meta:
        verbose_name = "Room Type"
        verbose_name_plural = "Room Types"
        ordering = ["name"]


class Amenity(AbstractItem):
    """
    Amenity Model Definition
        to add and remove amenities.
    """

    class Meta:
        verbose_name = "Amenity"
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    """
    Facility Model Definition
        to add and remove facilities.
    """

    class Meta:
        verbose_name = "Facility"
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    """
    HouseRule Model Definition
        to add and remove house rules.
    """

    class Meta:
        verbose_name = "House Rule"
        verbose_name_plural = "House Rules"


class Photo(core_models.TimeStampedModel):
    """
    Photo Model Definition
        to add photos for a room
    """

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):

    """
    Room Model Definition
    """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})

    def total_rating(self):

        """
        Method that calculates the overall average reviews of a room.
        returns the average rounded to two decimal places
        """

        all_reviews = self.reviews.all()
        total_rating = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                total_rating += review.rating_average()
            return round((total_rating / len(all_reviews)), 2)
        return 0

    total_rating.short_description = "Rating"
