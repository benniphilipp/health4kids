from django.db import models

from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList
from wagtail.models import Page

class legal(Page):
    template = "legal_page.html"
    text = models.CharField(blank=True,max_length=66, verbose_name="Hedline Text")
    
    content_panels = Page.content_panels + [
        FieldPanel('text')
    ]
    
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Hero'),
        ObjectList(Page.promote_panels, heading='Promotional'),
    ])