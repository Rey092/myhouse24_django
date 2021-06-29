# Generated by Django 3.2.4 on 2021-06-29 06:26

from django.db import migrations, models
import src.admin_panel.services.media_services


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0006_auto_20210629_0429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(default=1, upload_to=src.admin_panel.services.media_services.UploadToPathAndRename('docs')),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='name',
            field=models.CharField(default='name', max_length=100),
            preserve_default=False,
        ),
    ]
