from django.db import models

from wagtail import blocks
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import RichTextBlock

# Imagebulletpoints
class ImageBulletPoints(blocks.StructBlock):
    
    # Image
    image = ImageChooserBlock(
        required=True,
        label="Bild",
        help_text="Wähle ein Bild aus."
    )
    
    # Überschrift
    headline = blocks.RichTextBlock(
        required=True,
        max_length=96,
        label="Überschrift",
        features=['h2', 'custom-inline', 'custom-inline-blue'],
        help_text="Kreiere eine überzeugende Überschrift, um deine Website-Besucher auf deiner Website zu halten. Maximal 96 Zeichen."
    )
    
    # Fließtextfeld
    paragraph = blocks.RichTextBlock(
        blank=True, 
        null=True,
        max_length=750,
        form_classname="max_length-364",
        label="Fließtextfeld",
        help_text="Fließtextfeld für ausreichenden Text, sodass du deine Website-Besucher optimal ansprechen kannst. Maximal 550 Zeichen.",
        features=['h2', 'custom-inline', 'custom-inline-blue', 'ol', 'ul', 'bold', 'italic'])
    
    
    class Meta:
       template = 'image_bullet_points.html' 
       icon = 'edit'
       label = "Ein Bild mit Aufzählungspunkten"
       help_text="Fließtext mit Bild einfach, mit einem Bild und der Möglichkeit, das Bild links und den Text rechts oder das Bild rechts und den Text links zu platzieren."







# Contact steps
class ContactStepsBlock(blocks.StructBlock):
    titel = blocks.TextBlock(
        required=False, 
        max_length=33, 
        help_text="Maximal 33 Zeichen.", 
        label="Titel Accordion")
    
    text = blocks.TextBlock(
        required=True, 
        help_text="Maximal 120 Zeichen.", 
        max_length=120, 
        label="Text Accordion")
    
    image = ImageChooserBlock(
        required=False,
        label="Bild",
        help_text="Hier kannst du ein Bild auswählen."
    )

class ContactSteps(blocks.StructBlock):
    
    min_num = 1
    max_num = 3
    
    # Überschrift
    headline = blocks.RichTextBlock(
        required=True,
        max_length=96,
        label="Überschrift",
        features=['h2', 'custom-inline', 'custom-inline-blue'],
        help_text="Kreiere eine überzeugende Überschrift, um deine Website-Besucher auf deiner Website zu halten. Maximal 96 Zeichen."
    )
    
    # Fließtextfeld
    paragraph = blocks.RichTextBlock(
        blank=True, 
        null=True,
        max_length=164,
        form_classname="max_length-364",
        label="Fließtextfeld",
        help_text="Fließtextfeld für ausreichenden Text, sodass du deine Website-Besucher optimal ansprechen kannst.",
        features=['h2', 'custom-inline', 'custom-inline-blue', 'ol', 'ul', 'bold', 'italic'])
    
    # Contact Steps
    contact_steps_reapeat = blocks.ListBlock(
        ContactStepsBlock,
        label="Kontaktschritte Karten",
        help_text="Hier kannst du die Schritte aufzeigen, die deine Website-Besucher gehen müssen, um mit dir in Kontakt zu treten.")

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
    
    class Meta:
        template = 'contact-steps.html'
        icon = 'edit'
        label = "Kontaktschritte"

    


