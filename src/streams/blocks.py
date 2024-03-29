from django.db import models

from wagtail import blocks
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import RichTextBlock


'''Fragebogen Iframe'''
class QuestionnaireIframe(blocks.StructBlock):
    
    # Überschrift
    headline = blocks.RichTextBlock(
        required=True,
        max_length=96,
        label="Überschrift",
        features=['h2', 'pw-dark-blue', 'pw-white', 'pw-red', 'pw-brown', 'custom-inline', 'custom-inline-blue'],
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
        features=['custom-inline', 'custom-inline-blue', 'link', 'ol', 'ul', 'bold', 'italic'])
    
    # Iframe
    typeform = blocks.CharBlock(
        required=True, 
        label="Typeform iframe",
        help_text="Hier kannst du dein Fragebogen einbinden.")
    
    class Meta:
        template = 'typeform.html'
        icon = 'edit'
        label = "Typeform Fragebogen"


'''Imagebulletpoints'''
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
        features=['h2', 'pw-dark-blue', 'pw-white', 'pw-red', 'pw-brown', 'custom-inline', 'custom-inline-blue'],
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
        features=['custom-inline', 'custom-inline-blue', 'link', 'ol', 'ul', 'bold', 'italic'])
    
    
    class Meta:
       template = 'image_bullet_points.html' 
       icon = 'edit'
       label = "Ein Bild mit Aufzählungspunkten"
       help_text="Fließtext mit Bild einfach, mit einem Bild und der Möglichkeit, das Bild links und den Text rechts oder das Bild rechts und den Text links zu platzieren."


'''Contact steps'''
# Label-Feldname Anpassung
class ContactStepsBlock(blocks.StructBlock):
    titel = blocks.TextBlock(
        required=False, 
        max_length=33, 
        help_text="Maximal 33 Zeichen.", 
        label="Titel")
    
    text = blocks.TextBlock(
        required=True, 
        help_text="Maximal 320 Zeichen.", 
        max_length=320, 
        label="Text")
    
    image = ImageChooserBlock(
        required=False,
        label="Bild",
        help_text="Hier kannst du ein Bild auswählen."
    )

