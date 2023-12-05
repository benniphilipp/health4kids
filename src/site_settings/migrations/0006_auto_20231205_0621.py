# Generated by Django 3.2.23 on 2023-12-05 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('wagtailcore', '0083_workflowcontenttype'),
        ('site_settings', '0005_auto_20231201_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysettings',
            name='email',
            field=models.EmailField(blank=True, help_text='Gib hier die E-Mail-Adresse ein.', max_length=100, verbose_name='E-Mail-Adresse'),
        ),
        migrations.AddField(
            model_name='mysettings',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Telefonnummer für den Footer-Bereich.', max_length=100, verbose_name='Telefon Nummer'),
        ),
        migrations.AlterField(
            model_name='mysettings',
            name='around_logo',
            field=models.ForeignKey(help_text='Das runde Logo wird global auf der Website eingesetzt.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Rundes Logo'),
        ),
        migrations.AlterField(
            model_name='mysettings',
            name='book_appointment',
            field=models.ForeignKey(help_text='Wähle eine Seite aus, mit der du den Button verlinken möchtest.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Seiten Auswahl'),
        ),
        migrations.AlterField(
            model_name='mysettings',
            name='btn_text',
            field=models.CharField(blank=True, help_text='Gib hier den Text für den Button im Header ein.', max_length=500, verbose_name='Button Text'),
        ),
        migrations.AlterField(
            model_name='mysettings',
            name='header_logo',
            field=models.ForeignKey(help_text='Das quadratisch Logo wird global auf der Website eingesetzt.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Quadratisch Logo'),
        ),
    ]
