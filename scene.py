import numpy as np
from vispy import scene, app
from communication import SignalPool
from node import Node

# Signals

signal_pool = SignalPool()

# Generate random nodes
    
num_nodes = 100
nodes = [Node(np.random.rand(3) * 100) for _ in range(num_nodes)]
for node in nodes:
    node.subscribe(signal_pool)

for node in nodes:
    discovery_content = f"DISCOVERY\nPOS:{node.pos[0]},{node.pos[1]},{node.pos[2]}".encode()
    node.broadcast(discovery_content)

# Extract positions for visualization
pos = np.array([node.pos for node in nodes])

# Create a canvas and add a view
canvas = scene.SceneCanvas(keys='interactive', bgcolor='white', show=True)
view = canvas.central_widget.add_view()

view.camera = 'turntable'


# Create a scatter plot of the nodes
visual_nodes = scene.visuals.Markers(parent=view.scene)
visual_nodes.set_data(pos,symbol="o", size=10, face_color='green', edge_color='green')

view.camera.set_range()

if __name__ == '__main__':
    app.run()
