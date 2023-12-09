from wagtail import hooks
import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler
from draftjs_exporter.dom import DOM
from django.utils.html import format_html


@hooks.register('register_rich_text_features')
def register_custom_inline_feature(features):
    feature_name = 'custom-inline'
    type_ = 'CUSTOM_INLINE'

    css_class = 'image-underline'

    control = {
        'type': type_,
        'label': 'BTFU',
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
        'label': 'TFBU',
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


# Text Color
# pw-dark-blue
# pw-red
# pw-white
# pw-brown

@hooks.register('register_rich_text_features')
def register_bluehighlight_feature(features):  
        
    feature_name = 'pw-brown'
    type_ = 'PW_BROWN'
    tag = f'span{feature_name}'

    control = {
        'type': type_,
        'label': 'TFW', 
        'style': {'color': '#B09B8A'},
    }
    
    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    db_conversion = {
        'from_database_format': {tag: InlineStyleElementHandler(type_)},
        'to_database_format': {
            'style_map': {
                type_: {
                    'element': tag,
                    'props': {
                        'class': 'pw-brown'
                    }
                }
            }
        },
    }

    features.register_converter_rule('contentstate', feature_name, db_conversion)






@hooks.register('register_rich_text_features')
def register_bluehighlight_feature(features):  
        
    feature_name = 'pw-white'
    type_ = 'PW_WHITE'
    tag = f'span{feature_name}'

    control = {
        'type': type_,
        'label': 'TFW', 
        'style': {'color': '#808080'},
    }
    
    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    db_conversion = {
        'from_database_format': {tag: InlineStyleElementHandler(type_)},
        'to_database_format': {
            'style_map': {
                type_: {
                    'element': tag,
                    'props': {
                        'class': 'pw-white'
                    }
                }
            }
        },
    }

    features.register_converter_rule('contentstate', feature_name, db_conversion)





@hooks.register('register_rich_text_features')
def register_bluehighlight_feature(features):  
        
    feature_name = 'pw-red'
    type_ = 'PW_RED'
    tag = f'span{feature_name}'

    control = {
        'type': type_,
        'label': 'TFR', 
        'style': {'color': '#C7202D'},
    }
    
    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    db_conversion = {
        'from_database_format': {tag: InlineStyleElementHandler(type_)},
        'to_database_format': {
            'style_map': {
                type_: {
                    'element': tag,
                    'props': {
                        'class': 'pw-red'
                    }
                }
            }
        },
    }

    features.register_converter_rule('contentstate', feature_name, db_conversion)


@hooks.register('register_rich_text_features')
def register_bluehighlight_feature(features):  
        
    feature_name = 'pw-dark-blue'
    type_ = 'PW_DARK_BLUE'
    tag = f'span{feature_name}'

    control = {
        'type': type_,
        'label': 'TFB', 
        'style': {'color': '#0B2948'},
    }
    
    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    db_conversion = {
        'from_database_format': {tag: InlineStyleElementHandler(type_)},
        'to_database_format': {
            'style_map': {
                type_: {
                    'element': tag,
                    'props': {
                        'class': 'pw-dark-blue'
                    }
                }
            }
        },
    }

    features.register_converter_rule('contentstate', feature_name, db_conversion)    