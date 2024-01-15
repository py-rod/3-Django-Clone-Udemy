from django.urls import path
from . import views


urlpatterns = [
    path("users/signup/", views.signup, name="signup"),
    path("users/signin/", views.signin, name="signin"),
    path("users/logout", views.close_session, name="logout"),
    # ACTIVATE ACCOUNT
    path("users/activate/<uidb64>/<token>", views.activate, name="activate"),
    path("social/signup/", views.redirect_signin_with_google, name="signup_redirect")
]
