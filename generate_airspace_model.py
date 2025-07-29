import trimesh
import numpy as np

# Dummy geometry to start — replace with your real shapes later
vertices = np.array([
    [0, 0, 0],
    [50, 0, 100],
    [0, 50, 100],
    [50, 50, 0]
])

faces = np.array([
    [0, 1, 2],
    [0, 2, 3],
    [1, 2, 3],
    [0, 1, 3]
])

mesh = trimesh.Trimesh(vertices=vertices, faces=faces)
mesh.export('airspace.glb')
print("✅ airspace.glb generated.")
