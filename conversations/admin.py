from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "message",
        "user",
        "conversation",
        # "count_messages",
    )


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "count_messages",
    )
