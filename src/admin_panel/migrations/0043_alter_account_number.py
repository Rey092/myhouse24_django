# Generated by Django 3.2.4 on 2021-07-14 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_panel", "0042_alter_account_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="number",
            field=models.CharField(blank=True, max_length=40, unique=True),
        ),
    ]
