"""
URL configuration for django_pwdManager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from pwdManager import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup/", views.signup, name="signup"),
    path("newentry/", views.create_password_entry, name="newentry"),
    path("passwordlist/", views.all_passwords, name="passwordlist"),
    path("updateentry/<entry_id>", views.update_password_entry, name="updateentry"),
    path("deleteentry/<entry_id>", views.delete_password_entry, name="deleteentry"),
]

from django.urls import path
from pwdManager import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup/", views.signup, name="signup"),
    path("newentry/", views.create_password_entry, name="newentry"),
    path("passwordlist/", views.all_passwords, name="passwordlist"),
    path("updateentry/<entry_id>", views.update_password_entry, name="updateentry"),
    path("deleteentry/<entry_id>", views.delete_password_entry, name="deleteentry"),
    path("generate_password/", views.generate_password, name="generate_password"),
]
