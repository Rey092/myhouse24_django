# Generated by Django 3.2.4 on 2021-07-01 13:07

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0010_auto_20210630_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteContacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=3000, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('map', models.CharField(blank=True, max_length=4000, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('seo_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.seodata')),
            ],
        ),
    ]
