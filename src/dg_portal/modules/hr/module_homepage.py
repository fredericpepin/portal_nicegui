from nicegui import ui

from dg_portal.commons.layouts import default_layout
from dg_portal.commons.registry import register


@register.module('hr', 'Human Resources', '/hr')
def hr_home():
    default_layout(active='/hr')
    ui.label('Human Resources').classes('text-h4')
    ui.label('Overview').classes('text-subtitle1')