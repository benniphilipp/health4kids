from django.db import models

from wagtail import blocks
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import RichTextBlock

#Link Cards
class LinkCards(blocks.StructBlock):
    min_num = 1
    max_num = 3

    skyline = blocks.CharBlock(blank=True, max_length=66)
    heading = blocks.RichTextBlock(form_classname="Titel", blank=True)

    slider_reapeat = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=False)),
                ("headline", blocks.TextBlock(required=True, max_length=400)),
                ("paragraph", blocks.TextBlock(required=False, max_length=100)),
                ("button_page", blocks.PageChooserBlock(required=False)),
            ]
        )
    )
    
    class Meta:
        template = 'link-cards.html'
        icon = 'edit'
        label = "Link Cards"


#Promo Box
class PromoBox(blocks.StructBlock):
    heading = blocks.RichTextBlock(form_classname="Titel", blank=True)
    paragraph = blocks.RichTextBlock(form_classname="Text", blank=True)
    
    #Button Auswahl
    link_type = blocks.ChoiceBlock(
        choices=[
            ('page', 'Verlinkung Intern'),
            ('extern', 'Verlinkung Extern'),
        ],
        label="Auswahl Verlinkung",
        default='page',  # Setze den Standardwert nach Bedarf
    ) 
    
    #Button Page
    button_page = blocks.PageChooserBlock(required=False)
    
    #Button link
    button_url = blocks.URLBlock(required=False)
    
    #Button Text
    button_text = blocks.CharBlock(required=True, default='Mehr erfahren', max_length=40)    

    class Meta:
        template = 'promo-box.html'
        icon = 'edit'
        label = "Promo Box"
    

# Media Masonry
class MediaMasonry(blocks.StructBlock):
    min_num = 3
    max_num = 9
    
    heading = blocks.RichTextBlock(form_classname="Titel", blank=True)
    subline = blocks.CharBlock(blank=True, max_length=350)
    
    image_repeat = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
            ]
        )
    )
    
    class Meta:
        template = 'media-masonry.html'
        icon = 'edit'
        label = "Media Masonry"
        

#Bild Text
class ImageText(blocks.StructBlock):
    min_num = 1
    max_num = 3
    
    heading = blocks.RichTextBlock(form_classname="Titel", blank=True)
    subline = blocks.CharBlock(blank=True, max_length=350)
    paragraph = blocks.RichTextBlock(form_classname="Text", blank=True)
    
    #Button Auswahl
    link_type = blocks.ChoiceBlock(
        choices=[
            ('page', 'Verlinkung Intern'),
            ('extern', 'Verlinkung Extern'),
        ],
        label="Auswahl Verlinkung",
        default='page',  # Setze den Standardwert nach Bedarf
    ) 
    
    #Button Page
    button_page = blocks.PageChooserBlock(required=False)
    
    #Button link
    button_url = blocks.URLBlock(required=False)
    
    #Button Text
    button_text = blocks.CharBlock(required=True, default='Mehr erfahren', max_length=40)
    
    image_repeat = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
            ]
        )
    )
    
    class Meta:
        template = 'bild-text.html'
        icon = 'edit'
        label = "Bild Text"


# Personen Block
class PersonBlock(blocks.StructBlock):
    text = blocks.TextBlock(required=True, help_text="Maximal 400 Zeichen.", max_length=400, label="Text")
    img_person = ImageChooserBlock(required=False, label="Bild der Person")
    name_person = blocks.TextBlock(required=False, max_length=33, help_text="Maximal 33 Zeichen.", label="Name der Person")
    job_person = blocks.TextBlock(required=False, max_length=33, help_text="Maximal 33 Zeichen.", label="Beruf der Person")
    

# Testimonial Slider
class TestimonialSilder(blocks.StructBlock):
    min_mum = 1
    max_num = 12
    
    skyline = blocks.CharBlock(
        required=True,
        max_length=66,
        label="Skyline",
        help_text="Skyline als kleine Überschrift, maximal 66 Zeichen.",
        form_classname="max_length-66")
    
    headline = blocks.CharBlock(
        blank=True, 
        max_length=79,
        label="Überschrift",
        help_text="Überzeuge deine Website durch sozialen Beweis, maximal 79 Zeichen.",
        form_classname="max_length-140")
    
    testimonial_image = ImageChooserBlock(
        required=True,
        label="Bilde",
        help_text="Ein Bild, wer für die tollen Ergebnisse verantwortlich ist.",
    )
    
    slider_reapeat = blocks.ListBlock(
        PersonBlock(),
        label="Slider Repeat"
    )
        
    class Meta:
        template = 'slider.html'
        icon = 'edit'
        label = "Slider"
        help_text="Der Slider ist geeignet, um die Stimmen deiner Kunden deinen Website-Besuchern zu zeigen."


