# Generated by Django 3.2.23 on 2023-12-05 14:26

from django.db import migrations
import streams.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_alter_homepage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.fields.StreamField([('headline_text_horizontal_line', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(blank=True, features=['h2', 'custom-inline', 'custom-inline-blue'], form_classname='max_length-66', help_text='Hier Hilfe-Text einfügen', label='Überschrift', max_length=66)), ('subline', wagtail.blocks.CharBlock(form_classname='max_length-89', help_text='Die Unterzeile wird in Rot dargestellt, ist auf maximal 89 Zeichen begrenzt und kein Pflichtfeld. Du kannst es gerne leer lassen!', label='Unterzeile', max_length=89, required=False)), ('paragraph', wagtail.blocks.RichTextBlock(blank=True, features=['h2', 'custom-inline', 'custom-inline-blue', 'ol', 'ul', 'bold', 'italic'], form_classname='max_length-150', help_text='Fließtextfeld für ausreichenden Text, sodass du deine Website-Besucher optimal ansprechen kannst.', label='Fließtextfeld', max_length=150, null=True)), ('link_type', wagtail.blocks.ChoiceBlock(choices=[('page', 'Verlinkung intern'), ('extern', 'Verlinkung extern')], help_text='Bitte wähle aus, was du verlinken möchtest: eine externe Seite oder eine interne Seite.', label='Auswahl')), ('button_page', wagtail.blocks.PageChooserBlock(help_text='Die Seite muss öffentlich sein, damit Besucher deine Website erreichen können.', label='Seitenauswahl', required=False)), ('button_url', wagtail.blocks.URLBlock(help_text='Hier kannst du eine Wunschwebsite verlinken. Achte darauf, dass diese Seite unter https erreichbar ist.', label='Websiten-URL', required=False)), ('button_text', wagtail.blocks.CharBlock(default='Mehr erfahren', form_classname='max_length-90', help_text='Denk dir einen ansprechenden Text aus, der den Benutzer nach mehr verlangen lässt.', label='Dein individueller Buttontext', max_length=90, required=True)), ('image_repeat', wagtail.blocks.ListBlock(streams.blocks.YourRenamedStructBlock, help_text='Du kannst die gewünschten Bilder entweder aus der Mediathek einbinden oder extern laden.', label='Deine Bilder-Galerie'))])), ('fancy_box', wagtail.blocks.StructBlock([('headline', wagtail.blocks.RichTextBlock(blank=True, form_classname='Titel')), ('paragraph', wagtail.blocks.RichTextBlock(blank=True, form_classname='Text')), ('cards_reapeat', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(max_length=40, required=True)), ('text', wagtail.blocks.TextBlock(max_length=200, required=True)), ('button_page', wagtail.blocks.PageChooserBlock(required=False))])))])), ('testimonial_silder', wagtail.blocks.StructBlock([('skyline', wagtail.blocks.CharBlock(blank=True, form_classname='Skyline', max_length=66)), ('headline', wagtail.blocks.CharBlock(blank=True, form_classname='Titel', max_length=140)), ('testimonial_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('slider_type', wagtail.blocks.ChoiceBlock(choices=[('slider', 'Slider Inhalt'), ('testimonial', 'Testimonial Slider')], label='Slider Auswahl')), ('slider_reapeat', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock(max_length=400, required=True)), ('img_person', wagtail.images.blocks.ImageChooserBlock(required=False)), ('name_person', wagtail.blocks.TextBlock(max_length=100, required=False)), ('job_person', wagtail.blocks.TextBlock(max_length=100, required=False))])))])), ('image_text', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(blank=True, form_classname='Titel')), ('subline', wagtail.blocks.CharBlock(blank=True, max_length=350)), ('paragraph', wagtail.blocks.RichTextBlock(blank=True, form_classname='Text')), ('link_type', wagtail.blocks.ChoiceBlock(choices=[('page', 'Verlinkung Intern'), ('extern', 'Verlinkung Extern')], label='Auswahl Verlinkung')), ('button_page', wagtail.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.blocks.URLBlock(required=False)), ('button_text', wagtail.blocks.CharBlock(default='Mehr erfahren', max_length=40, required=True)), ('image_repeat', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))])))])), ('media_masonry', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(blank=True, form_classname='Titel')), ('subline', wagtail.blocks.CharBlock(blank=True, max_length=350)), ('image_repeat', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))])))])), ('promo_box', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(blank=True, form_classname='Titel')), ('paragraph', wagtail.blocks.RichTextBlock(blank=True, form_classname='Text')), ('link_type', wagtail.blocks.ChoiceBlock(choices=[('page', 'Verlinkung Intern'), ('extern', 'Verlinkung Extern')], label='Auswahl Verlinkung')), ('button_page', wagtail.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.blocks.URLBlock(required=False)), ('button_text', wagtail.blocks.CharBlock(default='Mehr erfahren', max_length=40, required=True))])), ('link_cards', wagtail.blocks.StructBlock([('skyline', wagtail.blocks.CharBlock(blank=True, max_length=66)), ('heading', wagtail.blocks.RichTextBlock(blank=True, form_classname='Titel')), ('slider_reapeat', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('headline', wagtail.blocks.TextBlock(max_length=400, required=True)), ('paragraph', wagtail.blocks.TextBlock(max_length=100, required=False)), ('button_page', wagtail.blocks.PageChooserBlock(required=False))])))]))], blank=True, use_json_field=True),
        ),
    ]
