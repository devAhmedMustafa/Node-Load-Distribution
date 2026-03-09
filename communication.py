from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from node import Node

class Message:
    def __init__(self, content: bytes, src_mac: int, dst_mac: int = None):
        self.src = src_mac
        self.dst = dst_mac
        self.content = content

class Signal:
    def __init__(self, message: Message):
        self.message = message


class SignalPool:

    def __init__(self):
        self.nodes: dict[int, "Node"] = {}
        self.node_mac_counter = 0

    def add_node(self, node: "Node"):
        node.mac = self.node_mac_counter
        self.node_mac_counter += 1
        self.nodes[node.mac] = node

    def emit(self, signal: Signal):

        if signal.message.dst is None:
            for node in self.nodes.values():
                if node.mac != signal.message.src:
                    node.receive(signal)

        elif signal.message.dst in self.nodes:
            self.nodes[signal.message.dst].receive(signal)

