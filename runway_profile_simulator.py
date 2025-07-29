# Runway Profile Simulator | Module 010
# Simulates runway elevation profile using TDZE, threshold, and LDA metrics
# Source Logic: HG 2.3.1.3 & HG 2.3.1.4

# --- Define runway parameters
runway_id = "RWY 09"
threshold_elevation = 327  # feet
tdze_elevation = 334        # feet
lda = 2500                  # meters
runway_length = 2600        # meters

# --- Compute profile slope
delta_elevation = tdze_elevation - threshold_elevation
slope_percent = (delta_elevation / lda) * 100

# --- Validate runway compliance
lda_flag = lda < runway_length
flag_msg = "⚠️ LDA shorter than runway length." if lda_flag else "✅ LDA within runway bounds."

# --- Display profile
print(f"[Runway Elevation Profile] {runway_id}")
print(f"  Threshold Elevation: {threshold_elevation} ft")
print(f"  TDZE Elevation:      {tdze_elevation} ft")
print(f"  Δ Elevation:         {delta_elevation} ft")
print(f"  LDA:                 {lda} m")
print(f"  Slope:               {slope_percent:.2f} %")
print(f"  {flag_msg}")
