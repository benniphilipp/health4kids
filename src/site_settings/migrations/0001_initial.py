# Generated by Django 3.2.23 on 2023-12-08 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('wagtailcore', '0083_workflowcontenttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, help_text='Facebook URL', null=True)),
                ('instagram', models.URLField(blank=True, help_text='Instagram URL', null=True)),
                ('whatsapp', models.URLField(blank=True, help_text='Whatsapp URL', null=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Einstellungen Social Media',
            },
        ),
        migrations.CreateModel(
            name='MySettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btn_text', models.CharField(blank=True, help_text='Gib hier den Text für den Button im Header ein.', max_length=500, null=True, verbose_name='Button Text')),
                ('phone_number', models.CharField(blank=True, help_text='Telefonnummer für den Footer-Bereich.', max_length=100, null=True, verbose_name='Telefon Nummer')),
                ('email', models.EmailField(blank=True, help_text='Gib hier die E-Mail-Adresse ein.', max_length=100, null=True, verbose_name='E-Mail-Adresse')),
                ('facebook', models.URLField(blank=True, help_text='Link zu deiner Facebook-Seite.', null=True)),
                ('instagram', models.URLField(blank=True, help_text='Link zu deiner Instagram-Seite.', null=True)),
                ('whatsapp', models.CharField(blank=True, help_text='Deine WhatsApp-Nummer.', max_length=100, null=True)),
                ('around_logo', models.ForeignKey(blank=True, help_text='Das runde Logo wird global auf der Website eingesetzt.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Rundes Logo')),
                ('book_appointment', models.ForeignKey(blank=True, help_text='Wähle eine Seite aus, mit der du den Button verlinken möchtest.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Seiten Auswahl')),
                ('header_logo', models.ForeignKey(blank=True, help_text='Das quadratisch Logo wird global auf der Website eingesetzt.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Quadratisch Logo')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Einstellungen',
            },
        ),
    ]
