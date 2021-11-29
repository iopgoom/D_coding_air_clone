from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.RoomType, models.Facility, models.Amenity, models.Houoserule)
class ItemAdmin(admin.ModelAdmin):
    """item admin define"""

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """room admin define"""

    fieldsets = (
        (
            "기본정보",
            {
                "fields": (
                    "방이름",
                    "방소개",
                    "국가",
                    "도시",
                    "가격",
                    "주소",
                )
            },
        ),
        (
            "시간",
            {
                "fields": (
                    "체크인_시간",
                    "체크아웃_시간",
                )
            },
        ),
        (
            "방 정보",
            {
                "fields": (
                    "투숙객",
                    "침대",
                    "화장실",
                    "욕조",
                ),
            },
        ),
        (
            "방 물품",
            {
                "classes": ("collapse",),
                "fields": (
                    "편의시설",
                    "부대시설",
                    "사용규칙",
                ),
            },
        ),
        (
            "추가 정보",
            {"fields": ("주인장",)},
        ),
    )

    list_display = (
        "방이름",
        "국가",
        "도시",
        "가격",
        "주소",
        "주인장",
        # "투숙객",
        # "침대",
        # "화장실",
        # "욕조",
        # "체크인_시간",
        # "체크아웃_시간",
        # "예약",
        # "방종류",
        # "편의시설",
        # "부대시설",
        "RuleNum",
        "photo_num",
        "total_rating",
    )

    list_filter = (
        "주인장",
        "도시",
        "국가",
    )

    search_fields = ("=도시", "주인장__username")
    filter_horizontal = (
        "편의시설",
        "부대시설",
        "사용규칙",
    )

    def RuleNum(self, obj):
        return obj.사용규칙.count()

    RuleNum.short_description = "사용규칙"

    def photo_num(self, obj):
        return obj.photo.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo admin define"""

    pass
