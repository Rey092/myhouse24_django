# Generated by Django 3.2.4 on 2021-07-06 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('выы', 'Активный'), ('INACTIVE', 'Неактивный'), ('DEACTIVATED', 'Деактивированный')], max_length=11),
        ),
    ]