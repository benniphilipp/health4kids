from wagtail import hooks
import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler
from draftjs_exporter.dom import DOM

@hooks.register('register_rich_text_features')
def register_custom_inline_feature(features):
    feature_name = 'custom-inline'
    type_ = 'CUSTOM_INLINE'

    css_class = 'image-underline'

    control = {
        'type': type_,
        'label': 'Red',
        'description': 'Image underline',
        'style': {'color': '#B09B8A'},
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    features.register_converter_rule('contentstate', feature_name, {
        'from_database_format': {'span[class=image-underline]': InlineStyleElementHandler(type_)},
        'to_database_format': {'style_map': {type_: {'element': 'span', 'props': {'class': css_class}}}},
    })

    features.default_features.append('custom-inline')
    

@hooks.register('register_rich_text_features')
def register_custom_inline_feature(features):
    feature_name = 'custom-inline-blue'
    type_ = 'CUSTOM_INLINE_BLUE'

    css_class = 'image-underline-blue'

    control = {
        'type': type_,
        'label': 'Blue',
        'description': 'Image underline blue',
        'style': {'color': '#0B2948'},
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    features.register_converter_rule('contentstate', feature_name, {
        'from_database_format': {'span[class=image-underline-blue]': InlineStyleElementHandler(type_)},
        'to_database_format': {'style_map': {type_: {'element': 'span', 'props': {'class': css_class}}}},
    })

    features.default_features.append('custom-inline-blue')



# from wagtail import hooks

# import wagtail.admin.rich_text.editors.draftail.features as draftail_features
# from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler


# from wagtail import hooks
# from wagtail import blocks
# from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler

# import wagtail.admin.rich_text.editors.draftail.features as draftail_features
# from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler

# @hooks.register('register_rich_text_features')
# def register_custom_feature(features):
#     feature_name = 'custom-attribute'
#     type_ = 'span'
#     tag = 'span'

#     # Konfigurieren Sie, wie Draftail das Feature in seiner Symbolleiste behandelt.
#     control = {
#         'type': type_,
#         'label': 'C',
#         'description': 'Custom Attribute',
#     }

#     class CustomInlineStyleElementHandler(InlineStyleElementHandler):
#         def create_inline_style(self, state, style, contentstate):
#             # Hinzufügen des Datenattributs "custom-attribute" zum Stil
#             return super().create_inline_style(state, {'data-custom-attribute': 'custom-value'}, contentstate)

#     features.register_editor_plugin(
#         'draftail', feature_name, draftail_features.InlineStyleFeature(control)
#     )

#     features.register_converter_rule('contentstate', feature_name, {
#         'from_database_format': {tag: CustomInlineStyleElementHandler(type_)},
#         'to_database_format': {type_: {'element': tag, 'props': {'data-custom-attribute': 'custom-value'}}},
#     })




# @hooks.register('register_rich_text_features')
# def register_custom_underline_feature(features):
#     feature_name = 'UnderlineSpan'
#     type_ = 'span'
#     tag = 'span'

#     class CustomUnderlineStyle(blocks.RichTextBlock):
#         def get_api_representation(self, value, context=None):
#             api_representation = super().get_api_representation(value, context=context)
#             api_representation['type'] = 'underline_span'
#             return api_representation

#     # Konfigurieren Sie, wie Draftail das Feature in seiner Symbolleiste behandelt.
#     control = {
#         'type': type_,
#         'label': '☆',
#         'description': 'span',
#         'element': 'span',  # Hier wird die element-Eigenschaft auf 'span' gesetzt
#         'style': {'textDecoration': 'underline'},
#     }

#     # Registrieren Sie das Feature-Plugin für Draftail
#     features.register_editor_plugin(
#         'draftail', feature_name, draftail_features.InlineStyleFeature(control)
#     )

#     # Konfigurieren Sie die Content-Transformation zwischen DB und Editor
#     db_conversion = {
#         'from_database_format': {tag: InlineStyleElementHandler(type_)},
#         'to_database_format': {'style_map': {type_: tag}},
#     }

#     # Registrieren Sie die Content-Transformation-Regel
#     features.register_converter_rule('contentstate', feature_name, db_conversion)

#     # (optional) Fügen Sie das Feature zur Standard-Feature-Liste hinzu
#     features.default_features.append('UnderlineSpan')




# # @hooks.register('register_rich_text_features')
# # def register_mark_feature(features):
# #     feature_name = 'Underline span'
# #     type_ = 'span'
# #     tag = 'span'

# #     # Fügen Sie Ihre CSS-Klasse hinzu
# #     css_class = 'my-custom-class'

# #     # Konfigurieren Sie, wie Draftail das Feature in seiner Symbolleiste behandelt.
# #     control = {
# #         'type': type_,
# #         'label': '☆',
# #         'description': 'span',
# #         'style': {'textDecoration': 'line-through'},
# #     }

# #     # Registrieren Sie das Feature-Plugin für Draftail
# #     features.register_editor_plugin(
# #         'draftail', feature_name, draftail_features.InlineStyleFeature(control)
# #     )

# #     # Konfigurieren Sie die Content-Transformation zwischen DB und Editor
# #     db_conversion = {
# #         'from_database_format': {tag: InlineStyleElementHandler(type_)},
# #         'to_database_format': {'style_map': {type_: tag}},
# #     }

# #     # Registrieren Sie die Content-Transformation-Regel
# #     features.register_converter_rule('contentstate', feature_name, db_conversion)

# #     # (optional) Fügen Sie das Feature zur Standard-Feature-Liste hinzu
# #     features.default_features.append('Underline span')


# # 1. Use the register_rich_text_features hook.
# # @hooks.register('register_rich_text_features')
# # def register_mark_feature(features):
# #     feature_name = 'Underline span'
# #     type_ = 'span'
# #     tag = 'span'

# #     # Fügen Sie Ihre CSS-Klasse hinzu
# #     css_class = 'my-custom-class'

# #     # Konfigurieren Sie, wie Draftail das Feature in seiner Symbolleiste behandelt.
# #     control = {
# #         'type': type_,
# #         'label': '☆',
# #         'description': 'span',
# #         'style': {'textDecoration': 'underline', 'className': css_class},
# #     }

# #     # Registrieren Sie das Feature-Plugin für Draftail
# #     features.register_editor_plugin(
# #         'draftail', feature_name, draftail_features.InlineStyleFeature(control)
# #     )

# #     # Konfigurieren Sie die Content-Transformation zwischen DB und Editor
# #     db_conversion = {
# #         'from_database_format': {tag: InlineStyleElementHandler(type_)},
# #         'to_database_format': {'style_map': {type_: tag}},
# #     }

# #     # Registrieren Sie die Content-Transformation-Regel
# #     features.register_converter_rule('contentstate', feature_name, db_conversion)


# #     # 6. (optional) Add the feature to the default features list to make it available
# #     # on rich text fields that do not specify an explicit 'features' list
# #     features.default_features.append('Underline span')
    
