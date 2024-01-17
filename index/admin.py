from django.contrib import admin
from .models import ContentSection1, SelectLogos, BrandsLogos
# Register your models here.


@admin.register(ContentSection1)
class ContentAdminSection1(admin.ModelAdmin):
    list_display = ("id", "title", "created")
    list_display_links = ("id", "title")
    list_filter = ("is_active", )
    list_per_page = 20
    search_fields = ("id", "title")


@admin.register(BrandsLogos)
class BrandsLogosAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    list_per_page = 20
    search_fields = ("id", "title")


@admin.register(SelectLogos)
class SelectLogosAdmin(admin.ModelAdmin):
    list_display = ("id", "brand_logo")
    list_display_links = ("id", "brand_logo")
    list_per_page = 20
    search_fields = ("id", "brand_logo")
