from django.contrib import admin
from .models import Subcategories
# Register your models here.


@admin.register(Subcategories)
class SubcategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("id", "title", "series", "is_active")
    list_display_links = ("id", "title")
    list_editable = ("series", "is_active")
    list_filter = ("series", "is_active")
    list_per_page = 20
    search_fields = ("id", "title")
