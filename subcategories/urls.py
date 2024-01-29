from django.urls import path
from . import views

urlpatterns = [
    path("<slug:category>/<slug:subcategory>/", views.all_courses_for_category,
         name="all_courses_for_category")
]
