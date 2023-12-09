from django.db import models

from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList
from wagtail.models import Page

from streams.blocks import TextfieldFullWidth

class legal(Page):
    template = "legal_page.html"
    page_description = "Erstelle nicht nur Datenschutz- oder Impressum-Seiten. Hier kannst du auch einfach reine Fließtextseiten erstellen."
    
    content = StreamField([
        ('textfield_full_width', TextfieldFullWidth()),
    ], 
    blank=True,           
    use_json_field=True)
    
    content_stream = Page.content_panels + [
        FieldPanel('content'),
    ]
    
    edit_handler = TabbedInterface([
        ObjectList(content_stream, heading='Inhalt Webseite'),
        ObjectList(Page.promote_panels, heading='Promotional'),
    ])
    
    class Meta:
        verbose_name = "Fließtextseite"
