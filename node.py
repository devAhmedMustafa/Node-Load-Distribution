import numpy as np
from route_graph import RouteGraph
from communication import Message, Signal, SignalPool

class Node:
    def __init__(self, pos: np.ndarray):
        self.mac = -1
        self.pos = pos
        self.route_graph = RouteGraph(self)
        self.signal_pool = None

    def subscribe(self, signal_pool: SignalPool):
        self.signal_pool = signal_pool
        signal_pool.add_node(self)
        
    def move(self, delta: np.ndarray):
        self.pos += delta

    def broadcast(self, content: bytes):
        self.signal_pool.emit(Signal(Message(content, self.mac)))

    def receive(self, signal: Signal):
        print(f"Node {self.mac} received signal from {signal.message.src}")

        msg_parts = signal.message.content.decode().split("\n")
        msg_type = msg_parts[0]

        if msg_type == "DISCOVERY":
            self.__handle_discovery(signal)
        

    def __handle_discovery(self, signal: Signal):
        ack_content = f"DISCOVERED\nACK:{self.mac},{self.pos[0]},{self.pos[1]},{self.pos[2]}".encode()
        self.signal_pool.emit(Signal(Message(ack_content, self.mac, signal.message.src)))