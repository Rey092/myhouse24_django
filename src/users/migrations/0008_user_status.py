# Generated by Django 3.2.4 on 2021-07-02 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_auto_20210702_0613"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="status",
            field=models.CharField(
                choices=[
                    ("ACTIVE", "Активный"),
                    ("INACTIVE", "Неактивный"),
                    ("DEACTIVATED", "Деактивированный"),
                ],
                default="ACTIVE",
                max_length=11,
            ),
            preserve_default=False,
        ),
    ]
