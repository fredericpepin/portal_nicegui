from nicegui import ui

from dg_portal.commons.layouts import default_layout
from dg_portal.commons.registry import register


@register.module('field_service', 'Field Service', '/field-service')
def field_service_home():
    default_layout(active='/field-service')
    ui.label('Field Service').classes('text-h4')
    ui.label('Overview').classes('text-subtitle1')