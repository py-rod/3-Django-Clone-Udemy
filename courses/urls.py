from django.urls import path
from . import views

urlpatterns = [
    path("<slug:category_slug>/<slug:subcategory_slug>/<slug:course_slug>",
         views.detail_course, name="detail_course")
]
