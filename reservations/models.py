from django.db import models
from django.utils import timezone
from core import models as core_models


# Create your models here.
class Reservation(core_models.TimeStampedModel):
    """예약 모델 정의"""

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELD = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELD, "Canceled"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )

    check_in = models.DateField()
    check_out = models.DateField()

    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room.방이름} - {self.check_in} 까지 입실"

    def in_prograss(self):
        now = timezone.now().date()
        return now > self.check_in and now < self.check_out

    in_prograss.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out

    is_finished.boolean = True
