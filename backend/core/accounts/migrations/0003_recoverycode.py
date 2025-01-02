# Generated by Django 4.2.17 on 2025-01-02 05:24

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_profile"),
    ]

    operations = [
        migrations.CreateModel(
            name="RecoveryCode",
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
                (
                    "digits",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1000),
                            django.core.validators.MaxValueValidator(9999),
                        ]
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
