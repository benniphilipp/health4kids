from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.images import get_image_model
from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList

class HomePage(Page):
    template = "home/home_page.html"
    max_count = 1

    skyline = models.CharField(blank=True, max_length=350, verbose_name="Skyline")
    headline = RichTextField(blank=True, features=['h1', 'h2'])
    subline = RichTextField(blank=True, features=['h1', 'h2'])
    
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
        choices=[('page', 'Verlingung Intern'), ('extern', 'Verlinkung Extern')],
        blank=True,
        verbose_name="Auswahl Verlinkung",
    )   
    
    # BTN Text 
    btn_text = models.CharField(blank=True, max_length=90, verbose_name="Button Text")
    
    # Link intern
    page_link = models.ForeignKey(
        Page,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Seiten Verlinkung",
        related_name='+',
    )
    
    # Link extern 
    link_url = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="Seiten Link Extern",
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('hero_image'),
        FieldPanel('skyline'),
        FieldPanel('headline'),
        FieldPanel('subline'),
        FieldPanel('link_choice'),
        FieldPanel('link_url'),
        FieldPanel('page_link'),
        FieldPanel('btn_text'),
    ]

    # Admin Tabs
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Hero'),
        ObjectList(Page.promote_panels, heading='Promotional'),
    ])
    
    # Image right
    # image_right = models.ForeignKey(
    # "wagtailimages.Image",
    # null=True,
    # blank=True,
    # on_delete= models.SET_NULL,
    # verbose_name="Hintergrund Rechts"
    # related_name="+"
    # )
    
    
    
