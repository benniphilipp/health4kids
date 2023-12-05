# Generated by Django 3.2.23 on 2023-12-05 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0006_auto_20231205_0621'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mysettings',
            options={'verbose_name': 'Einstellungen'},
        ),
        migrations.AddField(
            model_name='mysettings',
            name='facebook',
            field=models.URLField(blank=True, help_text='Link zu deiner Facebook-Seite.', null=True),
        ),
        migrations.AddField(
            model_name='mysettings',
            name='instagram',
            field=models.URLField(blank=True, help_text='Link zu deiner Instagram-Seite.', null=True),
        ),
        migrations.AddField(
            model_name='mysettings',
            name='whatsapp',
            field=models.URLField(blank=True, help_text='Deine WhatsApp-Nummer.', null=True),
        ),
    ]
