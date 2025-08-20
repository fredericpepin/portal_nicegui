from nicegui import ui

from dg_portal.commons.layouts import default_layout
from dg_portal.commons.registry import register


@register.page('Bill of Materials', '/operations/prod-mgmt/boms', module='prod-mgmt')
def prod_mgmt_boms():
    default_layout(active='/operations/prod-mgmt/boms')
    ui.label('Bill of Materials').classes('text-h4')
    ui.label('Import Bill of materials').classes('text-subtitle1')