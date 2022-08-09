from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class UserAdmin(UserAdmin):

    """
    Custom User Admin Display/View
    """

    fieldsets = UserAdmin.fieldsets + (
        (
            "More Info.",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "bithdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        # "id",
        "username",
        "first_name",
        "last_name",
        "email",
        "email_verified",
        # "email_secret",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