class ContactSteps(blocks.StructBlock):
        
    # Überschrift
    headline = blocks.RichTextBlock(
        required=True,
        max_length=96,
        label="Überschrift",
        features=['h2', 'pw-dark-blue', 'pw-white', 'pw-red', 'pw-brown', 'custom-inline', 'custom-inline-blue'],
        help_text="Kreiere eine überzeugende Überschrift, um deine Website-Besucher auf deiner Website zu halten. Maximal 96 Zeichen."
    )
    
    # Fließtextfeld
    paragraph = blocks.RichTextBlock(
        blank=True, 
        null=True,
        max_length=224,
        form_classname="max_length-364",
        label="Fließtextfeld",
        help_text="Fließtextfeld für ausreichenden Text, sodass du deine Website-Besucher optimal ansprechen kannst.",
        features=['custom-inline', 'custom-inline-blue', 'pw-dark-blue', 'pw-white', 'pw-red', 'link', 'ol', 'ul', 'bold', 'italic'])
    
    # Contact Steps
    contact_steps_reapeat = blocks.ListBlock(
        ContactStepsBlock,
        label="Kontaktschritte Karten",
        min_num = 1,
        max_num = 3,
        help_text="Hier kannst du die Schritte aufzeigen, die deine Website-Besucher gehen müssen, um mit dir in Kontakt zu treten.")

    #Button Auswahl
    link_type = blocks.ChoiceBlock(
        choices=[
            ('page', 'Verlinkung intern'),
            ('extern', 'Verlinkung extern'),
        ],
        label="Auswahl",
        default='page',
        form_classname="select-contact-steps", 
        help_text='Bitte wähle aus, was du verlinken möchtest: eine externe Seite oder eine interne Seite.'
    ) 
    
    #Button Page
    button_page = blocks.PageChooserBlock(
        required=False,
        label="Seitenauswahl",
        form_classname="select-contact-steps-page", 
        help_text="Die Seite muss öffentlich sein, damit Besucher deine Website erreichen können.")
    
    #Button link
    button_url = blocks.URLBlock(
        required=False,
        label="Websiten-URL",
        form_classname="select-contact-steps-url", 
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
        icon = 'dots-horizontal'
        label = "Kontaktschritte"
        help_text="Hier kannst du Schritte abbilden, wie eine Zusammenarbeit mit dir aussieht oder wie man mit dir in Kontakt tritt."


'''Video'''
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
        features=['h2', 'pw-dark-blue', 'pw-white', 'pw-red', 'pw-brown', 'custom-inline', 'custom-inline-blue'],
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
        features=['custom-inline', 'pw-white', 'pw-red', 'pw-brown', 'custom-inline', 'custom-inline-blue', 'link', 'ol', 'ul', 'bold', 'italic'])
    
    #Button Auswahl
    link_type = blocks.ChoiceBlock(
        choices=[
            ('page', 'Verlinkung intern'),
            ('extern', 'Verlinkung extern'),
        ],
        label="Auswahl",
        default='page', 
        form_classname="select-video",
        help_text='Bitte wähle aus, was du verlinken möchtest: eine externe Seite oder eine interne Seite.'
    )
    
    #Button Page
    button_page = blocks.PageChooserBlock(
        required=False,
        label="Seitenauswahl",
        form_classname="select-video-page",
        help_text="Die Seite muss öffentlich sein, damit Besucher deine Website erreichen können.")
    
    #Button link
    button_url = blocks.URLBlock(
        required=False,
        label="Websiten-URL",
        form_classname="select-video-url",
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


'''Accordion'''
# Label-Feldname Anpassung
class AccordionBlock(blocks.StructBlock):
    titel = blocks.TextBlock(required=False, max_length=166, help_text="Maximal 120 Zeichen.", label="Titel Accordion")
    text = blocks.TextBlock(required=True, help_text="Maximal 400 Zeichen.", max_length=400, label="Text Accordion")

    
class Accordion(blocks.StructBlock):
    
    # Überschrift
    headline = blocks.RichTextBlock(
        required=True,
        max_length=126,
        label="Überschrift",
        features=['h2', 'pw-dark-blue', 'pw-white', 'pw-red', 'pw-brown', 'custom-inline', 'custom-inline-blue'],
        help_text="Kreiere eine überzeugende Überschrift, um deine Website-Besucher auf deiner Website zu halten. Maximal 96 Zeichen."
    )
    
    # Fließtextfeld
    paragraph = blocks.RichTextBlock(
        blank=True, 
        null=True,
        max_length=364,
        form_classname="max_length-364",
        label="Fließtextfeld",
        help_text="Fließtextfeld für ausreichenden Text, sodass du deine Website-Besucher optimal ansprechen kannst, maximal 164 Zeichen.",
        features=['custom-inline', 'pw-dark-blue', 'pw-white', 'pw-red', 'pw-brown', 'custom-inline-blue', 'link', 'ol', 'ul', 'bold', 'italic'])
    
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
        form_classname="select-accordion-one",
        help_text='Bitte wähle aus, was du verlinken möchtest: eine externe Seite oder eine interne Seite.'
    ) 
    
    #Button Page
    button_page = blocks.PageChooserBlock(
        required=False,
        label="Seitenauswahl",
        form_classname="select-accordion-one-page",
        help_text="Die Seite muss öffentlich sein, damit Besucher deine Website erreichen können.")
    
    #Button link
    button_url = blocks.URLBlock(
        required=False,
        label="Websiten-URL",
        form_classname="select-accordion-one-url",
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
        icon = 'clipboard-list'
        label = "Accordion"
        help_text="Das Accordion ist dazu da, viel Text auf wenig Raum übersichtlich zu präsentieren."
    

'''Text One Image mit Wechsle bild links oder rechts'''
class TextOneImage(blocks.StructBlock):
    
    # Text links rechts
    text_position = blocks.ChoiceBlock(
        choices=[
            ('order-first', 'Bild Links & Text Rechts'),
            ('order-last', 'Bild Rechts & Text Links'),
        ],
        label="Auswahl",
        default='order-first', 
        help_text='Hier kannst du ganz leicht das Bild links oder rechts platzieren.'
    ) 
    
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
        features=['h2', 'pw-dark-blue', 'pw-white', 'pw-red', 'pw-brown', 'custom-inline', 'custom-inline-blue'],
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
        max_length=564,
        form_classname="max_length-364",
        label="Fließtextfeld",
        help_text="Fließtextfeld für ausreichenden Text, sodass du deine Website-Besucher optimal ansprechen kannst.",
        features=['custom-inline', 'custom-inline-blue', 'pw-dark-blue', 'pw-white', 'pw-red', 'pw-brown', 'link', 'ol', 'ul', 'bold', 'italic'])
    
    #Button Auswahl
    link_type = blocks.ChoiceBlock(
        choices=[
            ('page', 'Verlinkung intern'),
            ('extern', 'Verlinkung extern'),
        ],
        label="Auswahl",
        default='page', 
        form_classname="select-text-image-one",
        help_text='Bitte wähle aus, was du verlinken möchtest: eine externe Seite oder eine interne Seite.'
    ) 
    
    #Button Page
    button_page = blocks.PageChooserBlock(
        required=False,
        label="Seitenauswahl",
        form_classname="select-text-image-one-page",
        help_text="Die Seite muss öffentlich sein, damit Besucher deine Website erreichen können.")
    
    #Button link
    button_url = blocks.URLBlock(
        required=False,
        label="Websiten-URL",
        form_classname="select-text-image-one-url",
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
    

'''Textfield Full Width'''
class TextfieldFullWidth(blocks.StructBlock):
    text = blocks.RichTextBlock(
        required=True,
        max_length=10000,
        label="Fließtextfeld",
        features=['h2', 'h3', 'h4', 'p', 'link', 'pw-dark-blue', 'pw-white', 'pw-red', 'pw-brown', 'custom-inline', 'custom-inline-blue', 'ol', 'ul', 'bold', 'italic'], # Mein Fließtextfeld Test
        help_text="Textfeld gesamte Breite, maximal 10.000 Zeichen."
    ) 
    
    class Meta:
        template = 'textfield_full_width.html'
        icon = 'edit'
        label = "Fließtextfeld"
        help_text = "Textfeld gesamte Breite, gut geeignet, um viel Fließtext zu platzieren."


'''Link Karten'''
# Label-Feldname Anpassung
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
        max_length=66,
        features=['h2', 'pw-dark-blue', 'pw-white', 'pw-red', 'pw-brown', 'custom-inline', 'custom-inline-blue'],
        help_text="Hier kannst du eine Überschrift eingeben."
    )

    slider_reapeat = blocks.ListBlock(
        CustomLinkCardBlock,
        label="Benutzerdefinierte Link-Karte",
        help_text="Hier kannst du eine benutzerdefinierte Link-Karte hinzufügen.")

    
    class Meta:
        template = 'link-cards.html'
        icon = 'edit'
        label = "Link-Karten"
        help_text = "Benutzerdefinierte Link-Karten sind gut geeignet, um dem Benutzer eine Orientierung zu geben und ihn dorthin zu leiten, wo es für dich wichtig ist."


