# Generated by Django 3.2.4 on 2021-07-21 12:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_panel', '0056_auto_20210721_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='house_staff',
            field=models.ManyToManyField(blank=True, null=True, through='admin_panel.HouseStaff', to=settings.AUTH_USER_MODEL),
        ),
    ]