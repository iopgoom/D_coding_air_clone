from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """유저 디스플레이 확인"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "사용자설정",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "feelGood",
                    "생일",
                    "언어",
                    "통화",
                    "주인장",
                    "login_method",
                ),
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("주인장",)

    list_display = (
        "username",
        "email",
        "생일",
        "언어",
        "통화",
        "주인장",
        "is_active",
        "email_verified",
        "email_secret",
        "login_method",
    )
