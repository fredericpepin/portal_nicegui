from nicegui import ui

from dg_portal.commons.layouts import default_layout
from dg_portal.commons.registry import register


@register.module('purchasing', 'Purchasing', '/purchasing')
def purchasing_home():
    default_layout(active='/purchasing')
    ui.label('Purchasing').classes('text-h4')
    ui.label('Overview').classes('text-subtitle1')