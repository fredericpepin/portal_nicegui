from nicegui import ui

from dg_portal.commons.layouts import default_layout
from dg_portal.commons.registry import register


@register.module('operations', 'Operations', '/operations')
def operations_home():
    default_layout(active='/operations')
    ui.label('Operations').classes('text-h4')
    ui.label('Overview').classes('text-subtitle1')