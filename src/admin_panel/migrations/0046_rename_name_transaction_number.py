# Generated by Django 3.2.4 on 2021-07-14 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("admin_panel", "0045_alter_account_account_flat"),
    ]

    operations = [
        migrations.RenameField(
            model_name="transaction",
            old_name="name",
            new_name="number",
        ),
    ]
