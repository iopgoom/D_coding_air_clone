# from math import ceil
# from django.core import paginator
# from django.shortcuts import render, redirect
# from django.core.paginator import Paginator, EmptyPage
# from . import models


# Create your views here.
# def all_rooms(request):
# 자력으로 만들기
# page = request.GET.get("page", 1)
# page = int(page or 1)
# num = int(request.GET.get("num", 10))
# limit = page * num
# offset = (page * num) - num
# page_count = ceil(models.Room.objects.count() / num)
# print(page)

# all_rooms = models.Room.objects.all()[offset:limit]

# return render(
#     request,
#     "rooms/test.html",
#     context={
#         "rooms": all_rooms,
#         "page": page,
#         "page_count": page_count,
#         "page_range": range(1, page_count + 1),
#     },
# )

# 장고 기능 + 만들기 get_page
# page = request.GET.get("page")
# room_list = models.Room.objects.all()
# paginatior = Paginator(room_list, 10)
# rooms = paginatior.get_page(page)

# print(vars(rooms.paginator))
# return render(
#     request,
#     "rooms/test.html",
#     {
#         "rooms": rooms,
#     },
# )

# 장고 기능 + 만들기 page

# page = request.GET.get("page", 1)
# room_list = models.Room.objects.all()
# paginatior = Paginator(room_list, 10, orphans=5)
# try:
#     rooms = paginatior.page(int(page))
#     return render(
#         request,
#         "rooms/test.html",
#         {
#             "page": rooms,
#         },
#     )
# except EmptyPage:
#     return redirect("/")


# 장고가 다해주기
from django.views.generic import ListView
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django_countries import countries
from django.views.generic import ListView, DetailView
from . import models


class Homeview(ListView):
    """Homeview define"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 2
    ordering = "created"
    page_kwarg = "page"

    context_object_name = "rooms"


# function base
# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/detail.html", {"room": room})
#     except models.Room.DoesNotExist:
#         # return redirect(reverse("core:home"))
#         raise Http404()


# class_base
class RoomDetail(DetailView):
    model = models.Room
    pass


# function_base
def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "kr")
    room_type = int(request.GET.get("room_type", "0"))
    room_types = models.RoomType.objects.all()

    form = {"city": city, "s_country": country, "s_room_type": room_type}

    choices = {"room_types": room_types, "countries": countries}

    return render(
        request,
        "rooms/search.html",
        {**form, **choices},
    )
