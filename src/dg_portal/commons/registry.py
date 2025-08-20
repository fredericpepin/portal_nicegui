from __future__ import annotations

from typing import Callable, Optional, Tuple

from nicegui import ui

from .nav import navigation

__all__ = ['register']


class Registry:
    def __init__(self):
        self._modules = {}  # module_id -> (label, path, homepage_view)

    def page(
        self,
        label: str,
        path: str,
        *,
        module: Optional[str] = None,
        roles: Tuple[str, ...] = ('all',),
        icon: Optional[str] = None,
    ):
        """Register a page under a module.
        
        Usage:
            @register.page('BOMs', '/engineering/boms', module='engineering', icon='list')
            def boms_page():
                ...
        """
        def decorator(view: Callable[[], None]) -> Callable[[], None]:
            # Register the UI route
            @ui.page(path)
            def _page():
                return view()
            
            # Register in navigation
            parent_id = module if module in self._modules else None
            navigation.register(
                label, path, view, roles=roles, parent_id=parent_id, icon=icon
            )
            return view
        return decorator

    def module(
        self,
        module_id: str,
        label: str,
        path: str,
        *,
        parent: Optional[str] = None,
        roles: Tuple[str, ...] = ('all',),
        icon: Optional[str] = None,
    ):
        """Register a module with its homepage.
        
        Usage:
            @register.module('engineering', 'Engineering', '/engineering', icon='build')
            def engineering_home():
                ...
        """
        def decorator(homepage_view: Callable[[], None]) -> Callable[[], None]:
            # Store module info
            self._modules[module_id] = (label, path, homepage_view)
            
            # Create navigation group with the path (makes the header clickable)
            group_node = navigation.register_group(module_id, label, parent_id=parent)
            # Set the path and icon on the group node
            navigation.nodes[group_node].path = path
            navigation.nodes[group_node].icon = icon
            navigation.nodes[group_node].view = homepage_view
            navigation.nodes[group_node].is_module = True
            
            # Register homepage route
            @ui.page(path)
            def _homepage():
                return homepage_view()
            return homepage_view
        return decorator

    def sub_module(
        self,
        sub_module_id: str,
        label: str,
        path: str,
        *,
        parent: str,
        roles: Tuple[str, ...] = ('all',),
        icon: Optional[str] = None,
    ):
        """Register a sub-module under a parent module.
        
        Usage:
            @register.sub_module('prod-mgmt', 'Production Management', '/operations/prod-mgmt', parent='operations', icon='settings')
            def prod_mgmt_home():
                ...
        """
        def decorator(homepage_view: Callable[[], None]) -> Callable[[], None]:
            # Store sub-module info
            self._modules[sub_module_id] = (label, path, homepage_view)
            
            # Create navigation group under parent with the path (makes the header clickable)
            group_node = navigation.register_group(sub_module_id, label, parent_id=parent)
            # Set the path and icon on the group node
            navigation.nodes[group_node].path = path
            navigation.nodes[group_node].icon = icon
            navigation.nodes[group_node].view = homepage_view
            navigation.nodes[group_node].is_module = True
            
            # Register homepage route
            @ui.page(path)
            def _homepage():
                return homepage_view()
            return homepage_view
        return decorator


register = Registry()