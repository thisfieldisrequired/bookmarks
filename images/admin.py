from django.contrib import admin
from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """Регистрация мождели изображений в админ панеле"""

    list_display = ["title", "slug", "image", "created"]
    list_filter = ["created"]
