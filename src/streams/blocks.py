from django.db import models

from wagtail import blocks
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import RichTextBlock


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
    
    

#Testimonial
class TestimonialSilder(blocks.StructBlock):
    min_mum = 1
    max_num = 12
    
    skyline = blocks.CharBlock(form_classname="Skyline", blank=True, max_length=66)
    headline = blocks.CharBlock(form_classname="Titel", blank=True, max_length=140)
    testimonial_image = ImageChooserBlock(required=True)
    
    slider_type = blocks.ChoiceBlock(
        choices=[
            ('slider', 'Slider Inhalt'),
            ('testimonial', 'Testimonial Slider'),
        ],
        label="Slider Auswahl",
        default='slider',  # Setze den Standardwert nach Bedarf
    )
    
    slider_reapeat = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("text", blocks.TextBlock(required=True, max_length=400)),
                ("img_person", ImageChooserBlock(required=False)),
                ("name_person", blocks.TextBlock(required=False, max_length=100)),
                ("job_person", blocks.TextBlock(required=False, max_length=100)),
            ]
        )
    )
    
    class Meta:
        template = 'slider.html'
        icon = 'edit'
        label = "Slider"
    


    
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