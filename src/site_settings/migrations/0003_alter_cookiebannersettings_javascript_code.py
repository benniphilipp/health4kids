# Generated by Django 3.2.23 on 2023-12-10 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0002_auto_20231208_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cookiebannersettings',
            name='javascript_code',
            field=models.TextField(blank=True, null=True, verbose_name='Google Tag Manager Code GTM-KLTQ3K72'),
        ),
    ]
