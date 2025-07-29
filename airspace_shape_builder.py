# Airspace Shape Builder | Module 004
# Geometric shell of terminal airspace sector using altitude-based vertex logic
# Design reference: HG 6.2 — Vertical segment stacking for ICAO procedural volumes

import numpy as np

# --- Step 1: Define grid vertices for floor and ceiling
floor = np.array([
    [0, 0, 0],
    [0, 100, 0],
    [100, 100, 0],
    [100, 0, 0]
])

ceiling = np.array([
    [0, 0, 300],
    [0, 100, 300],
    [100, 100, 300],
    [100, 0, 300]
])

# --- Step 2: Stack vertical walls
walls = []
for i in range(len(floor)):
    next_i = (i + 1) % len(floor)
    wall = np.array([
        floor[i],
        floor[next_i],
        ceiling[next_i],
        ceiling[i]
    ])
    walls.append(wall)

# --- Step 3: Print wall coordinates for mesh visualization
print("Airspace Sector Geometry:")
for idx, wall in enumerate(walls):
    print(f"Wall {idx + 1}:")
    for pt in wall:
        print(f"  X: {pt[0]} | Y: {pt[1]} | Altitude: {pt[2]} ft")

# Future integration: Convert wall arrays into mesh surfaces with Open3D extrusion logic
