# 2:1 Spur Gear Reduction System: Verification & Iterative Design


## Project Overview
In order to link CAD modeling with mechanical analysis, I designed a 2:1 spur gear reduction system with Fusion 360. In order to confirm that the structure is safe enough, I created a Python script based on Lewis Bending Stress Equation for validation of my ASTM A36 mild steel design. Although it passed easily at 5.0 Nm, at 40.0 Nm the stress safety factor was found too low with only 1.06 compared to the 140 MPa material limitation. Being aware of the structural risk, I iterated my design through engineering feedback loop by parameterizing and raising the face width from 15mm to 25mm. By executing my Python script again, I confirmed that my new version of System (V2) met the design parameters safely with the safety factor of 1.76.

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
```
## 4. Photos, Videos & CAD Files

### First Gear Design (V1)
This was our starting design. It had a narrower gear width (15mm) and couldn't handle the heavy 40 Nm load, dropping down to a dangerous 1.06 safety factor.

* **Isometric View of the Gears:**
![V1 Assembly Isometric](render_1_isometric.png)

* **Top Down View of the Assembly:**
![V1 Assembly Top Down](render_1_topdown_assembly.png)

* **Close-up on the Gear Teeth:**
![Pitch Engagement Close Up](render_2_teeth_closeup.png)

---

### Spinning Gear Tests (Videos)
These clips show how the gears spin together inside Fusion 360. Turning the small gear twice turns the big gear exactly once.

* [Click here to see the gears spin automatically](gear_rotation_v1_2.mp4)
* [Click here to see the gears turned by hand](gear_rotation_v1_1.mp4)

---

### Fixed Gear Design (V2)
To stop the gears from breaking under the heavy load, we widened the teeth to 25mm. This fixed the problem and brought the safety factor up to a safe 1.76.

* **New Heavy Duty Design:**
![V2 Heavy Duty Configuration](render_2_isometric.png)

* **Baseplate Hole Locations:**
![V2 Baseplate Mounting Clearances](render_3_baseplate_holes.png)

---

## 5. Original CAD File Downloads
If anyone wants to download your actual 3D models to open them up on their computer, they can use these shortcuts:

* [Download First Design - V1 (.f3z file)](Gear_Reduction_System_V1.f3z)
* [Download Fixed Design - V2 (.f3z file)](Gear_Reduction_System_V2.f3z)
