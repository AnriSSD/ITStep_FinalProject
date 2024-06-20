import random
import string
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from pwdManager.forms import PasswordForm, PasswordGeneratorForm
from pwdManager.models import PasswordEntry
from pwdManager.forms import CreateUserForm, PasswordForm
from pwdManager.models import PasswordEntry


def signup(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"registerform": form}

    return render(request, "registration/signup.html", context=context)


def all_passwords(request):
    user = request.user
    if user.is_authenticated:
        entry_list = PasswordEntry.objects.filter(user=user)
        service_name = request.GET.get("service_name")
        if service_name:
            entry_list = entry_list.filter(
                service_name__icontains=service_name, user=user
            )
    else:
        entry_list = []
    return render(request, "passwordlist.html", {"entry_list": entry_list})


def create_password_entry(request):
    form = PasswordForm()

    if request.method == "POST":
        user = request.user
        data = request.POST.copy()
        data["user"] = user
        form = PasswordForm(data)
        print(request.POST)

        if form.is_valid():
            form.save()
            return redirect("passwordlist")

    context = {"newentry": form}
    return render(request, "newentry.html", context=context)


def update_password_entry(request, entry_id):
    entry = PasswordEntry.objects.get(pk=entry_id)
    form = PasswordForm(request.POST or None, instance=entry)
    if form.is_valid():
        form.save()
        return redirect("passwordlist")
    return render(request, "updateentry.html", {"entry": entry, "form": form})


def delete_password_entry(request, entry_id):
    entry = PasswordEntry.objects.get(pk=entry_id)
    entry.delete()
    return redirect("passwordlist")


@login_required
def generate_password(request):
    form = PasswordGeneratorForm()
    generated_password = None

    if request.method == "POST":
        form = PasswordGeneratorForm(request.POST)
        if form.is_valid():
            length = form.cleaned_data["length"]
            generated_password = "".join(
                random.choices(
                    string.ascii_letters + string.digits + string.punctuation, k=length
                )
            )

    context = {"form": form, "generated_password": generated_password}
    return render(request, "generate_password.html", context)
