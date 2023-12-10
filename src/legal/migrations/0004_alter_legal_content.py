# Generated by Django 3.2.23 on 2023-12-10 15:04

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('legal', '0003_alter_legal_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legal',
            name='content',
            field=wagtail.fields.StreamField([('textfield_full_width', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'p', 'a', 'pw-dark-blue', 'pw-white', 'pw-red', 'pw-brown', 'custom-inline', 'custom-inline-blue', 'ol', 'ul', 'bold', 'italic'], help_text='Textfeld gesamte Breite, maximal 10.000 Zeichen.', label='Fließtextfeld', max_length=10000, required=True))]))], blank=True, use_json_field=True),
        ),
    ]
