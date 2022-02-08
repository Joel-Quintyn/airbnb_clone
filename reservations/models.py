from operator import imod
from subprocess import check_output
from tabnanny import check
from django.db import models
from django.utils import timezone
from core import models as core_models


class Reservation(core_models.TimeStampedModel):

    """Reservation Model Definition"""

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUC_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )

    status = models.CharField(
        max_length=12, choices=STATUC_CHOICES, default=STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey(
        "users.User", related_name="reservations", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reservations", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.room.name} - {self.check_in}"

    def in_progress(self):

        """
        Method for checking if the resevation is in progress.
        returns True or False.
        """

        now = timezone.now().date()
        return now >= self.check_in and now <= self.check_out

    # To change the list display of in_progress view to a boolean icon/view i.e a tick or x
    in_progress.boolean = True

    def is_finished(self):

        """
        Method for checking if the resevation date has passed.
        returns True or False.
        """

        now = timezone.now().date()
        return now > self.check_out

    # To change the list display of is_finished view to a boolean icon/view i.e a tick or x
    is_finished.boolean = True
