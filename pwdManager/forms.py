from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from pwdManager.models import PasswordEntry


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class PasswordForm(forms.ModelForm):
    service_name = forms.CharField(min_length=1, required=True)
    user_name = forms.CharField(min_length=3, required=True)
    email = forms.EmailField(required=False)
    password = forms.CharField(min_length=3, required=True)
    comment = forms.CharField(required=False)

    class Meta:
        widgets = {"user": forms.HiddenInput()}
        model = PasswordEntry
        fields = ["service_name", "user_name", "email", "password", "comment", "user"]


class PasswordGeneratorForm(forms.Form):
    length = forms.IntegerField(min_value=8, max_value=128, required=True)
