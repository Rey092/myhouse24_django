# Generated by Django 3.2.4 on 2021-07-09 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('statistics_access', models.BooleanField(default=0)),
                ('flat_access', models.BooleanField(default=0)),
                ('house_user_access', models.BooleanField(default=0)),
                ('house_access', models.BooleanField(default=0)),
                ('message_access', models.BooleanField(default=0)),
                ('measures_access', models.BooleanField(default=0)),
                ('site_access', models.BooleanField(default=0)),
                ('service_access', models.BooleanField(default=0)),
                ('tariff_access', models.BooleanField(default=0)),
                ('role_access', models.BooleanField(default=0)),
                ('staff_access', models.BooleanField(default=0)),
                ('payments_detail_access', models.BooleanField(default=0)),
            ],
        ),
    ]