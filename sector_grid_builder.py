# Terminal Sector Grid Builder | Module 002

# Defines vertical segmentation zones (altitude bands) for controlled airspace
# Technical Reference: HG 1.7, HG 6.2 — ICAO Structured Sector Logic

import numpy as np

# --- Step 1: Define X/Y grid coordinates
x = np.linspace(0, 100, 5)  # horizontal range
y = np.linspace(0, 100, 5)

# --- Step 2: Define altitude layers for vertical stratification
altitude_bands = [0, 100, 200, 300]  # in feet

# --- Step 3: Generate grid points across altitude layers
grid_points = []
for z in altitude_bands:
    for xi in x:
        for yi in y:
            grid_points.append([xi, yi, z])

# Print structured vertical grid
print("3D Sector Grid Points with Altitude Bands:")
for pt in grid_points:
    print(f"X: {pt[0]:.1f}, Y: {pt[1]:.1f}, Altitude: {pt[2]:.1f} ft")

# Note: These points define control nodes for procedural volume modeling.
