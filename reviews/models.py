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
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review} - {self.room.name}"
