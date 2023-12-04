# Generated by Django 3.2.23 on 2023-12-03 11:14

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_homepage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.fields.StreamField([('headline_text_horizontal_line', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(blank=True, form_classname='Titel')), ('subline', wagtail.blocks.CharBlock(blank=True, max_length=350)), ('paragraph', wagtail.blocks.RichTextBlock(blank=True, form_classname='Text')), ('link_type', wagtail.blocks.ChoiceBlock(choices=[('page', 'Verlinkung Intern'), ('extern', 'Verlinkung Extern')], label='Auswahl Verlinkung')), ('button_page', wagtail.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.blocks.URLBlock(required=False)), ('button_text', wagtail.blocks.CharBlock(default='Mehr erfahren', max_length=40, required=True)), ('image_repeat', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))])))])), ('fancy_box', wagtail.blocks.StructBlock([('headline', wagtail.blocks.RichTextBlock(blank=True, form_classname='Titel')), ('paragraph', wagtail.blocks.RichTextBlock(blank=True, form_classname='Text')), ('cards_reapeat', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(max_length=40, required=True)), ('text', wagtail.blocks.TextBlock(max_length=200, required=True)), ('button_page', wagtail.blocks.PageChooserBlock(required=False))])))])), ('testimonial_silder', wagtail.blocks.StructBlock([('skyline', wagtail.blocks.RichTextBlock(blank=True, form_classname='Skyline', max_length=66)), ('headline', wagtail.blocks.RichTextBlock(blank=True, form_classname='Titel', max_length=140)), ('testimonial_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('slider_type', wagtail.blocks.ChoiceBlock(choices=[('slider', 'Slider Inhalt'), ('testimonial', 'Testimonial Slider')], label='Slider Auswahl')), ('slider_reapeat', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock(max_length=400, required=True)), ('img_person', wagtail.images.blocks.ImageChooserBlock(required=False)), ('name_person', wagtail.blocks.TextBlock(max_length=100, required=False)), ('job_person', wagtail.blocks.TextBlock(max_length=100, required=False))])))]))], blank=True, use_json_field=True),
        ),
    ]
