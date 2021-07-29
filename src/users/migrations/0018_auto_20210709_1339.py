# Generated by Django 3.2.4 on 2021-07-09 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0017_userrole"),
    ]

    operations = [
        migrations.RenameField(
            model_name="userrole",
            old_name="measures_access",
            new_name="measure_access",
        ),
        migrations.AddField(
            model_name="userrole",
            name="account_access",
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name="userrole",
            name="call_request_access",
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name="userrole",
            name="cashbox_access",
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name="userrole",
            name="meter_data_access",
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name="userrole",
            name="receipt_access",
            field=models.BooleanField(default=0),
        ),
    ]
