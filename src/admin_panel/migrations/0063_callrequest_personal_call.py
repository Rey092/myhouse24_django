# Generated by Django 3.2.4 on 2021-08-02 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_panel", "0062_alter_callrequest_flat"),
    ]

    operations = [
        migrations.AddField(
            model_name="callrequest",
            name="personal_call",
            field=models.BooleanField(blank=True, null=True),
        ),
    ]