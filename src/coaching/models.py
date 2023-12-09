from django.db import models

from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList
from wagtail.models import Page

from streams.blocks import (
    TextOneImage, 
    Accordion, 
    Video, 
    ContactSteps, 
    ImageBulletPoints, 
    QuestionnaireIframe, 
    GalleryImageText, 
    FancyBox, 
    TestimonialSilder, 
    ImageText, 
    MediaMasonry, 
    PromoBox, 
    LinkCards)

class Coaching(Page):
    template = "coaching_page.html"
    page_description = "Erstelle einfach eine Seite mit all deinen Modulen."

    # StreamField
    content = StreamField([
        ('text_one_image', TextOneImage()),
        ('accordion', Accordion()),
        ('video', Video()),
        ('contact_steps', ContactSteps()),
        ('image_bullet_points', ImageBulletPoints()),
        ('questionnaire_iframe', QuestionnaireIframe()),
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
    
    edit_handler = TabbedInterface([
        ObjectList(content_stream, heading='Inhalt deiner Website'),
        ObjectList(Page.promote_panels, heading='Promotional'),
        ObjectList(Page.promote_panels, heading='Seo-Einstellungen'),
    ])
    
    class Meta:
        verbose_name = "Seiten"
    