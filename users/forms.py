from typing import Any
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "username",
                  "email", "password1", "password2", "send_emails"]
        widgets = {
            "send_emails": forms.CheckboxInput(attrs={"class": "w-4 h-4 text-[#722FF9] bg-gray-100 border-gray-300 rounded focus:ring-[#722FF9] dark:focus:ring-[#722FF9]00 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"})
        }

    def save(self, commit=True) -> Any:
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.username = self.cleaned_data["username"]
        user.email = self.cleaned_data["email"]
        user.send_emails = self.cleaned_data["send_emails"]
        if commit:
            user.save()
        return user


class AuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs) -> None:
        super(AuthenticationForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.EmailInput(
        attrs={"type": "email", "autocomplete": "email", "autofocus": True}
    ))

    password = forms.PasswordInput()
