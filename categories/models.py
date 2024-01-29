from django.db import models
import os


# Create your models here.


class Categories(models.Model):
    title = models.CharField(max_length=200, unique=True, blank=False)
    slug = models.SlugField(default="", unique=True, blank=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"
        db_table = "Categories"

    def __str__(self):
        return self.title
