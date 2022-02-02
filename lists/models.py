from django.db import models
from core import models as core_models


class List(core_models.TimeStampedModel):

    """Lists Models Definition"""

    name = models.CharField(max_length=80)
    user = models.ForeignKey(
        "users.User", related_name="lists", on_delete=models.CASCADE
    )
    rooms = models.ManyToManyField("rooms.Room", related_name="lists", blank=True)

    def __str__(self):
        return self.name

    def total_stays(self):
        """Returns the total rooms/stays in a list"""
        return self.rooms.count()

    total_stays.short_description = "Stays"
