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
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, View
from . import models, forms


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
class SearchView(View):
    def get(get, request):

        country = request.GET.get("country")

        if country:
            form = forms.SearchForm(request.GET)
            if form.is_valid():
                city = form.cleaned_data.get("city")
                price = form.cleaned_data.get("price")
                room_type = form.cleaned_data.get("room_type")
                country = form.cleaned_data.get("country")
                guests = form.cleaned_data.get("guests")
                beds = form.cleaned_data.get("beds")
                bathrooms = form.cleaned_data.get("bathrooms")
                bath = form.cleaned_data.get("bath")
                instant_book = form.cleaned_data.get("instant_book")
                supehost = form.cleaned_data.get("supehost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")
                houoserules = form.cleaned_data.get("houoserules")

                filter_args = {}

                if city != "Anywhere":
                    filter_args["도시__startswith"] = city

                filter_args["국가"] = country

                if room_type is not None:
                    filter_args["방종류"] = room_type

                if price is not None:
                    filter_args["가격__lte"] = price

                if guests is not None:
                    filter_args["투숙객__gte"] = guests

                if bathrooms is not None:
                    filter_args["화장실__gte"] = bathrooms

                if beds is not None:
                    filter_args["침대__gte"] = beds

                if bath is not None:
                    filter_args["욕조__gte"] = bath

                if instant_book is True:
                    filter_args["예약"] = True

                if supehost is True:
                    filter_args["주인장__주인장"] = True

                for amenity in amenities:
                    filter_args["편의시설"] = amenity

                for facility in facilities:
                    filter_args["부대시설"] = facility

                for houoserule in houoserules:
                    filter_args["사용규칙"] = houoserule

                rooms = models.Room.objects.filter(**filter_args)
            return render(
                request,
                "rooms/search.html",
                {"form": form, "rooms": rooms},
            )
        else:
            form = forms.SearchForm()

        return render(
            request,
            "rooms/search.html",
            {"form": form},
        )
