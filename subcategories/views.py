from django.shortcuts import render
from .models import Subcategories
from courses.models import Course, SectionCourse, VideoCourse
# Create your views here.


def all_courses_for_category(request, category, subcategory):
    title_window = Subcategories.objects.get(
        series__slug=category, slug=subcategory, is_active=True)

    courses = Course.objects.filter(subcategory__title=title_window)

    return render(request, "content_courses.html", {
        "title_window": title_window,
        "courses": courses,
        "result": courses.count()
    })
