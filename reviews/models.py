from django.db import models
from core import models as core_models
import core


class Review(core_models.TimeStampedModel):

    review = models.TextField()
    cleanliness_rating = models.IntegerField()
    accuracy_rating = models.IntegerField()
    communication_rating = models.IntegerField()
    location_rating = models.IntegerField()
    check_in_rating = models.IntegerField()
    value_rating = models.IntegerField()
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.room.name}"

    def rating_average(self):

        """
        Method to calculate and return the average rating of a review
        returns the average rounded to two decimal places
        """
        
        avg = (
            self.cleanliness_rating
            + self.accuracy_rating
            + self.communication_rating
            + self.location_rating
            + self.check_in_rating
            + self.value_rating
        ) / 6
        return round(avg, 2)

    # rating_average.short_decription = "Avg."
