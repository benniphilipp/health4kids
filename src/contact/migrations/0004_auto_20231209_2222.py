# Generated by Django 3.2.23 on 2023-12-09 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_formpage_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formpage',
            name='intro',
            field=models.CharField(max_length=96, verbose_name='Überschrift'),
        ),
        migrations.AlterField(
            model_name='formpage',
            name='thank_you_text',
            field=models.CharField(max_length=96, verbose_name='Text Danke-Seite'),
        ),
    ]
