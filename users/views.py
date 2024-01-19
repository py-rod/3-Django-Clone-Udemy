from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import RegisterUserForm, AuthenticationForm

# AUTH ACCOUNT
from django.contrib.auth import login, logout, authenticate

# ACTIVATE ACCOUNT
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage, send_mail
from .token import account_activation_token

# MESSAGES DJANGO
from django.contrib import messages

# DEFAULT DECORATORS
from django.contrib.auth.decorators import login_required

# CUSTOM DECORATORS
from .decorators import user_not_authenticated

# Create your views here.


def activate_email(request, user, to_email):
    mail_sub = "EduHub | Activate your user account"
    message = render_to_string("activate_account.html", {
        "user": user,
        "domain": get_current_site(request).domain,
        "uid": urlsafe_base64_encode(force_bytes(user.id)),
        "token": account_activation_token.make_token(user),
        "protocol": "https" if request.is_secure() else "http"
    })
    email = EmailMessage(mail_sub, message, to=[to_email])
    # lA DECLARACION DE ABAJO SIRVE PARA QUE EL CORREO NO LLEGUE COMO TEXTO PLANO Y SE LE PUEDA DAR STYLOS
    email.content_subtype = "html"
    if email.send():
        messages.success(request, "Check your email to verifications")
    else:
        messages.error(
            request, f"Problem sending confirmation email {to_email}, check if your type is correctly")


def activate(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(id=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_social_account_active = False
        user.is_active = True
        user.save()
        messages.success(request, "Your account has been activate")
    else:
        messages.error(request, "Activate link is invalid")

    return redirect("signin")


@user_not_authenticated
def signup(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activate_email(request, user, form.cleaned_data.get("email"))
            return redirect("home")
        else:
            for error in list(form.errors.values()).pop():
                messages.error(request, error)
    else:
        form = RegisterUserForm()
    return render(request, "signup.html", {
        "form": form
    })


def redirect_signin_with_google(request):
    messages.error(
        request, "Something wrong here, it may be that you already have account!")
    return redirect("signin")


@user_not_authenticated
def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                email=form.cleaned_data.get("username"),
                password=form.cleaned_data.get("password")
            )
            if user is not None:
                login(request, user)
                messages.success(
                    request, f"Welcome {user.first_name} {user.last_name} :D")
                return redirect("home")
        else:
            for error in list(form.errors.values()).pop():
                messages.error(request, error)
    else:
        form = AuthenticationForm()
    return render(request, "signin.html", {
        "form": form
    })


@login_required(login_url="")
def close_session(request):
    logout(request)
    return redirect("home")
