from django.db import models

from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList
from wagtail.models import Page

from streams.blocks import TextOneImage, Accordion, Video, ContactSteps, ImageBulletPoints

class Coaching(Page):
    template = "coaching_page.html"

    # StreamField
    content = StreamField([
        ('text_one_image', TextOneImage()),
        ('accordion', Accordion()),
        ('video', Video()),
        ('contact_steps', ContactSteps()),
        ('image_bullet_points', ImageBulletPoints()),
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
    