from nicegui import ui

from dg_portal.commons.layouts import default_layout
from dg_portal.commons.registry import register


@register.module('inventory', 'Inventory / Warehouse', '/inventory')
def inventory_home():
    default_layout(active='/inventory')
    ui.label('Inventory / Warehouse').classes('text-h4')
    ui.label('Overview').classes('text-subtitle1')