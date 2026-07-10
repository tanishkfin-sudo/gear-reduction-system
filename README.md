# 2:1 Spur Gear Reduction System: Verification & Iterative Design
**Mechanical Engineering Application Portfolio Project**

## Project Overview
This work demonstrates the entire process of engineering design lifecycle of a 2:1 spur gear reduction system. The first design prototype (System V1) was created using Fusion 360, and then the stress analysis was done through a custom Python code of the Lewis Bending Stress Equation. After the structural risk of failure was found in the system under heavy loads, the next design (System V2) was created by optimizing the face width through parameterization.

---

## 1. Mechanical Design Specifications
The physical system relies on a perfectly matching center distance of $75.0 \text{ mm}$ with an integrated $0.1 \text{ mm}$ backlash setting to ensure friction reduction and smooth tooth engagement.

| Parameter | Input Pinion (Weaker Link) | Output Gear |
| :--- | :--- | :--- |
| **Number of Teeth ($N$)** | 20 | 40 |
| **Module ($m$)** | $2.5 \text{ mm}$ | $2.5 \text{ mm}$ |
| **Pitch Diameter ($d$)** | $50.0 \text{ mm}$ | $100.0 \text{ mm}$ |
| **Pressure Angle** | $20^\circ$ | $20^\circ$ |
| **Material Base** | ASTM A36 Mild Steel | ASTM A36 Mild Steel |

---

## 2. Validation Testing & Simulation Summary
The system's structural integrity was evaluated across three distinct operational test cases using our custom `gear_calc.py` validation script.

| Test Phase | Config Version | Input Torque | Face Width | Safety Factor | Status / Engineering Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Run 1: Baseline** | System V1 | $5.0 \text{ Nm}$ | $15.0 \text{ mm}$ | **8.45** | **PASS** (Heavily over-engineered for light duty) |
| **Run 2: Stress Test** | System V1 | $40.0 \text{ Nm}$ | $15.0 \text{ mm}$ | **1.06** | **CRITICAL FAIL** (Drops below $1.5$ minimum threshold) |
| **Run 3: Optimization** | System V2 | $40.0 \text{ Nm}$ | $25.0 \text{ mm}$ | **1.76** | **PASS** (Geometry revised and verified structurally safe) |

---

## 3. Script Simulation Execution Logs (`results_log.txt`)
The following comprehensive execution records capture the unedited input arrays, intermediate tangential forces, and ultimate mechanical safety factor calculations:

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
