from nicegui import ui

from dg_portal.commons.layouts import default_layout
from dg_portal.commons.registry import register


@register.module('platform_admin', 'Administration', '/platform-admin')
def admin_home():
    default_layout(active='/platform-admin')
    ui.label('Administration').classes('text-h4')
    ui.label('Overview').classes('text-subtitle1')