# Video
class Video(blocks.StructBlock):
    video_url = blocks.CharBlock(
        required=True, 
        label="Video URL",
        help_text="Binde Videos von Youtbue oder Vimeo ein.")
    
    # Überschrift
    headline = blocks.RichTextBlock(
        required=True,
        max_length=96,
        label="Überschrift",
        features=['h2', 'custom-inline', 'custom-inline-blue'],
        help_text="Kreiere eine überzeugende Überschrift, um deine Website-Besucher auf deiner Website zu halten. Maximal 96 Zeichen."
    )
    
    # Fließtextfeld
    paragraph = blocks.RichTextBlock(
        blank=True, 
        null=True,
        max_length=164,
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

    class Meta:
        template = 'video.html'
        icon = 'media'
        label = 'Video Block'
        help_text = "Ein Video hilft deinen Website-Besuchern, deine Botschaft noch intensiver zu vermitteln und sie länger auf deiner Website zu halten."







# Accordion
class AccordionBlock(blocks.StructBlock):
    titel = blocks.TextBlock(required=False, max_length=33, help_text="Maximal 33 Zeichen.", label="Titel Accordion")
    text = blocks.TextBlock(required=True, help_text="Maximal 400 Zeichen.", max_length=400, label="Text Accordion")

    
class Accordion(blocks.StructBlock):
    
    # Überschrift
    headline = blocks.RichTextBlock(
        required=True,
        max_length=96,
        label="Überschrift",
        features=['h2', 'custom-inline', 'custom-inline-blue'],
        help_text="Kreiere eine überzeugende Überschrift, um deine Website-Besucher auf deiner Website zu halten. Maximal 96 Zeichen."
    )
    
    # Fließtextfeld
    paragraph = blocks.RichTextBlock(
        blank=True, 
        null=True,
        max_length=164,
        form_classname="max_length-364",
        label="Fließtextfeld",
        help_text="Fließtextfeld für ausreichenden Text, sodass du deine Website-Besucher optimal ansprechen kannst.",
        features=['h2', 'custom-inline', 'custom-inline-blue', 'ol', 'ul', 'bold', 'italic'])
    
    accordion_reapeat = blocks.ListBlock(
        AccordionBlock(),
        label="Accordion",
        help_text="Perfekt geeignet, um viel Text übersichtlich zu präsentieren."
    )
    
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
    
    class Meta:
        template = 'accordion.html'
        icon = 'edit'
        label = "Accordion"
        help_text="Das Accordion ist dazu da, viel Text auf wenig Raum übersichtlich zu präsentieren."
    
    






# Text One Image mit Wechsle bild links oder rechts
class TextOneImage(blocks.StructBlock):
    
    # Image
    image = ImageChooserBlock(
        required=True,
        label="Bild",
        help_text="Wähle ein Bild aus."
    )
    
    # Überschrift
    headline = blocks.RichTextBlock(
        required=True,
        max_length=96,
        label="Überschrift",
        features=['h2', 'custom-inline', 'custom-inline-blue'],
        help_text="Kreiere eine überzeugende Überschrift, um deine Website-Besucher auf deiner Website zu halten. Maximal 96 Zeichen."
    ) 
    
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
    
    text_position = blocks.ChoiceBlock(
        choices=[
            ('order-first', 'Bild Links & Text Rechts'),
            ('order-last', 'Bild Rechts & Text Links'),
        ],
        label="Auswahl",
        default='order-first', 
        help_text='Hier kannst du ganz leicht das Bild links oder rechts platzieren.'
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
    
    
    class Meta:
       template = 'text_one-image.html' 
       icon = 'edit'
       label = "Fließtext mit Bild einfach."
       help_text="Fließtext mit Bild einfach, mit einem Bild und der Möglichkeit, das Bild links und den Text rechts oder das Bild rechts und den Text links zu platzieren."
    
    



# Textfield Full Width
class TextfieldFullWidth(blocks.StructBlock):
    text = blocks.RichTextBlock(
        required=True,
        max_length=10000,
        label="Fließtextfeld",
        features=['h2', 'custom-inline', 'custom-inline-blue'],
        help_text="Textfeld gesamte Breite, maximal 10.000 Zeichen."
    ) 
    
    class Meta:
        template = 'textfield_full_width.html'
        icon = 'edit'
        label = "Fließtextfeld"
        help_text = "Textfeld gesamte Breite, gut geeignet, um viel Fließtext zu platzieren."


#Link Cards
class CustomLinkCardBlock(blocks.StructBlock):
    image = ImageChooserBlock(
        required=False,
        label="Bild",
        help_text="Hier kannst du ein Bild auswählen."
    )

    headline = blocks.TextBlock(
        required=True,
        max_length=400,
        label="Überschrift",
        help_text="Hier kannst du eine Überschrift eingeben."
    )

    paragraph = blocks.TextBlock(
        required=False,
        max_length=100,
        label="Absatz",
        help_text="Hier kannst du einen Absatz eingeben."
    )

    button_page = blocks.PageChooserBlock(
        required=False,
        label="Button-Seite",
        help_text="Hier kannst du eine Seite für den Button auswählen."
    )

class LinkCards(blocks.StructBlock):
    min_num = 1
    max_num = 3
    
    skyline = blocks.CharBlock(
        blank=True,
        max_length=66,
        label="Skyline",
        help_text="Hier kannst du eine Skyline eingeben, maximal 66 Zeichen."
    )
    
    heading = blocks.RichTextBlock(
        blank=True,
        label="Überschrift",
        help_text="Hier kannst du eine Überschrift eingeben."
    )

    slider_reapeat = blocks.ListBlock(
        CustomLinkCardBlock,
        label="Benutzerdefinierte Link-Karte",
        help_text="Hier kannst du eine benutzerdefinierte Link-Karte hinzufügen.")

    
    class Meta:
        template = 'link-cards.html'
        icon = 'edit'
        label = "Link-Karte"
        help_text = "Benutzerdefinierte Link-Karten sind gut geeignet, um dem Benutzer eine Orientierung zu geben und ihn dorthin zu leiten, wo es für dich wichtig ist."


#Promo Box
class PromoBox(blocks.StructBlock):
    heading = blocks.RichTextBlock(
        max_length=66,
        label="Überschrift",
        form_classname="max_length-66", 
        required=True,
        help_text="Eine aussagekräftige Überschrift, um deine Website-Besucher zu animieren, weiter zu klicken, maximal 66 Zeichen.",
        features=['h2', 'custom-inline', 'custom-inline-blue'])
    
    paragraph = blocks.RichTextBlock(
        max_length=192,
        form_classname="max_length-192", 
        required=False,
        label="Fließtextfeld",
        help_text="Beschreibe noch einmal, um was es auf der Seite gibt, die du verlinkt hast. Maximal 66 Zeichen.",
        features=['h2', 'h3', 'custom-inline', 'custom-inline-blue'])
    
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
        help_text="Hier kannst du eine Wunschwebsite verlinken.")
    
    #Button link
    button_url = blocks.URLBlock(
        required=False,
        label="Websiten-URL",
        help_text="Hier kannst du eine Wunschwebsite verlinken. Achte darauf, dass diese Seite unter https erreichbar ist.")
    
    #Button Text
    button_text = blocks.CharBlock(
        required=True, 
        default='Mehr erfahren', 
        max_length=40,
        label="Dein individueller Buttontext",
        help_text="Denk dir einen ansprechenden Text aus, der den Benutzer nach mehr verlangen lässt.")    

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
        

class CustomImageRepeatBlock(blocks.StructBlock):
    image = ImageChooserBlock(
        required=True,
        label="Dein Bild",
        help_text="Hier kannst du ein Bild auswählen."
    )
    
#Bild Text
class ImageText(blocks.StructBlock):
    min_num = 1
    max_num = 3
    
    # Überschrift
    heading = blocks.RichTextBlock(
        max_length=139, 
        required=True, 
        label="Überschrift", 
        help_text="Hier ist der Platz für eine aussagekräftige Überschrift, um deine Webseitenbesucher zu begeistern, maximal 33 Zeichen..",
        form_classname="max_length-66",
        features=['h2', 'custom-inline', 'custom-inline-blue']
    )
    
    # Subline
    subline = blocks.CharBlock(
        required=True,
        max_length=96,
        label="Skyline",
        help_text="Skyline als kleine Überschrift, maximal 96 Zeichen.",
        form_classname="max_length-66"
    )
    
    # Fließtextfeld 280
    paragraph = blocks.RichTextBlock(
        required=False,
        max_length=280,
        label="Fließtextfeld",
        help_text="Die Unterzeile wird in Rot dargestellt, ist auf maximal 280 Zeichen begrenzt und kein Pflichtfeld. Du kannst es gerne leer lassen!", 
        form_classname="max_length-280"
    )
    
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
    
    image_repeat = blocks.ListBlock(CustomImageRepeatBlock)
    
    class Meta:
        template = 'bild-text.html'
        icon = 'edit'
        label = "Bild Text"
        help_text= "Der Bild-Text ist dafür geeignet, reichlich Informationen mit ansprechenden Bildern bereitzustellen und sie von deiner Dienstleistung zu überzeugen."


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
