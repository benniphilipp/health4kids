from django import template

from ..models import Menu

register = template.Library()


@register.simple_tag()
def get_menu(slug):
    return Menu.objects.get(slug=slug)


@register.filter
def menu_exists(slug):
    try:
        Menu.objects.get(slug=slug)
        return True
    except Menu.DoesNotExist:
        return False
