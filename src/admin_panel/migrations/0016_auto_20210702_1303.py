# Generated by Django 3.2.4 on 2021-07-02 13:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("admin_panel", "0015_rename_section_section_house"),
    ]

    operations = [
        migrations.AddField(
            model_name="section",
            name="floors",
            field=models.PositiveIntegerField(
                default=10, validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
        migrations.AlterField(
            model_name="section",
            name="house",
            field=models.ForeignKey(
                default=7,
                on_delete=django.db.models.deletion.CASCADE,
                to="admin_panel.house",
            ),
            preserve_default=False,
        ),
    ]
