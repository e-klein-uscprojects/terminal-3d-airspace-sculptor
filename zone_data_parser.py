# ICAO Zone Parser | Module 009
# Parses JSON boundary data into usable 3D volume coordinates and control logic

import json

# --- Load ADIZ boundary data
with open('adiz_boundary_data.json', 'r') as file:
    adiz_data = json.load(file)

# --- Extract vertices and altitude info
zone_name = adiz_data["zone_name"]
floor_alt = adiz_data["altitude_floor"]
ceiling_alt = adiz_data["altitude_ceiling"]
priority = adiz_data["priority"]
vertices_2d = adiz_data["vertices"]

# --- Generate full 3D coordinates for airspace extrusion
airspace_volume = []
for pt in vertices_2d:
    base = [pt[0], pt[1], floor_alt]
    top = [pt[0], pt[1], ceiling_alt]
    airspace_volume.append((base, top))

# --- Display structured vertical zone
print(f"[{zone_name}] Altitude Band: {floor_alt}–{ceiling_alt} ft | Priority: {priority}")
for idx, pair in enumerate(airspace_volume):
    b, t = pair
    print(f"Edge {idx + 1}: Base=({b[0]}, {b[1]}, {b[2]}), Top=({t[0]}, {t[1]}, {t[2]})")
