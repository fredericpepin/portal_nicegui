from nicegui import app, ui
from dg_portal.commons.nav import navigation
from pathlib import Path
from dg_portal.commons.internal_paths import css, images, icons

__all__ = ['default_layout']


# Load CSS
ui.add_css(css('layouts.css'), shared=True)

def _render_nodes(ids, active: str) -> None:
    """Render navigation nodes recursively using ui.expansion for modules."""
    for node_id in ids:
        node = navigation.nodes[node_id]

        if node.children:
            # Use a unique key for user-specific session storage
            storage_key = f'expansion_{node.id}'
            
            # Read the initial state from user storage. Default to False (collapsed).
            is_expanded = app.storage.user.get(storage_key, False)

            def save_state(e, key=storage_key):
                """Save the new state to user storage."""
                app.storage.user[key] = e.value

            # Create the expansion element with the initial state and an on_change handler to save new states.
            with ui.expansion(node.label, icon=node.icon, value=is_expanded, on_value_change=save_state).classes('nav-group'):
                with ui.column().classes('nav-list w-full'):
                    _render_nodes(node.children, active)
        else:
            # Regular page link
            link_classes = 'nav-link'
            if node.path == active:
                link_classes += ' nav-link--active'
            
            if node.path:
                ui.link(node.label, node.path).classes(link_classes).props(f'icon={node.icon}' if node.icon else '')

def default_layout(active: str = ''):
    """Create the main layout with header and a styled drawer."""
    # Header with background image and centered logo
    with ui.header().classes('header'):  # <- remove elevated=True
        ui.button(icon='menu', on_click=lambda: drawer.toggle()).props('flat color=white')
        with ui.element('div').classes('header-center'):
            ui.html('<img src="/static/images/new_logo_no_background.png" class="header-logo" alt="Logo">')

    with ui.left_drawer().classes('drawer') as drawer:
        with ui.column().classes('drawer__content'):
            _render_nodes(navigation.root, active)

