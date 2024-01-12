from django.contrib import admin
from .models import CustomUser
# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "is_active",
                    "is_teach", "is_superuser")
    list_display_links = ("id", "username", "email")
    list_editable = ("is_active", "is_teach", "is_superuser")
    list_filter = ("is_active", "is_teach", "is_superuser")
    list_per_page = 20
    search_fields = ("id", "username", "email")
