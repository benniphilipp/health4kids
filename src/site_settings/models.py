from django.db import models


from wagtail.admin.panels import FieldPanel, MultiFieldPanel, TabbedInterface, ObjectList
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting


@register_setting
class CookieBannerSettings(BaseSiteSetting):
    banner_text = models.TextField(verbose_name="Text des Cookie Banners")
    banner_accept_button_text = models.CharField(max_length=255, default="Cookies akzeptieren", verbose_name="Text des Akzeptieren-Buttons")
    banner_decline_button_text = models.CharField(max_length=255, default="Ablehnen", verbose_name="Text des Ablehnen-Buttons")

    privacy_policy  = models.ForeignKey(
        'wagtailcore.Page', null=True,blank=True, on_delete=models.SET_NULL, verbose_name="Datenschutz Seite", related_name='+', help_text="Wähle deine Datenschutzseite aus."
    )

    marketing = models.CharField(max_length=255, default="Marketing Code Beschreibung", verbose_name="Marketing")
    javascript_code = models.TextField(blank=True, null=True, verbose_name="Google Tag Manager Code GTM-KLTQ3K72")

    class Meta:
        verbose_name = "Cookie Banner Einstellungen"

    
@register_setting
class MySettings(BaseSiteSetting):
    
    header_logo = models.ForeignKey(
        'wagtailimages.Image', null=True,blank=True, on_delete=models.SET_NULL, verbose_name="Quadratisch Logo", related_name='+', help_text="Das quadratisch Logo wird global auf der Website eingesetzt."
    )
    
    around_logo = models.ForeignKey(
        'wagtailimages.Image', null=True,blank=True, on_delete=models.SET_NULL, verbose_name="Rundes Logo", related_name='+', help_text="Das runde Logo wird global auf der Website eingesetzt."
    )
    
    book_appointment  = models.ForeignKey(
        'wagtailcore.Page', null=True,blank=True, on_delete=models.SET_NULL, verbose_name="Seiten Auswahl", related_name='+', help_text="Wähle eine Seite aus, mit der du den Button verlinken möchtest."
    )
    
    btn_text = models.CharField(max_length=500,blank=True,null=True,verbose_name="Button Text", help_text="Gib hier den Text für den Button im Header ein.")
    
    phone_number = models.CharField(max_length=100,blank=True,null=True,verbose_name="Telefon Nummer", help_text="Telefonnummer für den Footer-Bereich.")
    
    email = models.EmailField(max_length=100,blank=True,null=True,verbose_name="E-Mail-Adresse", help_text="Gib hier die E-Mail-Adresse ein.")
    
    
    facebook = models.URLField(blank=True, null=True, help_text="Link zu deiner Facebook-Seite.")
    instagram = models.URLField(blank=True, null=True, help_text="Link zu deiner Instagram-Seite.")
    whatsapp = models.CharField(blank=True, null=True, max_length=100, help_text="Deine WhatsApp-Nummer.")
    
    social_media = [
        FieldPanel("facebook"),
        FieldPanel("instagram"),
        FieldPanel("whatsapp"),
    ]
    
    footer_panel = [
       FieldPanel("phone_number"), 
       FieldPanel("email"), 
    ]
    
    header_panel = [
        FieldPanel("header_logo"),
        FieldPanel("around_logo"),
    ]
    
    button_panel = [
        FieldPanel("book_appointment"),
        FieldPanel("btn_text"),
    ]
    
    edit_handler = TabbedInterface([
        ObjectList(header_panel, heading='Header'),
        ObjectList(button_panel, heading='Button'),
        ObjectList(footer_panel, heading='Footer'),
        ObjectList(social_media, heading='Social Media'),
    ])  
    
    class Meta:
        verbose_name = "Einstellungen"