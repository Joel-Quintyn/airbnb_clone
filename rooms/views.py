from django.views.generic import ListView, DetailView
from django.shortcuts import render
from . import models


class HomeView(ListView):

    context_object_name = "rooms"
    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"


class RoomDetail(DetailView):

    model = models.Room


""" Function based view for the room_detail view """
# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/detail.html", {"room": room})
#     except models.Room.DoesNotExist:
#         raise Http404()


def search_view(request):
    city = str.capitalize(request.GET.get("city"))
    print(city)
    return render(request, "rooms/search.html", {"city": city})
