from django.db import models
import json

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
    
    template = "contact/contact_page.html"

    landing_page_template = "contact/contact_page_landing.html"
    
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

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

    # def get_data_fields(self):
    #     data_fields = [
    #         ('username', 'Username'),
    #     ]
    #     data_fields += super().get_data_fields()

    #     return data_fields

    # def process_form_submission(self, form):
    #     return self.get_submission_class().objects.create(
    #         form_data=form.cleaned_data,
    #         page=self, user=form.user
    #     )
        


