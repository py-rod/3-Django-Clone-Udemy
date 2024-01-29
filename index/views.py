from django.shortcuts import render
from .models import ContentSection1, SelectLogos
from courses.models import Course
# Create your views here.


def index(request):
    content_section1 = ContentSection1.objects.filter(is_active=True, id=1)
    logos = SelectLogos.objects.all()
    videos = Course.objects.all()
    return render(request, "index.html", {
        "texts_section1": content_section1,
        "logos": logos,
    })
