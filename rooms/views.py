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
from . import models


class Homeview(ListView):
    """Homeview define"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 2
    ordering = "created"
    page_kwarg = "page"

    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
