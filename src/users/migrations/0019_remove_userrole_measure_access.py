# Generated by Django 3.2.4 on 2021-07-09 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0018_auto_20210709_1339"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userrole",
            name="measure_access",
        ),
    ]
