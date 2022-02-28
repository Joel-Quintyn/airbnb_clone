from django.views.generic import ListView
from . import models


class HomeView(ListView):

    context_object_name = "rooms"
    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
