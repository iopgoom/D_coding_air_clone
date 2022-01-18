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
    room_type = int(request.GET.get("room_type", 0))
    max_price = int(request.GET.get("max_price", 0))
    min_price = int(request.GET.get("min_price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    bads = int(request.GET.get("bads", 0))
    baths = int(request.GET.get("baths", 0))
    instant = bool(request.GET.get("instant", False))
    superhost = bool(request.GET.get("superhost", False))
    s_amenities = request.GET.getlist("amenities")
    s_facilities = request.GET.getlist("facilities")
    s_houoserules = request.GET.getlist("houoserules")

    form = {
        "city": city,
        "s_country": country,
        "s_room_type": room_type,
        "max_price": max_price,
        "min_price": min_price,
        "guests": guests,
        "bedrooms": bedrooms,
        "bads": bads,
        "baths": baths,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
        "s_houoserules": s_houoserules,
        "instant": instant,
        "superhost": superhost,
    }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()
    houoserules = models.Houoserule.objects.all()

    choices = {
        "room_types": room_types,
        "countries": countries,
        "amenities": amenities,
        "facilities": facilities,
        "houoserules": houoserules,
    }

    filter_arg = {}

    if city != "Anywhere":
        filter_arg["도시__startswith"] = city

    filter_arg["국가"] = country

    if room_type != 0:
        filter_arg["방종류__pk"] = room_type

    if max_price != 0:
        filter_arg["가격__lte"] = max_price

    if min_price != 0:
        filter_arg["가격__gte"] = min_price

    if guests != 0:
        filter_arg["투숙객__gte"] = guests

    if bedrooms != 0:
        filter_arg["침대__gte"] = bedrooms

    if bads != 0:
        filter_arg["화장실__gte"] = bads

    if baths != 0:
        filter_arg["욕조__gte"] = baths

    if instant is True:
        filter_arg["예약"] = True

    if superhost is True:
        filter_arg["주인장__주인장"] = True

    if len(s_amenities) > 0:
        for s_amenity in s_amenities:
            filter_arg["편의시설__pk"] = int(s_amenity)

    if len(s_facilities) > 0:
        for s_facility in s_facilities:
            filter_arg["부대시설__pk"] = int(s_facility)

    if len(houoserules) > 0:
        for houoserule in houoserules:
            filter_arg["사용규칙__pk"] = int(houoserule)

    rooms = models.Room.objects.filter(**filter_arg)

    return render(
        request,
        "rooms/search.html",
        {**form, **choices, "rooms": rooms},
    )
