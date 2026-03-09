import numpy as np
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from node import Node

class Route:
    def __init__(self, node1: "Node", node2: "Node"):
        self.node1 = node1
        self.node2 = node2
        self.distance = np.linalg.norm(node1.pos - node2.pos)

class RouteGraph:
    def __init__(self, src: "Node"):
        self.src = src
        self.routes = []
        self.route_table = {}

    def add_route(self, dst: "Node"):
        route = Route(self.src, dst)
        self.routes.append(route)
        self.route_table[(self.src, dst)] = route