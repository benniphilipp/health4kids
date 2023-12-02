from wagtail import blocks
from wagtail.fields import RichTextField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import RichTextBlock

class GalleryImageText(blocks.StructBlock):
    
    min_num = 1
    max_num = 3
    
    heading = blocks.RichTextBlock(form_classname="Titel", blank=True)
    subline = blocks.CharBlock(blank=True, max_length=350)
    paragraph = blocks.RichTextBlock(form_classname="Text", blank=True)
    
    image_repeat = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
            ]
        )
    )
    
    class Meta:
        template = 'gallery-image-text.html'
        icon = 'edit'
        label = "Galerie Bild Text"