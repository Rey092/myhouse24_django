# Generated by Django 3.2.4 on 2021-07-09 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("admin_panel", "0025_remove_tariff_services"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="serviceprice",
            name="tariff",
        ),
    ]
