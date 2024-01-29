from django.db import models
from django.template.defaultfilters import slugify
import os
from subcategories.models import Subcategories
from tinymce.models import HTMLField
from django.urls import reverse
# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=300, default="", blank=False)
    slug = models.SlugField(default="", blank=False, unique=True)
    author = models.CharField(max_length=200, blank=True, default="")
    subcategory = models.ForeignKey(
        Subcategories, default="", on_delete=models.CASCADE)
    category = models.CharField(max_length=200, blank=True)
    will_learn = HTMLField(max_length=2000, blank=False)
    requirements = HTMLField(max_length=2000, blank=False)
    description = models.TextField(max_length=1000, blank=False)

    def __str__(self):
        return self.title

    def get_url_course_detail(self):
        return reverse("detail_course", args=[self.subcategory.series.slug, self.subcategory.slug, self.slug])


class SectionCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class VideoCourse(models.Model):
    def video_upload_to(self, instance):
        if instance:
            return os.path.join("Video_Courses", slugify(self.section.course.author),  instance)
        return None
    section = models.ForeignKey(SectionCourse, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to=f"{video_upload_to}")

    def __str__(self):
        return self.title
