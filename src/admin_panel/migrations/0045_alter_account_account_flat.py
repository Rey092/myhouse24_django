# Generated by Django 3.2.4 on 2021-07-14 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("admin_panel", "0044_alter_account_account_flat"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="account_flat",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="flat_account",
                to="admin_panel.flat",
            ),
        ),
    ]
