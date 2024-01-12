from django.urls import path
from . import views


urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("logout", views.close_session, name="logout"),
    # ACTIVATE ACCOUNT
    path("activate/<uidb64>/<token>", views.activate, name="activate"),
]
