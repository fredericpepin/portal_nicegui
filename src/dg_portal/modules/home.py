from nicegui import ui

from dg_portal.commons.layouts import default_layout
from dg_portal.commons.registry import register


@register.page('Home', '/')
def home_page():
    default_layout(active='/')
    ui.label('Welcome to the Home Page!').classes('text-h4')
    ui.label('This is the main landing page of the application.')