from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "name",
                    "description",
                    "room_type",
                    "address",
                    "country",
                    "city",
                    "price",
                )
            },
        ),
        (
            "Booking",
            {"fields": ("check_in", "check_out", "instant_book")},
        ),
        (
            "More about the space",
            {"fields": ("guests", "beds", "bedrooms", "baths")},
        ),
        (
            "What this place offers",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        (
            "Last Details",
            {"fields": ("host", "created", "updated")},
        ),
    )

    # ordering = ("name", "price", "bedrooms")

    list_display = (
        "name",
        "host",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "room_type",
        # "count_amenities",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        # "city",
        "country",
    )

    search_fields = (
        "country",
        "city",
        "^host__username",
    )

    filter_horizontal = ("amenities", "facilities", "house_rules")

    readonly_fields = ("created", "updated")

    # def count_amenities(self, obj):
    #     amount = obj.amenities.count()
    #     return amount

    # count_amenities.short_description = "Amenities"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    pass
