# Navigation Obstacle Proximity Engine | Module 015
# Blends terrain elevation data, known obstructions, and procedural approach vectors
# Source: ICAO Supplements, HG 2.3.2.2

# --- Example terrain surface (TDZE reference grid)
terrain_surface = [
    {"location": [0, 0], "elevation": 334},
    {"location": [100, 50], "elevation": 350},
    {"location": [200, 100], "elevation": 366}
]

# --- Known obstacles
obstacles = [
    {"type": "Tower", "location": [150, 75], "elevation": 390},
    {"type": "Crane", "location": [220, 110], "elevation": 410}
]

# --- Threshold elevation reference
tdze_elevation = 334

# --- Clearance checks
print("[Obstacle Proximity Check]")
for obs in obstacles:
    delta = obs["elevation"] - tdze_elevation
    alert = "⚠️ ALERT" if delta > 50 else "✅ Clear"
    print(f"{obs['type']} at {obs['location']}: Elevation {obs['elevation']} ft → Δ {delta} ft → {alert}")
