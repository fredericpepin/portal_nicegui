from nicegui import ui

from dg_portal.commons.layouts import default_layout
from dg_portal.commons.registry import register


@register.module('maintenance', 'Maintenance', '/maintenance')
def maintenance_home():
    default_layout(active='/maintenance')
    ui.label('Maintenance').classes('text-h4')
    ui.label('Overview').classes('text-subtitle1')