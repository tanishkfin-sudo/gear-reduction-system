# gear_calc.py
# Final validated script for the 2:1 spur gear reduction system (v2 design)
# checks ratio, speed, torque, and bending stress on teeth

# inputs / constants
n_pinion = 20
n_gear = 40
mod = 2.5       # mm
rpm_in = 1000   # rpm
t_in = 40.0     # Nm
eff = 0.95      # friction loss
b = 25          # face width in mm

# quick ratio & output math
ratio = n_gear / n_pinion
rpm_out = rpm_in / ratio
t_out = t_in * ratio * eff

print("=== Gear Performance ===")
print("Gear Ratio:", round(ratio, 2), ":1")
print("Output Speed:", round(rpm_out, 2), "RPM")
print("Output Torque:", round(t_out, 2), "Nm")

# lewis factor lookup table (20 deg full depth)
# pinion has 20 teeth, so Y = 0.322
lewis_table = {12: 0.245, 15: 0.276, 20: 0.322, 24: 0.337, 30: 0.358, 40: 0.389, 60: 0.422, 75: 0.435}

# checking pinion because smaller gear is always the weaker one
Y = lewis_table[n_pinion]

# force math
d_pinion = mod * n_pinion       # pitch diameter (50mm)
r_pinion_m = (d_pinion / 2) / 1000  # convert radius mm to meters

f_tangent = t_in / r_pinion_m

# convert b and mod to meters for the stress calculation
b_m = b / 1000
mod_m = mod / 1000

# lewis equation
stress_pa = f_tangent / (b_m * mod_m * Y)
stress_mpa = stress_pa / 1e6  # Pa to MPa

print("=== Tooth Strength ===")
print("Lewis Factor:", Y)
print("Tangential Force:", round(f_tangent, 2), "N")
print("Bending Stress:", round(stress_mpa, 2), "MPa")

# safety margin verification
# using standard mild steel properties as a baseline
allowable_mpa = 140
sf = allowable_mpa / stress_mpa
min_sf = 1.5

print("\n=== Safety Check ===")
print("Allowable Stress:", allowable_mpa, "MPa")
print("Safety Factor:", round(sf, 2))

if sf >= min_sf:
    print("PASS: Safety factor meets the requirement.")
else:
    print("FAIL: Safety factor is too low.")
