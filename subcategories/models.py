from django.db import models
from categories.models import Categories
import os


# Create your models here.


class Subcategories(models.Model):
    title = models.CharField(max_length=200, blank=False, unique=True)
    series = models.ForeignKey(
        Categories, default="", blank=False, on_delete=models.SET_DEFAULT)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Sub_Categories"
        db_table = "Sub_Categories"

    def __str__(self):
        return self.title
