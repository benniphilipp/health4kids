from django.utils.html import format_html_join
from django.utils.safestring import mark_safe
from django.templatetags.static import static

from wagtail import hooks

@hooks.register('insert_editor_js')
def editor_js():
    js_files = [
        'js/custom_admin.js',
    ]
    js_includes = format_html_join('\n', '<script src="{0}"></script>',
        ((static(filename),) for filename in js_files)
    )
    return js_includes
