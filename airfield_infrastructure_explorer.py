# Airfield Infrastructure Explorer | Module 011
# Simulates runway ILS geometry, lighting systems, and NAVAID zone placements
# Source reference: HG 2.3.2.6, HG 1.6.10.1

# --- Define runway reference point
runway_start = [0, 0]
runway_end = [3000, 0]  # in meters

# --- ILS Zone Simulation
ils_zone = {
    "type": "LOC/DME",
    "start": runway_start,
    "end": [runway_end[0], runway_end[1] + 75],  # 75m lateral offset
    "glide_slope_angle": 3.0  # degrees
}

# --- Lighting System
lighting = {
    "system_type": "MALSF",
    "length": 450,  # meters
    "position": [runway_start[0] - 450, runway_start[1]]
}

# --- NAVAID Beacon
navaid = {
    "identifier": "I-XXX",
    "type": "VOR",
    "location": [runway_end[0] + 1000, runway_end[1] + 500]
}

# --- Output Simulation
print(f"[ILS Zone] Type: {ils_zone['type']}")
print(f"  Begin: {ils_zone['start']}")
print(f"  End:   {ils_zone['end']}")
print(f"  Glide Slope: {ils_zone['glide_slope_angle']}°")

print(f"\n[Lighting System] Type: {lighting['system_type']}")
print(f"  Length: {lighting['length']} m")
print(f"  Position: {lighting['position']}")

print(f"\n[NAVAID] Identifier: {navaid['identifier']} | Type: {navaid['type']}")
print(f"  Location: {navaid['location']}")
