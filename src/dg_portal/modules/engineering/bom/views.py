from nicegui import ui

from dg_portal.commons.layouts import default_layout
from dg_portal.commons.registry import register


@register.page('BOMs', '/engineering/boms', module='engineering')
def boms_page():
    default_layout(active='/engineering/boms')
    ui.label('Bill of Materials').classes('text-h4')
    ui.label('This is where the Bill of Materials module will be.')