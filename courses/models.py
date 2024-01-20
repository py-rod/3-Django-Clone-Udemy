from collections.abc import Iterable
from django.db import models
from django.template.defaultfilters import slugify
import os
# Create your models here.


class Course(models.Model):
    def video_upload_to(self, instance):
        if instance:
            return os.path.join("Video_Courses", slugify(self.author), slugify(self.title), instance)
        return None

    title = models.CharField(max_length=300, default="", blank=False)
    video = models.FileField(upload_to=f"{video_upload_to}")
    author = models.CharField(max_length=200, blank=True, default="")

    def __str__(self):
        return self.title
