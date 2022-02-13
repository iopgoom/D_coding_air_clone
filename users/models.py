import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string


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
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string(
                "emails/verify_email.html", {"secret": secret}
            )

            send_mail(
                "Verify Airbnb Account",
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
                html_message=html_message,
            )
        return
