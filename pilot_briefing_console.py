# Pilot Briefing Console | Module 016
# Simulates formatted procedural annotations across terminal navigation structures
# Source: HG 2.3.2.1–HG 2.3.3 | Includes Trouble T, equipment flags, and altitude zoning

# --- Sample briefing data
briefing_data = [
    {"zone": "Final Approach", "altitude": "2600 ft", "notes": "RNAV required | Trouble T active"},
    {"zone": "Missed Approach Point", "altitude": "1700 ft", "notes": "Climb straight ahead to 3000 ft"},
    {"zone": "Holding Pattern Entry", "altitude": "4000 ft", "notes": "Left turns | Max speed 200 KIAS"},
    {"zone": "SUAS Boundary", "altitude": "3000 ft", "notes": "Restricted use | Active 0600–1200Z"}
]

# --- Render formatted console output
print("[Pilot Briefing Console]")
for entry in briefing_data:
    print(f"🔹 {entry['zone']}")
    print(f"   Altitude: {entry['altitude']}")
    print(f"   Notes: {entry['notes']}\n")
