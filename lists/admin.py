from pyexpat import model
from django.contrib import admin
from . import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    """List Admin Definition"""

    list_display = ("name", "user", "total_stays")

    search_fields = ("name",)
