from django.db import models
from categories.models import Categories
import os
from django.urls import reverse

# Create your models here.


class Subcategories(models.Model):
    title = models.CharField(max_length=200, blank=False, unique=True)
    slug = models.SlugField(default="", unique=True, blank=False)
    series = models.ForeignKey(
        Categories, default="", blank=False, on_delete=models.SET_DEFAULT)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Sub Categories"
        db_table = "Sub_Categories"

    def __str__(self):
        return self.title

    def get_subcategory_url(self):
        return reverse("all_courses_for_category", args=[self.series.slug, self.slug])


class Themes(models.Model):
    title = models.ForeignKey(
        Subcategories, default="", on_delete=models.CASCADE)
