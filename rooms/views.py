# from math import ceil
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models


def all_rooms(request):
    page = request.GET.get("page", 1)
    rooms_list = models.Room.objects.all()
    paginator = Paginator(rooms_list, 10)
    # print(vars(rooms.paginator))
    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/all_rooms.html", context={"page": rooms})
    except EmptyPage:
        return redirect("/")


#  Manual Pagination Method
# def all_rooms(request):
#     page = int(request.GET.get("page", 1))
#     page_size = 10
#     limit = page_size * page
#     offset = limit - page_size
#     all_rooms = models.Room.objects.all()[offset:limit]
#     page_count = ceil(models.Room.objects.count() / page_size)
#     page_range = range(1, page_count + 1)
#     return render(
#         request,
#         "rooms/all_rooms.html",
#         context={
#             "rooms": all_rooms,
#             "page": page,
#             "page_count": page_count,
#             "page_range": page_range,
#         },
#     )
