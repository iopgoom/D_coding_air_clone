from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """예약 어드민 정의"""

    list_display = (
        "room",
        "guest",
        "check_in",
        "check_out",
        "status",
        "in_prograss",
        "is_finished",
    )

    list_filter = ("status",)
