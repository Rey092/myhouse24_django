# Generated by Django 3.2.4 on 2021-07-14 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("admin_panel", "0046_rename_name_transaction_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="amount",
            field=models.DecimalField(decimal_places=2, default=10, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="transaction",
            name="manager",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="transaction_manager",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="transaction_created_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
