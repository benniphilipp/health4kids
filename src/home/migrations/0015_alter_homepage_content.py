# Generated by Django 3.2.23 on 2023-12-10 15:02

from django.db import migrations
import streams.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_homepage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.fields.StreamField([('headline_text_horizontal_line', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(blank=True, features=['h2', 'custom-inline', 'custom-inline-blue', 'pw-dark-blue', 'pw-white', 'pw-red', 'pw-brown'], form_classname='max_length-66', help_text='Hier ist der Platz für eine aussagekräftige Überschrift, um deine Webseitenbesucher zu begeistern.', label='Überschrift', max_length=66)), ('subline', wagtail.blocks.CharBlock(form_classname='max_length-89', help_text='Die Unterzeile wird in Rot dargestellt, ist auf maximal 89 Zeichen begrenzt und kein Pflichtfeld. Du kannst es gerne leer lassen!', label='Unterzeile', max_length=89, required=False)), ('paragraph', wagtail.blocks.RichTextBlock(blank=True, features=['h2', 'h3', 'h4', 'p', 'pw-dark-blue', 'pw-white', 'pw-red', 'pw-brown', 'custom-inline', 'custom-inline-blue', 'ol', 'ul', 'bold', 'italic'], form_classname='max_length-364', help_text='Fließtextfeld für ausreichenden Text, sodass du deine Website-Besucher optimal ansprechen kannst. Maximal 464 Zeichen.', label='Fließtextfeld', max_length=464, null=True)), ('link_type', wagtail.blocks.ChoiceBlock(choices=[('page', 'Verlinkung intern'), ('extern', 'Verlinkung extern')], form_classname='select-gallery-image-text', help_text='Bitte wähle aus, was du verlinken möchtest: eine externe Seite oder eine interne Seite.', label='Auswahl')), ('button_page', wagtail.blocks.PageChooserBlock(form_classname='select-gallery-image-text-page', help_text='Die Seite muss öffentlich sein, damit Besucher deine Website erreichen können.', label='Seitenauswahl', required=False)), ('button_url', wagtail.blocks.URLBlock(form_classname='select-gallery-image-text-url', help_text='Hier kannst du eine Wunschwebsite verlinken. Achte darauf, dass diese Seite unter https erreichbar ist.', label='Websiten-URL', required=False)), ('button_text', wagtail.blocks.CharBlock(default='Mehr erfahren', form_classname='max_length-90', help_text='Denk dir einen ansprechenden Text aus, der den Benutzer nach mehr verlangen lässt.', label='Dein individueller Buttontext', max_length=90, required=True)), ('image_repeat', wagtail.blocks.ListBlock(streams.blocks.YourRenamedStructBlock, help_text='Du kannst die gewünschten Bilder entweder aus der Mediathek einbinden oder extern laden.', label='Deine Bilder-Galerie'))])), ('fancy_box', wagtail.blocks.StructBlock([('headline', wagtail.blocks.RichTextBlock(blank=True, features=['h2', 'pw-dark-blue', 'pw-white', 'pw-red', 'pw-brown', 'custom-inline', 'custom-inline-blue'], form_classname='max_length-33', help_text='Diese Überschrift ist nur dafür geeignet, den Website-Besucher neugierig zu machen, was es auf der nächsten Seite zu entdecken gibt. Maximal 33 Zeichen.', label='Überschrift klein', max_length=33)), ('paragraph', wagtail.blocks.RichTextBlock(features=['pw-dark-blue', 'pw-white', 'pw-red', 'pw-brown', 'custom-inline', 'custom-inline-blue', 'ol', 'ul', 'bold', 'italic'], form_classname='max_length-178', help_text='Die Unterzeile wird in Rot dargestellt, ist auf maximal 178 Zeichen begrenzt und kein Pflichtfeld. Du kannst es gerne leer lassen! Maximal 178 Zeichen.', label='Fließtextfeld', max_length=178, required=False)), ('cards_repeat', wagtail.blocks.ListBlock(streams.blocks.CustomCardBlock, help_text='Du kannst die gewünschten Bilder entweder aus der Mediathek einbinden oder extern laden.', label='Deine Bilder-Galerie'))])), ('testimonial_silder', wagtail.blocks.StructBlock([('skyline', wagtail.blocks.CharBlock(form_classname='max_length-66', help_text='Skyline als kleine Überschrift, maximal 66 Zeichen.', label='Skyline', max_length=66, required=True)), ('headline', wagtail.blocks.CharBlock(blank=True, form_classname='max_length-140', help_text='Überzeuge deine Website durch sozialen Beweis, maximal 79 Zeichen.', label='Überschrift', max_length=79)), ('testimonial_image', wagtail.images.blocks.ImageChooserBlock(help_text='Ein Bild, wer für die tollen Ergebnisse verantwortlich ist.', label='Bilde', required=True)), ('slider_reapeat', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock(help_text='Maximal 400 Zeichen.', label='Text', max_length=400, required=True)), ('img_person', wagtail.images.blocks.ImageChooserBlock(label='Bild der Person', required=False)), ('name_person', wagtail.blocks.TextBlock(help_text='Maximal 33 Zeichen.', label='Name der Person', max_length=33, required=False)), ('job_person', wagtail.blocks.TextBlock(help_text='Maximal 33 Zeichen.', label='Beruf der Person', max_length=33, required=False))]), label='Slider Repeat'))])), ('image_text', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(features=['h2', 'pw-dark-blue', 'pw-red', 'pw-brown', 'custom-inline', 'custom-inline-blue'], form_classname='max_length-66', help_text='Hier ist der Platz für eine aussagekräftige Überschrift, um deine Webseitenbesucher zu begeistern, maximal 33 Zeichen..', label='Überschrift', max_length=139, required=True)), ('subline', wagtail.blocks.CharBlock(form_classname='max_length-66', help_text='Skyline als kleine Überschrift, maximal 96 Zeichen.', label='Skyline', max_length=96, required=True)), ('paragraph', wagtail.blocks.RichTextBlock(features=['pw-dark-blue', 'pw-white', 'pw-red', 'pw-brown', 'custom-inline', 'custom-inline-blue', 'ol', 'ul', 'bold', 'italic'], form_classname='max_length-280', help_text='Die Unterzeile wird in Rot dargestellt, ist auf maximal 280 Zeichen begrenzt und kein Pflichtfeld. Du kannst es gerne leer lassen!', label='Fließtextfeld', max_length=280, required=False)), ('link_type', wagtail.blocks.ChoiceBlock(choices=[('page', 'Verlinkung intern'), ('extern', 'Verlinkung extern')], form_classname='select-image-text', help_text='Bitte wähle aus, was du verlinken möchtest: eine externe Seite oder eine interne Seite.', label='Auswahl')), ('button_page', wagtail.blocks.PageChooserBlock(form_classname='select-image-page', help_text='Die Seite muss öffentlich sein, damit Besucher deine Website erreichen können.', label='Seitenauswahl', required=False)), ('button_url', wagtail.blocks.URLBlock(form_classname='select-image-url', help_text='Hier kannst du eine Wunschwebsite verlinken. Achte darauf, dass diese Seite unter https erreichbar ist.', label='Websiten-URL', required=False)), ('button_text', wagtail.blocks.CharBlock(default='Mehr erfahren', form_classname='max_length-90', help_text='Denk dir einen ansprechenden Text aus, der den Benutzer nach mehr verlangen lässt.', label='Dein individueller Buttontext', max_length=90, required=True)), ('image_repeat', wagtail.blocks.ListBlock(streams.blocks.CustomImageRepeatBlock))])), ('media_masonry', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(blank=True, features=['h2', 'pw-dark-blue', 'pw-red', 'pw-brown', 'custom-inline', 'custom-inline-blue'], label='Überschrift', max_length=33)), ('subline', wagtail.blocks.CharBlock(blank=True, label='Unterzeile', max_length=120)), ('images', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))]), max_num=6, min_num=3))])), ('promo_box', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(features=['h2', 'custom-inline', 'custom-inline-blue'], form_classname='max_length-66', help_text='Eine aussagekräftige Überschrift, um deine Website-Besucher zu animieren, weiter zu klicken, maximal 66 Zeichen.', label='Überschrift', max_length=66, required=True)), ('paragraph', wagtail.blocks.RichTextBlock(features=['pw-dark-blue', 'pw-white', 'pw-red', 'pw-brown', 'custom-inline', 'custom-inline-blue', 'bold', 'italic'], form_classname='max_length-192', help_text='Beschreibe noch einmal, um was es auf der Seite gibt, die du verlinkt hast. Maximal 192 Zeichen.', label='Fließtextfeld', max_length=192, required=False)), ('link_type', wagtail.blocks.ChoiceBlock(choices=[('page', 'Verlinkung intern'), ('extern', 'Verlinkung extern')], form_classname='select-promo-box', help_text='Bitte wähle aus, was du verlinken möchtest: eine externe Seite oder eine interne Seite.', label='Auswahl')), ('button_page', wagtail.blocks.PageChooserBlock(form_classname='select-promo-box-page', help_text='Hier kannst du eine Wunschwebsite verlinken.', label='Seitenauswahl', required=False)), ('button_url', wagtail.blocks.URLBlock(form_classname='select-promo-box-url', help_text='Hier kannst du eine Wunschwebsite verlinken. Achte darauf, dass diese Seite unter https erreichbar ist.', label='Websiten-URL', required=False)), ('button_text', wagtail.blocks.CharBlock(default='Mehr erfahren', help_text='Denk dir einen ansprechenden Text aus, der den Benutzer nach mehr verlangen lässt.', label='Dein individueller Buttontext', max_length=40, required=True))])), ('link_cards', wagtail.blocks.StructBlock([('skyline', wagtail.blocks.CharBlock(blank=True, help_text='Hier kannst du eine Skyline eingeben, maximal 66 Zeichen.', label='Skyline', max_length=66)), ('heading', wagtail.blocks.RichTextBlock(blank=True, features=['h2', 'pw-dark-blue', 'pw-white', 'pw-red', 'pw-brown', 'custom-inline', 'custom-inline-blue'], help_text='Hier kannst du eine Überschrift eingeben.', label='Überschrift', max_length=66)), ('slider_reapeat', wagtail.blocks.ListBlock(streams.blocks.CustomLinkCardBlock, help_text='Hier kannst du eine benutzerdefinierte Link-Karte hinzufügen.', label='Benutzerdefinierte Link-Karte'))]))], blank=True, use_json_field=True),
        ),
    ]
