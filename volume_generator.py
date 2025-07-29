# Terminal Airspace Volume Generator | Module 001

# This script constructs a simplified 3D airspace boundary for procedural visualization.
# Source specifications: ICAO HG 1.7 and HG 6.2

import numpy as np

# Define corner coordinates (ground and ceiling points) of the sector
lower_surface = np.array([
    [0, 0, 0],
    [0, 100, 0],
    [100, 100, 0],
    [100, 0, 0]
])

upper_surface = np.array([
    [0, 0, 300],
    [0, 100, 300],
    [100, 100, 300],
    [100, 0, 300]
])

# Combine into full boundary array
airspace_volume = np.concatenate([lower_surface, upper_surface])

# Annotated geometry data
print("Airspace Points (Ground and Ceiling):")
for pt in airspace_volume:
    print(f"X: {pt[0]:.1f}, Y: {pt[1]:.1f}, Altitude: {pt[2]:.1f} ft")

# Note: This script prepares coordinates only. Future modules will construct 3D shapes and apply ICAO sector logic.
