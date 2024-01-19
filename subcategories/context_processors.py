from categories.models import Categories
from .models import Subcategories
import json


def menu_links(request):
    categories = Categories.objects.filter(is_active=True).order_by("id")

    sub = {}

    for category in categories:
        subcategory = Subcategories.objects.filter(
            series__title=category, is_active=True).order_by("id")
        sub[category] = subcategory

    return dict(subcategories=sub, categories=categories)
