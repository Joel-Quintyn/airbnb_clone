from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    list_display = (
        "name",
        "room_count",
    )

    def room_count(self, obj):
        return obj.rooms.count()

    room_count.short_description = "No. of Rooms"


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    inlines = (PhotoInline,)

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
        # "id",
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
        "count_photos",
        "total_rating",
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

    raw_id_fields = ("host",)

    search_fields = (
        "country",
        "city",
        "^host__username",
    )

    filter_horizontal = ("amenities", "facilities", "house_rules")

    readonly_fields = ("created", "updated")

    # def count_amenities(self, obj):
    #     return obj.amenities.count()

    # count_amenities.short_description = "Amenities"

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photos"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    list_display = (
        "caption",
        "room",
        "get_thumbnail",
    )

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
