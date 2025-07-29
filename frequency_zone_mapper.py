# Frequency Zone Mapper | Module 013
# Simulates air traffic control frequency volumes (VHF/UHF) in spatial form
# Source: HG 1.6, HG 1.6.8 — ATC zone logic with part-time and CPDLC tagging

# --- Define control zone data
atc_zones = [
    {
        "facility": "San Jose Tower",
        "freq": "120.9 MHz",
        "location": [1000, 2000],
        "radius": 800,     # meters
        "height": 2000,    # meters
        "type": "Full-time"
    },
    {
        "facility": "NorCal Approach",
        "freq": "133.0 MHz",
        "location": [3000, 4000],
        "radius": 1200,
        "height": 2500,
        "type": "Part-time"
    },
    {
        "facility": "CPDLC Node Alpha",
        "freq": "Datalink",
        "location": [5000, 6000],
        "radius": 500,
        "height": 3000,
        "type": "CPDLC"
    }
]

# --- Display structured frequency zones
print("[Frequency Volume Mapping]")
for zone in atc_zones:
    print(f"\nFacility: {zone['facility']} | Frequency: {zone['freq']}")
    print(f"  Location: {zone['location']}")
    print(f"  Radius: {zone['radius']} m | Height: {zone['height']} m")
    if zone['type'] == "Part-time":
        print("  ⚠️ Part-time frequency (active hours not guaranteed)")
    elif zone['type'] == "CPDLC":
        print("  🛰️ Digital CPDLC link volume")
    else:
        print("  ✅ Full-time VHF/UHF control zone")
