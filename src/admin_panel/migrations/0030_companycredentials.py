# Generated by Django 3.2.4 on 2021-07-12 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_panel", "0029_auto_20210709_1052"),
    ]

    operations = [
        migrations.CreateModel(
            name="CompanyCredentials",
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
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=3000, null=True),
                ),
            ],
        ),
    ]
