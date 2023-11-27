from django.db import models
from django_extensions.db.fields import AutoSlugField

from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import MultiFieldPanel, FieldPanel, InlinePanel, PageChooserPanel
from wagtail.models import Orderable

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

class MenuItem(Orderable):
    
    link_title = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        verbose_name="Name Link",
    )
    
    url_extern = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="Seiten Auswahl",
    )
    
    page_intern = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.CASCADE,
        verbose_name="Seite",
    )
    
    open_in_new_tab = models.BooleanField(default=False, blank=True)
    
    page = ParentalKey("Menu", related_name="menu_items")
    
    @property
    def link(self):
        if self.page_intern:
            return self.page_intern.url
        elif self.url_extern:
            return self.url_extern
        return '#'
    
    @property
    def title(self):
        if self.page_intern and not self.link_title:
            return self.page_intern.title
        elif self.link_title:
            return self.link_title
        return 'Missing Title'


@register_snippet
class Menu(ClusterableModel):
    """The main menu clusterable model."""

    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title", editable=True)
    # slug = models.SlugField()

    panels = [
        MultiFieldPanel([
            FieldPanel("title"),
            FieldPanel("slug"),
        ], heading="Menu"),
        InlinePanel("menu_items", label="Menu Item")
    ]

    def __str__(self):
        return self.title