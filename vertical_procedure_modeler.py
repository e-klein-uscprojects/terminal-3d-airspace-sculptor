# Vertical Procedure Tree Modeler | Module 014
# Builds CAT I/II/III tiered approach ladders with glide slope logic and obstacle margins
# Source references: HG 1.5.1, HG 2.2.1, ICAO procedure plates

# --- Define approach fix
approach_fix = [0, 0, 300]  # meters altitude

# --- Define CAT profiles
categories = [
    {"cat": "CAT I", "glide_slope": 3.0, "minima": 60},
    {"cat": "CAT II", "glide_slope": 2.8, "minima": 45},
    {"cat": "CAT III", "glide_slope": 2.5, "minima": 30}
]

# --- Generate descent paths
print("[Vertical Procedure Tree]")
for cat in categories:
    path = []
    altitude = approach_fix[2]
    x = 0
    print(f"\n{cat['cat']} → Glide Slope: {cat['glide_slope']}° | Minima: {cat['minima']} ft")
    while altitude > cat["minima"]:
        x += 100
        altitude -= 100 * np.tan(np.radians(cat["glide_slope"]))
        path.append((x, 0, round(altitude, 2)))
    for idx, point in enumerate(path):
        print(f"  Step {idx + 1}: X:{point[0]} Y:{point[1]} Altitude:{point[2]} ft")