'''Promo Box'''
class PromoBox(blocks.StructBlock):
    heading = blocks.RichTextBlock(
        max_length=66,
        label="Überschrift",
        form_classname="max_length-66", 
        required=True,
        help_text="Eine aussagekräftige Überschrift, um deine Website-Besucher zu animieren, weiter zu klicken, maximal 66 Zeichen.",
        features=['h2', 'custom-inline', 'custom-inline-blue',])
    
    paragraph = blocks.RichTextBlock(
        max_length=192,
        form_classname="max_length-192", 
        required=False,
        label="Fließtextfeld",
        help_text="Beschreibe noch einmal, um was es auf der Seite gibt, die du verlinkt hast. Maximal 192 Zeichen.",
        features=['pw-dark-blue', 'pw-white', 'pw-red', 'pw-brown', 'custom-inline', 'custom-inline-blue', 'bold', 'italic'])
    
    #Button Auswahl
    link_type = blocks.ChoiceBlock(
        choices=[
            ('page', 'Verlinkung intern'),
            ('extern', 'Verlinkung extern'),
        ],
        label="Auswahl",
        default='page',
        form_classname="select-promo-box",
        help_text='Bitte wähle aus, was du verlinken möchtest: eine externe Seite oder eine interne Seite.'
    ) 
    
    #Button Page
    button_page = blocks.PageChooserBlock(
        required=False,
        label="Seitenauswahl",
        form_classname="select-promo-box-page",
        help_text="Hier kannst du eine Wunschwebsite verlinken.")
    
    #Button link
    button_url = blocks.URLBlock(
        required=False,
        label="Websiten-URL",
        form_classname="select-promo-box-url",
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
        icon = 'success'
        label = "Promo Box"
        help_text = "Promo-Box zum Hervorheben von Aktionen, die der Benutzer ausführen soll."
    

'''Media Masonry'''
# Label-Feldname Anpassung
class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)

