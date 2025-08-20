from nicegui import ui

from dg_portal.commons.layouts import default_layout
from dg_portal.commons.registry import register


@register.module('marketing', 'Marketing', '/marketing')
def marketing_home():
    default_layout(active='/marketing')
    ui.label('Marketing').classes('text-h4')
    ui.label('Overview').classes('text-subtitle1')