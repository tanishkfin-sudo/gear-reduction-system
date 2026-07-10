```text
GEAR REDUCTION SYSTEM — VALIDATION RESULTS LOG
2:1 Spur Gear Reduction System

 
These logs record three runs of the script that test the gear design and illustrate
the design -> calculation -> problem -> revision -> verification cycle detailed in
the project README.

RUN 1: V1 Baseline

Inputs:
  Teeth (pinion / gear): 20 / 40
  Module: 2.5 mm
  Face width: 15 mm
  Input speed: 1000 RPM
  Input torque: 5.0 Nm
  Friction efficiency: 0.95

Results:
=== Gear Performance ===
Gear Ratio: 2.0 :1
Output Speed: 500.0 RPM
Output Torque: 9.5 Nm
=== Tooth Strength ===
Lewis Factor: 0.322
Tangential Force: 200.0 N
Bending Stress: 16.56 MPa
=== Safety Check ===
Allowable Stress: 140 MPa
Safety Factor: 8.45
PASS: Safety factor meets the requirement. (heavily over-engineered for this load)

Notes:
At a light load of 5.0 Nm, the initial design with a face width of 15mm is much stronger than needed.
The baseline serves to verify the calculator operates as intended before applying it to finding an actual weakness.


RUN 2: V1 Stress Test (problem found)

Inputs:
  Teeth (pinion / gear): 20 / 40
  Module: 2.5 mm
  Face width: 15 mm  <-- unchanged from V1
  Input speed: 1000 RPM
  Input torque: 40.0 Nm  <-- deliberately increased
  Friction efficiency: 0.95

Results:
=== Gear Performance ===
Gear Ratio: 2.0 :1
Output Speed: 500.0 RPM
Output Torque: 76.0 Nm
=== Tooth Strength ===
Lewis Factor: 0.322
Tangential Force: 1600.0 N
Bending Stress: 132.51 MPa
=== Safety Check ===
Allowable Stress: 140 MPa
Safety Factor: 1.06
FAIL: Safety factor is too low. (below the 1.5 minimum safety threshold)

Notes:
The input torque is intentionally increased to 40.0 Nm to represent a heavier load case. At this load level,
the original 15mm face width is unable to pass the 1.5 safety factor threshold.
This is the "problem found in v1" mentioned in the README.


RUN 3: V2 Fix (revised design, re-verified)

Inputs:
  Teeth (pinion / gear): 20 / 40
  Module: 2.5 mm
  Face width: 25 mm  <-- increased from 15mm to fix the failure
  Input speed: 1000 RPM
  Input torque: 40.0 Nm  <-- same stress-test load as Run 2
  Friction efficiency: 0.95

Results:
=== Gear Performance ===
Gear Ratio: 2.0 :1
Output Speed: 500.0 RPM
Output Torque: 76.0 Nm
=== Tooth Strength ===
Lewis Factor: 0.322
Tangential Force: 1600.0 N
Bending Stress: 79.5 MPa
=== Safety Check ===
Allowable Stress: 140 MPa
Safety Factor: 1.76
PASS: Safety factor meets the requirement. (design revised, verified safe)

Notes:
Face width was enlarged from 15mm to 25mm in Fusion 360 (v2 CAD file) in order to decrease tooth bending stress.
Using the new face width, while applying the same 40.0 Nm load in the calculator verifies that the safety factor now exceeds the 1.5 threshold.
The change in design was also verified in CAD by using the Interference Check in Fusion,
which indicated there was no collision in the v2 assembly.


SUMMARY

  Run 1 (V1, 5.0 Nm):    Safety Factor 8.45  -> PASS
  Run 2 (V1, 40.0 Nm):   Safety Factor 1.06  -> FAIL
  Run 3 (V2, 40.0 Nm):   Safety Factor 1.76  -> PASS

Assumed material: Mild steel (bending allowable ~140 MPa), commonly chosen as a cheap starting point material for a gear design.

```
