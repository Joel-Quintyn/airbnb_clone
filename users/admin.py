from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """
    Custom User Admin Display/View
    """

    list_display = ("username", "email", "gender", "language", "currency", "superhost")
    list_filter = ("superhost", "language", "currency")
