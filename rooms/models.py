from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

# Create your models here.


class AbstractItem(core_models.TimeStampedModel):
    """방 요약"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """방 타입 정의"""

    class Meta:
        verbose_name_plural = "방 타입"


class Amenity(AbstractItem):
    """방 편의 시설 정의"""

    class Meta:
        verbose_name_plural = "편의 시설"


class Facility(AbstractItem):
    """방 부대 시설 정의"""

    class Meta:
        verbose_name_plural = "부대 시설"


class Houoserule(AbstractItem):
    """사용 규칙 정의"""

    class Meta:
        verbose_name_plural = "사용 규칙"


class Photo(core_models.TimeStampedModel):
    """사진 모델 정의"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photo", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):
    """방 모델 정의"""

    방이름 = models.CharField(max_length=140)
    방소개 = models.TextField()
    국가 = CountryField()
    도시 = models.CharField(max_length=80)
    가격 = models.IntegerField()
    주소 = models.CharField(max_length=140)
    투숙객 = models.IntegerField()
    침대 = models.IntegerField()
    화장실 = models.IntegerField()
    욕조 = models.IntegerField()
    체크인_시간 = models.TimeField()
    체크아웃_시간 = models.TimeField()
    예약 = models.BooleanField(default=False)
    주인장 = ForeignKey("users.User", related_name="rooms", on_delete=models.CASCADE)
    방종류 = models.ForeignKey(
        "RoomType",
        related_name="rooms",
        blank=True,
        on_delete=models.SET_NULL,
        null=True,
    )
    편의시설 = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    부대시설 = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    사용규칙 = models.ManyToManyField("Houoserule", related_name="rooms", blank=True)

    def __str__(self):
        return self.방이름

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0

        for review in all_reviews:
            all_ratings += review.rating_average()

        if len(all_reviews) > 0:
            return round(all_ratings / len(all_reviews), 2)
        else:
            return 0
