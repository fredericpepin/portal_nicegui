from __future__ import annotations
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional

__all__ = ['navigation']


@dataclass
class Node:
    id: str
    label: str
    path: Optional[str] = None
    view: Optional[Callable] = None
    roles: tuple = ('all',)
    icon: Optional[str] = None
    children: List[str] = field(default_factory=list)
    is_module: bool = False


class Nav:
    def __init__(self) -> None:
        self.nodes: Dict[str, Node] = {}
        self.root: List[str] = []

    def register_group(self, id: str, label: str, parent_id: Optional[str] = None) -> str:
        node = Node(id=id, label=label)
        self.nodes[id] = node
        if parent_id and parent_id in self.nodes:
            self.nodes[parent_id].children.append(id)
        else:
            self.root.append(id)
        return id

    def register(
        self,
        label: str,
        path: str,
        view: Callable,
        roles: tuple = ('all',),
        parent_id: Optional[str] = None,
        id: Optional[str] = None,
        icon: Optional[str] = None,
    ) -> str:
        node_id = id or (path if path else label.lower().replace(' ', '-'))
        node = Node(id=node_id, label=label, path=path, view=view, roles=roles, icon=icon)
        self.nodes[node_id] = node
        if parent_id and parent_id in self.nodes:
            self.nodes[parent_id].children.append(node_id)
        else:
            self.root.append(node_id)
        return node_id


navigation = Nav()