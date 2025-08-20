from nicegui import ui

from dg_portal.commons.layouts import default_layout
from dg_portal.commons.registry import register


@register.sub_module('prod-mgmt', 'Production Management', '/operations/prod-mgmt', parent='operations')
def prod_mgmt_home():
    default_layout(active='/operations/prod-mgmt')
    ui.label('Production Management').classes('text-h4')
    ui.label('Plan, release and track production orders').classes('text-subtitle1')