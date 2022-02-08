from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):

    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANG_EN = "영어"
    LANG_KR = "한국어"

    LANG_CHOICES = (
        (LANG_EN, "en"),
        (LANG_KR, "kr"),
    )

    CURRENCY_EN = "USD"
    CURRENCY_KR = "KRW"

    CURRENCY_CHOICES = (
        (CURRENCY_EN, "USD"),
        (CURRENCY_KR, "KRW"),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES,
        default=GENDER_MALE,
        max_length=10,
        blank=True,
    )
    feelGood = models.TextField(default="", blank=True)
    생일 = models.DateField(blank=True, null=True)
    언어 = models.CharField(
        choices=LANG_CHOICES, max_length=2, blank=True, default=LANG_KR
    )
    통화 = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, blank=True, default=CURRENCY_KR
    )
    주인장 = models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=120, default="", blank=True)

    def verify_email(self):
        pass
