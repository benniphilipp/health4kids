from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.images import get_image_model
from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList

from streams.blocks import GalleryImageText, FancyBox, TestimonialSilder, ImageText, MediaMasonry, PromoBox, LinkCards

class HomePage(Page):
    template = "home/home_page.html"
    max_count = 1
    subpage_types = ["coaching.Coaching", "legal.legal", "contact.FormPage"]

    skyline = models.CharField(
        blank=True, 
        max_length=96, 
        verbose_name="Skyline",
        help_text="Die Skyline ist kein kleiner Text mit braunen hintergund, mit 96 Zeichen.")
    
    headline = RichTextField(
        blank=True, 
        max_length=122, 
        verbose_name="Überschrift",
        help_text="Hier ist der Platz für eine aussagekräftige Überschrift, um deine Webseitenbesucher zu begeistern, mit 122 Zeichen.",
        features=['h1', 'h2', 'custom-inline', 'custom-inline-blue'])
    
    subline = RichTextField(
        blank=True,
        max_length=550, 
        verbose_name="Unterzeile", 
        help_text="Die Unterzeile wird in Rot dargestellt, ist auf maximal 550 Zeichen begrenzt und kein Pflichtfeld. Du kannst es gerne leer lassen!",
        features=['h1', 'h2', 'custom-inline', 'custom-inline-blue'])
    
    # Hero Image
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hintergrund Bild"
    )
    
    # Auswahl Link
    link_choice = models.CharField(
        max_length=20,
        choices=[
            ('page', 'Verlinkung intern'),
            ('extern', 'Verlinkung extern'),
        ],
        verbose_name="Auswahl",
        default='page', 
        help_text='Bitte wähle aus, was du verlinken möchtest: eine externe Seite oder eine interne Seite.'
    )   
    
    # BTN Text 
    btn_text = models.CharField(
        blank=True, 
        max_length=90, 
        verbose_name="Dein individueller Buttontext",
        help_text="Denk dir einen ansprechenden Text aus, der den Benutzer nach mehr verlangen lässt.",
        )
    
    # Link intern
    page_link = models.ForeignKey(
        Page,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Seitenauswahl",
        help_text="Die Seite muss öffentlich sein, damit Besucher deine Website erreichen können.",
        related_name='+',
    )
    
    # Link extern 
    link_url = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="Websiten-URL",
        help_text="Hier kannst du eine Wunschwebsite verlinken. Achte darauf, dass diese Seite unter https erreichbar ist."
    )
    
    # StreamField
    content = StreamField([
        ('headline_text_horizontal_line', GalleryImageText()),
        ('fancy_box', FancyBox()),
        ('testimonial_silder', TestimonialSilder()),
        ('image_text', ImageText()),
        ('media_masonry', MediaMasonry()),
        ('promo_box', PromoBox()),
        ('link_cards', LinkCards()),
    ], 
    blank=True,           
    use_json_field=True)
    
    content_stream = Page.content_panels + [
        FieldPanel('content'),
    ]
    
    content_panels = Page.content_panels + [
        FieldPanel('hero_image'),
        FieldPanel('skyline', classname="max_length-96"),
        FieldPanel('headline', classname="max_length-122"),
        FieldPanel('subline', classname="max_length-550"),
        FieldPanel('link_choice'),
        FieldPanel('link_url'),
        FieldPanel('page_link'),
        FieldPanel('btn_text', classname="max_length-90"),
    ]

    # Admin Tabs
    edit_handler = TabbedInterface([
        ObjectList(content_stream, heading='Inhalt deiner Website'),
        ObjectList(content_panels, heading='Startseiten-Header'),
        ObjectList(Page.promote_panels, heading='Seo-Einstellungen'),
        ObjectList(Page.settings_panels, heading='Einstellungen'),
    ])
    
    
    
    
