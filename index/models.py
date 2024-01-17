from django.db import models
import os
# Create your models here.


class ContentSection1(models.Model):
    title = models.CharField(max_length=254, default="", blank=False)
    description = models.TextField(max_length=300, default="", blank=False)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Content Section 1"

    def __str__(self):
        return self.title


class BrandsLogos(models.Model):
    def image_upload_to(self, instance):
        if instance:
            return os.path.join("LogoBrand", self.title, instance)
        return None

    title = models.CharField(unique=True, blank=False, max_length=200)
    image = models.ImageField(
        upload_to=image_upload_to, default="", blank=False)

    class Meta:
        verbose_name_plural = "Upload Logos"
        db_table = "Brands_Logos"

    def __str__(self):
        return self.title


class SelectLogos(models.Model):
    brand_logo = models.ForeignKey(BrandsLogos,
                                   default="", blank=False, on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name_plural = "Select Logos"
        db_table = "Select_Logos"

    def __str__(self):
        return f"You have select {self.brand_logo.title}"
