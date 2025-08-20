from nicegui import ui

from dg_portal.commons.layouts import default_layout
from dg_portal.commons.registry import register


@register.module('finance', 'Finance', '/finance')
def finance_home():
    default_layout(active='/finance')
    ui.label('Finance').classes('text-h4')
    ui.label('Overview').classes('text-subtitle1')