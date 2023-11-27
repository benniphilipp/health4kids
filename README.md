# ToDo

coching Modul erstellen
Menu Modul erstelen

Social Media Verlinkung

# Git
git add .
git commit -m <Commit>
git push origin home <branch_name>

git branch --list
git branch <Name>
git checkout <Name>

# CLI

source env/bin/activate
deactivate

python manage.py runserver

python manage.py makemigrations
python manage.py migrate

python manage.py startapp app_name

# Apps

python manage.py startapp snippets
python manage.py startapp coaching
python manage.py startapp menu









pip install Pillow


from wagtail.images.models import AbstractImage, AbstractRendition

class WebPImage(AbstractImage):
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Pfad zum ursprünglichen Bild
        original_image_path = self.file.path

        # Pfad für das WebP-Bild
        webp_image_path = f"{original_image_path.split('.')[0]}.webp"

        # Bild öffnen
        original_image = Image.open(original_image_path)

        # Bild als WebP speichern
        original_image.save(webp_image_path, format='WEBP')

        # Update des Bildpfads auf das WebP-Bild
        self.file.name = webp_image_path.split('/')[-1]
        super().save(*args, **kwargs)

    @classmethod
    def create_webp_version(cls, image_path):
        # Pfad für das WebP-Bild
        webp_image_path = f"{image_path.split('.')[0]}.webp"

        # Bild öffnen
        original_image = Image.open(image_path)

        # Bild als WebP speichern
        original_image.save(webp_image_path, format='WEBP')

        # InMemoryUploadedFile für WebP erstellen
        with open(webp_image_path, 'rb') as webp_file:
            return InMemoryUploadedFile(
                file=webp_file,
                field_name=None,
                name=webp_image_path.split('/')[-1],
                content_type='image/webp',
                size=webp_file.tell(),
                charset=None,
                content_type_extra=None,
            )
















from django.db import models
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePage(Page):
    template = "home/home_page.html"

    hero_image = models.ForeignKey(
        "WebPImage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Hintergrund Bild",
        related_name="+"
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("hero_image"),
        # Weitere Panels für andere Felder
    ]


{% if page.hero_image %}
    <img src="{{ page.hero_image.url }}" alt="Hero Image">
{% endif %}

