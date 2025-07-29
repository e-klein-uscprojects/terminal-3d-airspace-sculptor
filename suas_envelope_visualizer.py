# SUAS Envelope Visualizer | Module 012
# Builds 3D extrusion models for Special Use Airspace zones
# Source reference: HG 1.8, G-TUG Chapter 13

# --- Define base horizontal footprint
suas_boundary = [
    [0, 0],
    [0, 150],
    [150, 150],
    [150, 0]
]

# --- Define altitude layers with operational time ranges
altitude_layers = [
    {"min": 0, "max": 100, "time": "0600–1200Z"},
    {"min": 100, "max": 200, "time": "1200–1800Z"},
    {"min": 200, "max": 300, "time": "Permanently Active"}
]

# --- Generate stacked envelopes
print("[SUAS Zone Visualization]")
for idx, layer in enumerate(altitude_layers):
    print(f"  Layer {idx + 1}: {layer['min']}–{layer['max']} ft | Time: {layer['time']}")
    for pt in suas_boundary:
        base = [pt[0], pt[1], layer['min']]
        top = [pt[0], pt[1], layer['max']]
        print(f"    Base: {base} | Top: {top}")
