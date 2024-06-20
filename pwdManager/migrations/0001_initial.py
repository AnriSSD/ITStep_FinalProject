# Generated by Django 5.0.6 on 2024-06-15 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PasswordEntry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("service_name", models.CharField(max_length=100, unique=True)),
                ("user_name", models.CharField(max_length=30)),
                ("password", models.CharField(max_length=30)),
                ("email", models.CharField(max_length=50)),
                ("comment", models.TextField()),
            ],
        ),
    ]