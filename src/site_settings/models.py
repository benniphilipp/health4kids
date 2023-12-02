from django.db import models


from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting


@register_setting
class SocialMediaSettings(BaseSiteSetting):
    """Social media settings for our custom website."""

    facebook = models.URLField(blank=True, null=True, help_text="Facebook URL")
    instagram = models.URLField(blank=True, null=True, help_text="Instagram URL")
    whatsapp = models.URLField(blank=True, null=True, help_text="Whatsapp URL")

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("instagram"),
            FieldPanel("whatsapp"),
        ], heading="Social Media")
    ]
    
    class Meta:
        verbose_name = "Einstellungen Social Media"
    
@register_setting
class MySettings(BaseSiteSetting):
    
    header_logo = models.ForeignKey(
        'wagtailimages.Image', null=True, on_delete=models.SET_NULL, verbose_name="logo quadratisch", related_name='+'
    )
    
    around_logo = models.ForeignKey(
        'wagtailimages.Image', null=True, on_delete=models.SET_NULL, verbose_name="Logo rund", related_name='+'
    )
    
    book_appointment  = models.ForeignKey(
        'wagtailcore.Page', null=True, on_delete=models.SET_NULL, verbose_name="Seiten Auswahl", related_name='+'
    )
    
    btn_text = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="Button Text",
    )
    
    panels = [
        MultiFieldPanel([
            FieldPanel("header_logo"),
            FieldPanel("around_logo"),
            FieldPanel("book_appointment"),
            FieldPanel("btn_text"),
        ], heading="Header Button")
    ]
    
    class Meta:
        verbose_name = "Einstellungen Button"