from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):

    participants = models.ManyToManyField("users.User")

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)

        # If the amount of participants are 2; Return different format of string.
        if len(usernames) == 2:
            return " and ".join(usernames)
        return ", ".join(usernames)

    def count_messages(self):
        """Method that returns the amount of messages in a coversation"""
        return self.messages.count()

    count_messages.short_description = "Messages"

    def count_participants(self):
        """Method that returns the amount of participants in a coversation"""
        return self.participants.count()

    count_participants.short_description = "Participants"


class Message(core_models.TimeStampedModel):

    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says: {self.message}"
