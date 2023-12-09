from django.db import models
import json
from datetime import date
from wagtail.admin.mail import send_mail
from django.conf import settings
from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from wagtail.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField, AbstractFormSubmission


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')


class FormPage(AbstractEmailForm):
    page_description = "Hier kannst du individuelle Kontaktseiten nach deinem Bedarf erstellen."
    
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    # template = "contact_page.html"
    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    def send_mail(self, form):
        print("send_mail method called")

        # Email addresses are parsed from the FormPage's addresses field
        addresses = [x.strip() for x in self.to_address.split(',')]

        # Subject can be adjusted (adding submitted date), be sure to include the form's defined subject field
        submitted_date_str = date.today().strftime('%x')
        subject = f"{self.subject} - {submitted_date_str}"

        send_mail(subject, self.render_email(form), addresses, self.from_address,)
        
        
    class Meta:
        verbose_name = "Kontaktseite"


    
        



class CustomFormSubmission(AbstractFormSubmission):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def get_data(self):
        form_data = super().get_data()
        form_data.update({
            'username': self.user.username,
        })

        return form_data
        

        


