from nicegui import ui

from dg_portal.commons.layouts import default_layout
from dg_portal.commons.registry import register


@register.module('sales', 'Sales / CRM', '/sales')
def sales_home():
    default_layout(active='/sales')
    ui.label('Sales / CRM').classes('text-h4')
    ui.label('Overview').classes('text-subtitle1')