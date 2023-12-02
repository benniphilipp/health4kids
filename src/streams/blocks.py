from django.db import models

from wagtail import blocks
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import RichTextBlock


# Fancy Box Section
class FancyBox(blocks.StructBlock):
    min_num = 1
    max_num = 2
    
    headline = blocks.RichTextBlock(form_classname="Titel", blank=True)
    paragraph = blocks.RichTextBlock(form_classname="Text", blank=True)
    
    cards_reapeat = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
            ]
        )
    )
    
    class Meta:
        template = 'fancy-box.html'
        icon = 'edit'
        label = "Fancy Box"



class GalleryImageText(blocks.StructBlock):
    
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
        template = 'gallery-image-text.html'
        icon = 'edit'
        label = "Galerie Bild Text"