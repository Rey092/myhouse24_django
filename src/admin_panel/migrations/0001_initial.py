# Generated by Django 3.2.4 on 2021-06-25 15:47

from django.db import migrations, models
import django.db.models.deletion
import src.admin_panel.services.media_services


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=3000)),
                (
                    "image",
                    models.ImageField(
                        upload_to=src.admin_panel.services.media_services.UploadToPathAndRename(
                            "images/site/home_page/articles"
                        )
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SeoData",
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
                ("title", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=3000, null=True),
                ),
                ("keywords", models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="SiteHomePage",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=3000)),
                ("show_links", models.BooleanField(default=False)),
                (
                    "slider1",
                    models.ImageField(
                        upload_to=src.admin_panel.services.media_services.UploadToPathAndRename(
                            "images/site/home_page/slider"
                        )
                    ),
                ),
                (
                    "slider2",
                    models.ImageField(
                        upload_to=src.admin_panel.services.media_services.UploadToPathAndRename(
                            "images/site/home_page/slider"
                        )
                    ),
                ),
                (
                    "slider3",
                    models.ImageField(
                        upload_to=src.admin_panel.services.media_services.UploadToPathAndRename(
                            "images/site/home_page/slider"
                        )
                    ),
                ),
                ("around_us", models.ManyToManyField(to="admin_panel.Article")),
                (
                    "seo_data",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admin_panel.seodata",
                    ),
                ),
            ],
        ),
    ]
