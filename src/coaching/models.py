from django.db import models

from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList
from wagtail.models import Page

class Coaching(Page):
    template = "coaching_page.html"
    text = RichTextField(blank=True, features=['h1', 'h1', 'h3', 'bold', 'italic'])
    
    content_panels = Page.content_panels + [
        FieldPanel('text')
    ]
    
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Hero'),
        ObjectList(Page.promote_panels, heading='Promotional'),
    ])