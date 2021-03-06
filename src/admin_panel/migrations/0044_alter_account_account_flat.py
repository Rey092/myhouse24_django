# Generated by Django 3.2.4 on 2021-07-14 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("admin_panel", "0043_alter_account_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="account_flat",
            field=models.OneToOneField(
                blank=True,
                default=4,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="flat_account",
                to="admin_panel.flat",
            ),
            preserve_default=False,
        ),
    ]
