# Generated by Django 3.2.4 on 2021-07-12 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0037_alter_message_floor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='floor',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]