class MediaMasonry(blocks.StructBlock):
    heading = blocks.RichTextBlock(
        features=['h2', 'pw-dark-blue', 'pw-red', 'pw-brown', 'custom-inline', 'custom-inline-blue'],
        label="Überschrift",
        max_length=33, 
        blank=True)
    
    subline = blocks.CharBlock(
        label="Unterzeile", 
        blank=True, 
        max_length=120)
    
    images = blocks.ListBlock(ImageBlock(), min_num=3, max_num=6)
    
    class Meta:
        template = 'media-masonry.html'
        icon = 'edit'
        label = "Media Masonry"
        help_text = "Eine einfache Bildergalerie: Die Bilder werden bei einem Klick auf das Bild in einem Popup angezeigt." 
           

'''Bild Text'''
# Label-Feldname Anpassung
class CustomImageRepeatBlock(blocks.StructBlock):
    image = ImageChooserBlock(
        required=True,
        label="Dein Bild",
        help_text="Hier kannst du ein Bild auswählen."
    )

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
        features=['h2', 'pw-dark-blue', 'pw-red', 'pw-brown', 'custom-inline', 'custom-inline-blue']
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
        max_length=580,
        label="Fließtextfeld",
        help_text="Die Unterzeile wird in Rot dargestellt, ist auf maximal 280 Zeichen begrenzt und kein Pflichtfeld. Du kannst es gerne leer lassen!", 
        form_classname="max_length-280",
        features=['pw-dark-blue', 'pw-white', 'pw-red', 'pw-brown', 'custom-inline', 'custom-inline-blue', 'ol', 'ul', 'bold', 'italic']
    )
    
    #Button Auswahl
    link_type = blocks.ChoiceBlock(
        choices=[
            ('page', 'Verlinkung intern'),
            ('extern', 'Verlinkung extern'),
        ],
        label="Auswahl",
        default='page', 
        form_classname="select-image-text",
        help_text='Bitte wähle aus, was du verlinken möchtest: eine externe Seite oder eine interne Seite.'
    ) 
    
    #Button Page
    button_page = blocks.PageChooserBlock(
        required=False,
        label="Seitenauswahl",
        form_classname="select-image-page",
        help_text="Die Seite muss öffentlich sein, damit Besucher deine Website erreichen können.")
    
    #Button link
    button_url = blocks.URLBlock(
        required=False,
        label="Websiten-URL",
        form_classname="select-image-url",
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
        label = "Bildtext mit farbigem Hintergrund"
        help_text= "Der Bild-Text ist dafür geeignet, reichlich Informationen mit ansprechenden Bildern bereitzustellen und sie von deiner Dienstleistung zu überzeugen."


'''Testimonial Slider'''
# Label-Feldname Anpassung
class PersonBlock(blocks.StructBlock):
    text = blocks.TextBlock(required=True, help_text="Maximal 400 Zeichen.", max_length=400, label="Text")
    img_person = ImageChooserBlock(required=False, label="Bild der Person")
    name_person = blocks.TextBlock(required=False, max_length=33, help_text="Maximal 33 Zeichen.", label="Name der Person")
    job_person = blocks.TextBlock(required=False, max_length=33, help_text="Maximal 33 Zeichen.", label="Beruf der Person")

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
        icon = 'image'
        label = "Testimonial Slider"
        help_text="Der Testimonial Slider ist geeignet, um die Stimmen deiner Kunden deinen Website-Besuchern zu zeigen."


'''Fancy Box'''
# Label-Feldname Anpassung
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

class FancyBox(blocks.StructBlock):
    min_num = 1
    max_num = 2
    
    headline = blocks.RichTextBlock(
        blank=True,
        max_length=33,
        form_classname="max_length-33", 
        label="Überschrift klein",
        features=['h2', 'pw-dark-blue', 'pw-white', 'pw-red', 'pw-brown', 'custom-inline', 'custom-inline-blue'],
        help_text="Diese Überschrift ist nur dafür geeignet, den Website-Besucher neugierig zu machen, was es auf der nächsten Seite zu entdecken gibt. Maximal 33 Zeichen.")
    
    paragraph = blocks.RichTextBlock(
        required=False,
        max_length=178,
        label="Fließtextfeld",
        help_text="Die Unterzeile wird in Rot dargestellt, ist auf maximal 178 Zeichen begrenzt und kein Pflichtfeld. Du kannst es gerne leer lassen! Maximal 178 Zeichen.",
        features=['pw-dark-blue', 'pw-white', 'pw-red', 'pw-brown', 'custom-inline', 'custom-inline-blue', 'ol', 'ul', 'bold', 'italic'], 
        form_classname="max_length-178")
    
    cards_repeat = blocks.ListBlock(CustomCardBlock, label="Deine Bilder-Galerie", help_text="Du kannst die gewünschten Bilder entweder aus der Mediathek einbinden oder extern laden.")
    
    class Meta:
        template = 'fancy-box.html'
        icon = 'edit'
        label = "Fancy Box"
        help_text= "Die Fancy Box ist perfekt geeignet, um deine Website-Besucher auf eine weitere Website von dir zu leiten"


'''Gallery Image Text'''
# Label-Feldname Anpassung
class YourRenamedStructBlock(blocks.StructBlock):
    image = ImageChooserBlock(
        required=True,
        label="Bild",
        help_text="Wähle ein Bild aus."
    )

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
        features=['h2', 'custom-inline', 'custom-inline-blue', 'pw-dark-blue', 'pw-white', 'pw-red', 'pw-brown']) # Test Überschrift auswahl
    
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
        max_length=464,
        form_classname="max_length-364",
        label="Fließtextfeld",
        help_text="Fließtextfeld für ausreichenden Text, sodass du deine Website-Besucher optimal ansprechen kannst. Maximal 464 Zeichen.",
        features=['h2', 'h3', 'h4', 'p', 'pw-dark-blue', 'pw-white', 'pw-red', 'pw-brown', 'custom-inline', 'custom-inline-blue', 'ol', 'ul', 'bold', 'italic'])
    
    #Button Auswahl
    link_type = blocks.ChoiceBlock(
        choices=[
            ('page', 'Verlinkung intern'),
            ('extern', 'Verlinkung extern'),
        ],
        label="Auswahl",
        default='page', 
        form_classname="select-gallery-image-text",
        help_text='Bitte wähle aus, was du verlinken möchtest: eine externe Seite oder eine interne Seite.'
    ) 
    
    #Button Page
    button_page = blocks.PageChooserBlock(
        required=False,
        label="Seitenauswahl",
        form_classname="select-gallery-image-text-page",
        help_text="Die Seite muss öffentlich sein, damit Besucher deine Website erreichen können.")
    
    #Button link
    button_url = blocks.URLBlock(
        required=False,
        label="Websiten-URL",
        form_classname="select-gallery-image-text-url",
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
