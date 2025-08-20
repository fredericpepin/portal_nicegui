from nicegui import ui

from dg_portal.commons.layouts import default_layout
from dg_portal.commons.registry import register


@register.module('engineering', 'Engineering', '/engineering')
def engineering_home():
    default_layout(active='/engineering')
    ui.label('Engineering').classes('text-h4')
    ui.label('Overview').classes('text-subtitle1')