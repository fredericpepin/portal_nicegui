from nicegui import ui

from dg_portal.commons.layouts import default_layout
from dg_portal.commons.registry import register


@register.page('Reports', '/reports')
def reports_page():
    default_layout(active='/reports')
    ui.label('Reports').classes('text-h4')
    ui.label('This is the reports page.')