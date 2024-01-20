from typing import Any
from django.contrib import admin
from .models import Course
# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author")
    list_display_links = ("id", "title", "author")
    search_fields = ("id", "title", "author")
    list_per_page = 20

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        get_user = request.user
        if not obj.author:
            obj.author = get_user
        super().save_model(request, obj, form, change)
