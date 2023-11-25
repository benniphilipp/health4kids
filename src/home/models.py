from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    template = "home/home_page.html"
    max_count = 1
    
    # TODO 
    # Background Image
    # Image Left
    # 
    
