from django.contrib import admin
from .models import Actions


@admin.register(Actions)
class ActionAdmin(admin.ModelAdmin):
    """Регистрация подели действий пользователей"""

    list_display = ["user", "verb", "target", "created"]
    list_filter = ["created"]
    search_fields = ["verb"]
