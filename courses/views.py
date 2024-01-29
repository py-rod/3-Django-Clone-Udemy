from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Course, SectionCourse, VideoCourse
# Create your views here.


def detail_course(request, category_slug, subcategory_slug, course_slug):

    course = Course.objects.get(
        subcategory__series__slug=category_slug, subcategory__slug=subcategory_slug, slug=course_slug)

    return render(request, "course_detail.html", {
        "course": course
    })
