# Generated by Django 3.2.4 on 2021-07-08 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_panel", "0023_auto_20210708_0430"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="is_removable",
            field=models.BooleanField(default=True),
        ),
    ]
