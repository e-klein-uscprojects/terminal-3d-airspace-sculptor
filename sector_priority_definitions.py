# Sector Priority Definitions | Module 006
# ICAO-based airspace categorization with altitude envelope logic
# Referenced Spec: HG 1.7, TEM 13APR2023 — Controlled zone type stratification

# --- Airspace zone definitions
zones = [
    {"name": "ADIZ", "min_alt": 0, "max_alt": 100, "priority": 1},
    {"name": "International Boundary", "min_alt": 100, "max_alt": 200, "priority": 2},
    {"name": "SUAS", "min_alt": 200, "max_alt": 300, "priority": 3}
]

# --- Apply priority rule (higher priority = lower number)
def get_zone_by_altitude(altitude):
    for zone in sorted(zones, key=lambda z: z["priority"]):
        if zone["min_alt"] <= altitude < zone["max_alt"]:
            return zone["name"]
    return "Undefined"

# --- Example altitude logic test
test_alts = [50, 150, 250, 350]
for alt in test_alts:
    zone_type = get_zone_by_altitude(alt)
    print(f"Altitude {alt} ft belongs to: {zone_type}")