class CustomCardBlock(blocks.StructBlock):
    image = ImageChooserBlock(
        required=True,
        label="Bild",
        help_text="Wähle ein Bild aus.")
    
    title = blocks.CharBlock(
        required=True,
        max_length=33,
        label="Titel",
        help_text="Maximal 33 Zeichen.")
    
    text = blocks.TextBlock(
        required=True,
        label="Text",
        help_text="Maximal 89 Zeichen.",
        max_length=89)
    
    button_page = blocks.PageChooserBlock(
        required=False,
        label="Seitenauswahl",
        help_text="Hier kannst du eine Wunschwebsite verlinken.")


# Fancy Box Section
class FancyBox(blocks.StructBlock):
    min_num = 1
    max_num = 2
    
    headline = blocks.RichTextBlock(
        blank=True,
        max_length=33,
        form_classname="max_length-33", 
        label="Überschrift klein",
        help_text="Diese Überschrift ist nur dafür geeignet, den Website-Besucher neugierig zu machen, was es auf der nächsten Seite zu entdecken gibt.")
    
    paragraph = blocks.RichTextBlock(
        required=False,
        max_length=178,
        label="Fließtextfeld",
        help_text="Die Unterzeile wird in Rot dargestellt, ist auf maximal 178 Zeichen begrenzt und kein Pflichtfeld. Du kannst es gerne leer lassen!", 
        form_classname="max_length-178")
    
    cards_repeat = blocks.ListBlock(CustomCardBlock, label="Deine Bilder-Galerie", help_text="Du kannst die gewünschten Bilder entweder aus der Mediathek einbinden oder extern laden.")
    
    class Meta:
        template = 'fancy-box.html'
        icon = 'edit'
        label = "Fancy Box"
        help_text= "Die Fancy Box ist perfekt geeignet, um deine Website-Besucher auf eine weitere Website von dir zu leiten"


# Label feld Name anpassung
class YourRenamedStructBlock(blocks.StructBlock):
    image = ImageChooserBlock(
        required=True,
        label="Bild",
        help_text="Wähle ein Bild aus."
    )


# Label-Feldname Anpassung
class GalleryImageText(blocks.StructBlock):
    
    min_num = 1
    max_num = 3
    
    # Überschrift
    heading = blocks.RichTextBlock(
        max_length=66, 
        blank=True, 
        label="Überschrift", 
        help_text="Hier ist der Platz für eine aussagekräftige Überschrift, um deine Webseitenbesucher zu begeistern.",
        form_classname="max_length-66",
        features=['h2', 'custom-inline', 'custom-inline-blue'])
    
    # Unterzeile
    subline = blocks.CharBlock(
        required=False,
        max_length=89, 
        label="Unterzeile", 
        help_text="Die Unterzeile wird in Rot dargestellt, ist auf maximal 89 Zeichen begrenzt und kein Pflichtfeld. Du kannst es gerne leer lassen!", 
        form_classname="max_length-89")
    
    # Fließtextfeld
    paragraph = blocks.RichTextBlock(
        blank=True, 
        null=True,
        max_length=364,
        form_classname="max_length-364",
        label="Fließtextfeld",
        help_text="Fließtextfeld für ausreichenden Text, sodass du deine Website-Besucher optimal ansprechen kannst.",
        features=['h2', 'custom-inline', 'custom-inline-blue', 'ol', 'ul', 'bold', 'italic'])
    
    #Button Auswahl
    link_type = blocks.ChoiceBlock(
        choices=[
            ('page', 'Verlinkung intern'),
            ('extern', 'Verlinkung extern'),
        ],
        label="Auswahl",
        default='page', 
        help_text='Bitte wähle aus, was du verlinken möchtest: eine externe Seite oder eine interne Seite.'
    ) 
    
    #Button Page
    button_page = blocks.PageChooserBlock(
        required=False,
        label="Seitenauswahl",
        help_text="Die Seite muss öffentlich sein, damit Besucher deine Website erreichen können.")
    
    #Button link
    button_url = blocks.URLBlock(
        required=False,
        label="Websiten-URL",
        help_text="Hier kannst du eine Wunschwebsite verlinken. Achte darauf, dass diese Seite unter https erreichbar ist.")
    
    #Button Text
    button_text = blocks.CharBlock(
        required=True, 
        default='Mehr erfahren', 
        label="Dein individueller Buttontext",
        help_text="Denk dir einen ansprechenden Text aus, der den Benutzer nach mehr verlangen lässt.",
        max_length=90,
        form_classname="max_length-90")

    image_repeat = blocks.ListBlock(YourRenamedStructBlock, label="Deine Bilder-Galerie", help_text="Du kannst die gewünschten Bilder entweder aus der Mediathek einbinden oder extern laden.")
    
    class Meta:
        template = 'gallery-image-text.html'
        icon = 'edit'
        label = "Galerie-Bild- und Text"
        help_text= "Galerie-Bild- und Textabschnitt mit einem CTA-Button."
