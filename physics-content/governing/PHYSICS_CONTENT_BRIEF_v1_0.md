# GCSE Physics — Content Brief
## Edexcel IGCSE Physics (4PH1) · Higher Tier
### Version 1.0 · February 2026

**Purpose:** This document defines the 22 coverage contracts that govern Physics scenario authoring. Each contract specifies exactly what a scenario must contain — required subtopics, interaction types, AO spread, mark targets, and misconceptions. It also contains the master misconceptions list (per TAG1–TAG2 in the authoring rules).

**Governing documents:**
- `SCIENCE_CONTENT_AUTHORING_RULES_v1_2.md` — quality rules, marking conventions, tag taxonomy
- `UNIFIED_SCENARIO_SCHEMA_v1_3.md` — JSON schema
- `Physics_Curriculum_v1_0.docx` — curriculum source of truth

**Build order (by exam weight):**
1. Sprint 3a: Group 1 · Forces & Motion (T1–T5) — 5 scenarios
2. Sprint 3b: Group 2 · Electricity & Magnetism (T6–T10) — 5 scenarios
3. Sprint 3c: Group 3 · Waves & Light (T11–T14) — 4 scenarios
4. Sprint 3d: Groups 4+5 · Energy + Radioactivity & Space (T15–T22) — 8 scenarios
5. Sprint 3e: QA (structural + academic)

**Gold examples:** phy_01, phy_02, phy_06, phy_13, phy_19

**Target totals:** 22 scenarios, ~110 questions, ~210 marks.

**Target AO distribution (subject-level):** AO1: ~30%, AO2: ~40%, AO3: ~30%. Per CS2/academic QA: no individual AO category may exceed 40% of total marks at subject level. No AO category may exceed 45% at group level unless pedagogically justified with a written note.

---

## Master Misconceptions List

Per TAG1–TAG2, all misconception tags used in Physics scenarios must be selected from this list. New tags require formal addition here before use in any scenario file.

Each entry includes the tag and a one-line description of the real student error it represents.

### Forces & Motion

| Tag | Student Error |
|-----|---------------|
| `assumes-heavier-falls-faster` | Thinks heavier objects always fall faster, ignoring air resistance / vacuum conditions |
| `thinks-motion-requires-force` | Believes a moving object needs a continuous force to keep moving (contradicts Newton's 1st law) |
| `thinks-action-reaction-same-object` | Places Newton's 3rd law action-reaction pair on the same object instead of two interacting objects |
| `confuses-mass-weight` | Uses mass (kg) and weight (N) interchangeably or applies wrong units |
| `confuses-speed-velocity` | Doesn't distinguish speed (scalar, magnitude only) from velocity (vector, magnitude + direction) |
| `confuses-distance-displacement` | Treats distance (scalar, total path) and displacement (vector, straight-line) as identical |
| `confuses-d-t-gradient-with-acceleration` | Reads the gradient of a distance-time graph as acceleration instead of speed |
| `confuses-v-t-gradient-and-area` | Swaps gradient (= acceleration) and area under curve (= distance) on velocity-time graphs |
| `thinks-acceleration-means-speeding-up` | Doesn't recognise deceleration (negative acceleration) or change in direction as acceleration |
| `forgets-v-t-area-is-distance` | Doesn't know the area under a velocity-time graph gives distance/displacement |
| `confuses-resultant-force-direction` | Cannot determine the resultant of two or more forces acting on a body |
| `thinks-terminal-velocity-means-stopping` | Thinks terminal velocity means the object eventually stops rather than reaching constant speed |
| `confuses-elastic-plastic-deformation` | Swaps elastic deformation (returns to original shape) and plastic deformation (permanently deformed) |
| `thinks-momentum-is-velocity` | Confuses momentum (mass × velocity) with velocity alone, ignoring mass |
| `confuses-impulse-momentum` | Doesn't understand impulse (Ft) equals change in momentum (Δp) |
| `thinks-momentum-not-conserved` | Believes total momentum changes in a collision or explosion |
| `confuses-kinetic-potential-energy` | Swaps kinetic energy (motion) and gravitational potential energy (height) in energy transfers |
| `thinks-efficiency-exceeds-100` | Believes useful energy output can exceed total energy input |
| `confuses-work-force` | Thinks work done equals force alone, forgetting to multiply by distance |
| `confuses-power-energy` | Uses power (rate of energy transfer, W) and energy (J) interchangeably |

### Electricity & Magnetism

| Tag | Student Error |
|-----|---------------|
| `thinks-current-used-up` | Believes current is "used up" as it flows through components in a circuit |
| `confuses-series-parallel-current` | Doesn't know current is the same in series but splits in parallel |
| `confuses-voltage-current` | Uses voltage and current interchangeably or doesn't understand their distinct roles |
| `confuses-power-energy-electricity` | Doesn't distinguish electrical power (P = IV, watts) from energy (E = Pt, joules) |
| `confuses-ammeter-voltmeter-placement` | Places ammeter in parallel or voltmeter in series instead of vice versa |
| `thinks-resistance-proportional-to-voltage` | Misinterprets Ohm's law — thinks resistance increases when voltage increases |
| `confuses-iv-graph-gradient` | Misreads or misinterprets the gradient of I-V characteristic graphs |
| `confuses-thermistor-ldr-response` | Swaps thermistor response (resistance decreases with temperature) and LDR response (resistance decreases with light) |
| `confuses-ac-dc` | Doesn't understand AC (alternating direction) vs DC (constant direction) |
| `thinks-transformers-create-energy` | Believes step-up transformers increase the total power, violating energy conservation |
| `confuses-step-up-step-down` | Swaps step-up (more turns on secondary, increases voltage) and step-down (fewer turns, decreases voltage) |
| `confuses-magnetic-electric-fields` | Mixes up magnetic field patterns with electric field patterns |
| `confuses-motor-effect-direction` | Gets Fleming's left-hand rule wrong — swaps force, field, or current fingers |
| `thinks-electromagnets-are-permanent` | Doesn't understand electromagnets can be switched on and off by controlling current |
| `confuses-induction-direction` | Gets the direction of induced current/EMF wrong in electromagnetic induction |

### Waves & Light

| Tag | Student Error |
|-----|---------------|
| `thinks-em-waves-need-medium` | Believes electromagnetic waves need a material medium to travel through |
| `confuses-transverse-longitudinal` | Swaps descriptions of transverse (perpendicular oscillation) and longitudinal (parallel oscillation) waves |
| `confuses-frequency-speed` | Thinks increasing frequency increases wave speed in a given medium |
| `confuses-amplitude-wavelength` | Swaps amplitude (maximum displacement from rest) and wavelength (distance between successive peaks) |
| `confuses-period-frequency` | Doesn't know period = 1/frequency, or confuses which is measured in Hz vs seconds |
| `confuses-em-spectrum-order` | Gets the order of the electromagnetic spectrum wrong (e.g. places microwaves after visible light) |
| `confuses-reflection-refraction` | Mixes up reflection (wave bouncing back) and refraction (wave changing direction when entering a new medium) |
| `thinks-light-bends-away-from-normal` | Gets refraction direction wrong — light bends towards normal when entering a denser medium, not away |
| `confuses-real-virtual-images` | Swaps properties of real images (formed by converging rays) and virtual images (formed by diverging rays) |
| `confuses-convex-concave-lenses` | Swaps converging (convex) and diverging (concave) lens behaviour |
| `confuses-critical-angle-TIR` | Doesn't understand total internal reflection only occurs above the critical angle |
| `confuses-pitch-loudness` | Swaps pitch (determined by frequency) and loudness (determined by amplitude) |
| `thinks-sound-travels-in-vacuum` | Believes sound waves can travel through a vacuum |
| `confuses-ultrasound-applications` | Mixes up medical imaging and industrial flaw-detection uses of ultrasound |

### Energy

| Tag | Student Error |
|-----|---------------|
| `confuses-heat-temperature` | Uses heat (energy transferred, J) and temperature (degree of hotness, °C) interchangeably |
| `thinks-cold-transfers-to-hot` | Believes "coldness" is transferred rather than heat flowing from hot to cold |
| `confuses-energy-force` | Uses energy and force interchangeably (e.g. "the force of the fuel") |
| `confuses-conduction-convection-radiation` | Cannot distinguish the three methods of thermal energy transfer |
| `forgets-shc-units` | Uses wrong units for specific heat capacity (should be J/kg°C or J/kg·K) |
| `confuses-shc-latent-heat` | Doesn't distinguish specific heat capacity (temperature change) from latent heat (state change at constant temperature) |
| `confuses-latent-heat-types` | Swaps specific latent heat of fusion (solid↔liquid) and vaporisation (liquid↔gas) |
| `thinks-renewable-means-unlimited` | Believes renewable energy sources have no environmental impact or limitations |
| `confuses-sankey-arrow-widths` | Cannot interpret Sankey diagram arrow widths as proportional to energy transferred |
| `confuses-pressure-force` | Doesn't understand P = F/A — thinks pressure and force are the same quantity |
| `forgets-depth-pressure-relationship` | Doesn't know pressure in a fluid increases with depth (P = hρg) |
| `confuses-boyles-law-direction` | Gets the inverse relationship between pressure and volume wrong |

### Radioactivity & Space

| Tag | Student Error |
|-----|---------------|
| `thinks-radiation-makes-radioactive` | Believes irradiation (exposure to radiation) always makes the object radioactive (contamination) |
| `thinks-half-life-means-half-gone` | Misunderstands half-life — thinks the substance disappears or becomes completely inactive after one half-life |
| `confuses-fission-fusion` | Swaps nuclear fission (large nucleus splits) and nuclear fusion (small nuclei join) |
| `confuses-alpha-beta-gamma-properties` | Mixes up penetrating power, ionising ability, and charge of alpha, beta, and gamma radiation |
| `confuses-proton-nucleon-number` | Swaps proton number (Z, number of protons) and nucleon number (A, protons + neutrons) |
| `confuses-isotopes-elements` | Thinks isotopes (same element, different neutrons) are different elements |
| `thinks-background-radiation-harmful` | Assumes all background radiation is dangerous rather than understanding it is low-level and natural |
| `confuses-decay-equation-balancing` | Cannot balance nucleon numbers and proton numbers in nuclear decay equations |
| `confuses-star-lifecycle-stages` | Gets the order of stellar evolution wrong (e.g. skips red giant phase or confuses end states) |
| `thinks-big-bang-was-explosion` | Believes the Big Bang was a literal explosion in pre-existing space rather than an expansion of space itself |
| `confuses-redshift-blueshift` | Swaps redshift (galaxy moving away, wavelength increases) and blueshift (galaxy moving closer) |
| `thinks-heavier-objects-orbit-faster` | Doesn't understand that orbital speed depends on orbital radius, not object mass |
| `confuses-weight-mass-space` | Thinks mass changes in different gravitational fields (only weight changes) |

### Cross-Topic — Investigation & Data Handling

| Tag | Student Error |
|-----|---------------|
| `includes-anomalies-in-mean` | Includes obvious outliers when calculating a mean instead of identifying and excluding them |
| `forgets-to-convert-units` | Fails to convert units before performing calculations (e.g. g to kg, cm to m, mA to A) |

**Total misconception tags: 76**

---

## Coverage Contracts

### Group 1 · Forces & Motion

---

#### Topic 1: Motion & Speed

```
Scenario ID: phy_01
Mark target: 10
Parts: 5
Icon: 🏃

Required subtopics:
- Distance-time graphs — must appear
- Speed calculations — must appear
- Scalar vs vector (speed/velocity) — must appear

Interaction types:
- Part (a): mcq — AO1 — 1 mark (recall: what the gradient of a d-t graph represents)
- Part (b): graph_reading — AO2 — 3 marks (read distance and time values from d-t graph; determine speed from gradient)
- Part (c): numeric_with_unit — AO2 — 2 marks (calculate average speed for a multi-stage journey)
- Part (d): mcq — AO1 — 1 mark (identify which quantity is a vector: speed, distance, velocity, or time)
- Part (e): self_assessed — AO3 — 3 marks (describe and explain the motion shown in each section of the d-t graph)

Required misconceptions:
- confuses-d-t-gradient-with-acceleration
- confuses-speed-velocity
- confuses-distance-displacement

Graph/Diagram/Data table requirements:
- Distance-time graph with 3–4 distinct sections (constant speed, stationary, different constant speed, return journey). Graph type: d-t.

AO spread: AO1: 2, AO2: 5, AO3: 3
Notes: GOLD EXAMPLE. PHY1 compliance: graph type is d-t. Graph reading tolerance ±2% per MC1.
```

---

#### Topic 2: Acceleration & Velocity

```
Scenario ID: phy_02
Mark target: 10
Parts: 5
Icon: 🚀

Required subtopics:
- Velocity-time graphs — must appear
- Acceleration calculations — must appear
- Area under v-t graph = distance — must appear

Interaction types:
- Part (a): mcq — AO1 — 1 mark (recall: what the gradient of a v-t graph represents)
- Part (b): graph_reading — AO2 — 3 marks (read velocity at given times; calculate acceleration from gradient of v-t graph)
- Part (c): calculation — AO2 — 2 marks (calculate distance from area under v-t graph — triangle + rectangle)
- Part (d): mcq — AO1 — 1 mark (identify deceleration from a v-t graph description)
- Part (e): self_assessed — AO3 — 3 marks (compare two journeys shown on the same v-t graph — which covers more distance and why)

Required misconceptions:
- confuses-v-t-gradient-and-area
- thinks-acceleration-means-speeding-up
- forgets-v-t-area-is-distance

Graph/Diagram/Data table requirements:
- Velocity-time graph with acceleration, constant velocity, and deceleration sections. Two lines for the comparison in part (e). Graph type: v-t.

AO spread: AO1: 2, AO2: 5, AO3: 3
Notes: GOLD EXAMPLE. PHY1 compliance: graph type is v-t. PHY2 compliance: formula sheet provided (v = u + at, s = ½(u+v)t). Graph reading tolerance ±2%.
```

---

#### Topic 3: Forces

```
Scenario ID: phy_03
Mark target: 10
Parts: 5
Icon: ⚖️

Required subtopics:
- Newton's laws of motion — must appear
- Free body diagrams — must appear
- Weight, mass, and gravitational field strength — must appear
- Hooke's Law / force-extension — preferred

Interaction types:
- Part (a): diagram_label — AO1 — 3 marks (label forces on a free body diagram: weight, normal contact, friction)
- Part (b): mcq — AO1 — 1 mark (recall Newton's 1st law — what happens when resultant force is zero)
- Part (c): numeric_with_unit — AO2 — 2 marks (calculate weight from mass using W = mg)
- Part (d): mcq — AO1 — 1 mark (identify correct unit for weight)
- Part (e): self_assessed — AO3 — 3 marks (explain why a skydiver reaches terminal velocity — link to balanced forces)

Required misconceptions:
- thinks-motion-requires-force
- confuses-mass-weight
- thinks-terminal-velocity-means-stopping
- confuses-resultant-force-direction

Graph/Diagram/Data table requirements:
- Free body diagram of an object (e.g. skydiver or box on slope) with 3 labelled force arrows. Label bank with distractors.

AO spread: AO1: 5, AO2: 2, AO3: 3
Notes: PHY2 compliance: formula sheet provided (W = mg). Diagram spec must pass DIA5 reproducibility test.
```

---

#### Topic 4: Momentum & Impulse

```
Scenario ID: phy_04
Mark target: 9
Parts: 5
Icon: 💥

Required subtopics:
- Momentum = mass × velocity — must appear
- Conservation of momentum — must appear
- Impulse = force × time = change in momentum — must appear

Interaction types:
- Part (a): mcq — AO1 — 1 mark (recall: definition of momentum, select correct equation)
- Part (b): numeric_with_unit — AO2 — 2 marks (calculate momentum of a moving object)
- Part (c): calculation — AO2 — 2 marks (use conservation of momentum to find velocity after collision)
- Part (d): mcq — AO1 — 1 mark (identify which collision is elastic vs inelastic)
- Part (e): self_assessed — AO3 — 3 marks (explain why crumple zones in cars reduce injury — link to impulse, force, and time)

Required misconceptions:
- thinks-momentum-is-velocity
- thinks-momentum-not-conserved
- confuses-impulse-momentum

Graph/Diagram/Data table requirements:
- None

AO spread: AO1: 2, AO2: 4, AO3: 3
Notes: PHY2 compliance: formula sheet provided (p = mv, F = Δp/Δt). Numbers chosen to produce clean integer answers per DIF3.
```

---

#### Topic 5: Work, Energy & Power

```
Scenario ID: phy_05
Mark target: 9
Parts: 5
Icon: ⚡

Required subtopics:
- Work done = force × distance — must appear
- Kinetic and gravitational potential energy — must appear
- Conservation of energy — must appear
- Power and efficiency — must appear

Interaction types:
- Part (a): mcq — AO1 — 1 mark (recall: identify the correct equation for kinetic energy)
- Part (b): calculation — AO2 — 2 marks (calculate GPE gained: Ep = mgh)
- Part (c): numeric_with_unit — AO2 — 2 marks (calculate KE at the bottom of a slope using energy conservation)
- Part (d): mcq — AO1 — 1 mark (identify what happens to "lost" energy in a transfer — it becomes thermal)
- Part (e): self_assessed — AO3 — 3 marks (evaluate the efficiency of an energy transfer, explain why efficiency < 100%)

Required misconceptions:
- confuses-kinetic-potential-energy
- thinks-efficiency-exceeds-100
- confuses-work-force
- confuses-power-energy

Graph/Diagram/Data table requirements:
- None (energy bar chart or transfer diagram may be included as visual support but is not assessed)

AO spread: AO1: 2, AO2: 4, AO3: 3
Notes: PHY2 compliance: formula sheet provided (Ek = ½mv², Ep = mgh, W = Fd, P = W/t). Clean integers per DIF3.
```

---

### Group 2 · Electricity & Magnetism

---

#### Topic 6: Circuit Fundamentals

```
Scenario ID: phy_06
Mark target: 10
Parts: 5
Icon: 🔋

Required subtopics:
- Current, voltage, resistance — must appear
- Ohm's law (V = IR) — must appear
- Series and parallel circuits — must appear
- Ammeter and voltmeter placement — must appear

Interaction types:
- Part (a): diagram_label — AO1 — 3 marks (label components on a circuit diagram: ammeter, voltmeter, resistor)
- Part (b): mcq — AO1 — 1 mark (recall: ammeter placement — series or parallel?)
- Part (c): numeric_with_unit — AO2 — 2 marks (calculate resistance using V = IR from circuit values)
- Part (d): mcq — AO2 — 1 mark (predict what happens to total resistance when a resistor is added in parallel)
- Part (e): self_assessed — AO3 — 3 marks (explain why current is the same at all points in a series circuit but voltage is shared)

Required misconceptions:
- thinks-current-used-up
- confuses-series-parallel-current
- confuses-ammeter-voltmeter-placement
- confuses-voltage-current

Graph/Diagram/Data table requirements:
- Circuit diagram with series and parallel sections, ammeter and voltmeter positions, standard IEC symbols. Label bank with distractors (e.g. thermistor, LDR, diode).

AO spread: AO1: 4, AO2: 3, AO3: 3
Notes: GOLD EXAMPLE. PHY2 compliance: formula sheet provided (V = IR). Circuit diagram label uses standard IEC symbols per curriculum doc.
```

---

#### Topic 7: Electrical Components

```
Scenario ID: phy_07
Mark target: 10
Parts: 5
Icon: 💡

Required subtopics:
- I-V characteristics (resistor, filament lamp, diode) — must appear
- Resistance calculations — must appear
- Thermistor and LDR — must appear

Interaction types:
- Part (a): graph_reading — AO2 — 2 marks (read current and voltage values from an I-V characteristic graph)
- Part (b): mcq — AO1 — 1 mark (identify which I-V graph belongs to an ohmic resistor)
- Part (c): diagram_label — AO1 — 2 marks (label circuit symbols: thermistor, LDR)
- Part (d): numeric_with_unit — AO2 — 2 marks (calculate resistance at a specific point on the I-V graph)
- Part (e): self_assessed — AO3 — 3 marks (explain why the filament lamp I-V curve is non-linear — link to temperature and resistance)

Required misconceptions:
- confuses-iv-graph-gradient
- confuses-thermistor-ldr-response
- thinks-resistance-proportional-to-voltage

Graph/Diagram/Data table requirements:
- I-V characteristic graph showing at least two components (ohmic resistor as straight line, filament lamp as curve). Graph type: I-V.

AO spread: AO1: 3, AO2: 4, AO3: 3
Notes: PHY1 compliance: graph type is I-V. Graph reading tolerance ±2%.
```

---

#### Topic 8: Electrical Power & Energy

```
Scenario ID: phy_08
Mark target: 9
Parts: 5
Icon: 🔌

Required subtopics:
- P = IV, P = I²R, P = V²/R — must appear
- Energy = power × time — must appear
- Cost of electricity — must appear
- AC vs DC — preferred

Interaction types:
- Part (a): mcq — AO1 — 1 mark (recall: which equation links power, current, and voltage)
- Part (b): calculation — AO2 — 2 marks (calculate power dissipated by a component using P = I²R)
- Part (c): numeric_with_unit — AO2 — 2 marks (calculate cost of running an appliance: E = Pt, cost = kWh × price)
- Part (d): mcq — AO1 — 1 mark (identify the difference between AC and DC)
- Part (e): self_assessed — AO3 — 3 marks (explain why high-power appliances use thicker cables — link to I²R heating)

Required misconceptions:
- confuses-power-energy-electricity
- confuses-ac-dc
- forgets-to-convert-units

Graph/Diagram/Data table requirements:
- None

AO spread: AO1: 2, AO2: 4, AO3: 3
Notes: PHY2 compliance: formula sheet provided (P = IV, P = I²R, E = Pt). Ensure kWh conversion produces clean numbers per DIF3.
```

---

#### Topic 9: Magnetism & Electromagnetism

```
Scenario ID: phy_09
Mark target: 10
Parts: 5
Icon: 🧲

Required subtopics:
- Magnetic field patterns — must appear
- Electromagnets — must appear
- Motor effect and Fleming's left-hand rule — must appear
- Electromagnetic induction — preferred

Interaction types:
- Part (a): diagram_label — AO1 — 3 marks (label magnetic field lines around a bar magnet: N pole, S pole, field direction arrows)
- Part (b): mcq — AO1 — 1 mark (recall: how to increase the strength of an electromagnet)
- Part (c): numeric_with_unit — AO2 — 2 marks (calculate force on a current-carrying wire: F = BIL)
- Part (d): mcq — AO2 — 1 mark (apply Fleming's left-hand rule to determine force direction)
- Part (e): self_assessed — AO3 — 3 marks (explain how a simple DC motor works — link to motor effect, commutator, and rotation)

Required misconceptions:
- confuses-magnetic-electric-fields
- confuses-motor-effect-direction
- thinks-electromagnets-are-permanent
- confuses-induction-direction

Graph/Diagram/Data table requirements:
- Bar magnet field line diagram with hotspots at N pole, S pole, and field line direction. Label bank with distractors.

AO spread: AO1: 4, AO2: 3, AO3: 3
Notes: PHY2 compliance: formula sheet provided (F = BIL). Diagram spec must pass DIA5.
```

---

#### Topic 10: Transformers & the Grid

```
Scenario ID: phy_10
Mark target: 9
Parts: 5
Icon: 🏗️

Required subtopics:
- Transformer equation (Vp/Vs = Np/Ns) — must appear
- Step-up and step-down transformers — must appear
- Power transmission and the National Grid — must appear

Interaction types:
- Part (a): mcq — AO1 — 1 mark (recall: identify a step-up transformer from a description)
- Part (b): calculation — AO2 — 2 marks (calculate secondary voltage using Vp/Vs = Np/Ns)
- Part (c): numeric_with_unit — AO2 — 2 marks (calculate current in secondary coil assuming 100% efficiency: VpIp = VsIs)
- Part (d): mcq — AO1 — 1 mark (identify why the National Grid uses high voltage for transmission)
- Part (e): self_assessed — AO3 — 3 marks (explain why transmitting at high voltage reduces energy losses — link to P = I²R)

Required misconceptions:
- confuses-step-up-step-down
- thinks-transformers-create-energy
- confuses-power-energy-electricity

Graph/Diagram/Data table requirements:
- None (a schematic transformer diagram may be included as visual context but is not assessed)

AO spread: AO1: 2, AO2: 4, AO3: 3
Notes: PHY2 compliance: formula sheet provided (Vp/Vs = Np/Ns, P = IV). Clean integers per DIF3.
```

---

### Group 3 · Waves & Light

---

#### Topic 11: Wave Properties

```
Scenario ID: phy_11
Mark target: 10
Parts: 5
Icon: 🌊

Required subtopics:
- Transverse vs longitudinal waves — must appear
- Amplitude, frequency, wavelength, period — must appear
- Wave speed equation (v = fλ) — must appear

Interaction types:
- Part (a): diagram_label — AO1 — 2 marks (label amplitude and wavelength on a transverse wave diagram)
- Part (b): mcq — AO1 — 1 mark (identify which wave type is longitudinal: sound, light, water, or radio)
- Part (c): graph_reading — AO2 — 2 marks (read amplitude and period from a displacement-time wave graph)
- Part (d): numeric_with_unit — AO2 — 2 marks (calculate wave speed using v = fλ)
- Part (e): self_assessed — AO3 — 3 marks (compare and contrast transverse and longitudinal waves with examples)

Required misconceptions:
- confuses-transverse-longitudinal
- confuses-amplitude-wavelength
- confuses-frequency-speed
- confuses-period-frequency

Graph/Diagram/Data table requirements:
- Transverse wave diagram with labelled features (for part a). Displacement-time graph of a wave (for part c). Graph type: wave displacement-time.

AO spread: AO1: 3, AO2: 4, AO3: 3
Notes: PHY1 compliance: graph type is wave displacement-time. PHY2 compliance: formula sheet provided (v = fλ). Graph reading tolerance ±2%.
```

---

#### Topic 12: The Electromagnetic Spectrum

```
Scenario ID: phy_12
Mark target: 9
Parts: 4
Icon: 📡

Required subtopics:
- EM spectrum order — must appear
- Properties, uses, and hazards of each region — must appear
- Speed of light — preferred

Interaction types:
- Part (a): process_sequence — AO2 — 3 marks (order EM spectrum regions from lowest to highest frequency)
- Part (b): mcq — AO1 — 1 mark (recall: which EM wave is used for mobile phone communication)
- Part (c): keyword_match — AO1 — 2 marks (match EM regions to their uses/hazards from a word bank)
- Part (d): self_assessed — AO3 — 3 marks (explain why UV radiation is more dangerous than radio waves — link to frequency, energy, and ionisation)

Required misconceptions:
- thinks-em-waves-need-medium
- confuses-em-spectrum-order
- confuses-frequency-speed

Graph/Diagram/Data table requirements:
- None

AO spread: AO1: 3, AO2: 3, AO3: 3
```

---

#### Topic 13: Light & Optics

```
Scenario ID: phy_13
Mark target: 10
Parts: 5
Icon: 🔦

Required subtopics:
- Reflection and refraction — must appear
- Snell's law / refractive index — must appear
- Total internal reflection and critical angle — must appear
- Lenses (convex/concave) — preferred

Interaction types:
- Part (a): mcq — AO1 — 1 mark (recall: state the law of reflection)
- Part (b): diagram_label — AO1 — 2 marks (label incident ray, refracted ray, and normal on a ray diagram)
- Part (c): numeric_with_unit — AO2 — 2 marks (calculate refractive index using Snell's law: n = sin i / sin r)
- Part (d): mcq — AO2 — 1 mark (identify which situation produces total internal reflection — angle must exceed critical angle)
- Part (e): self_assessed — AO3 — 4 marks (explain how optical fibres use total internal reflection for data transmission, and why the critical angle matters)

Required misconceptions:
- confuses-reflection-refraction
- thinks-light-bends-away-from-normal
- confuses-critical-angle-TIR
- confuses-real-virtual-images

Graph/Diagram/Data table requirements:
- Interactive ray diagram (SVG) showing refraction at a glass-air boundary with labelled incident ray, normal, refracted ray. Hotspots for labels.

AO spread: AO1: 3, AO2: 3, AO3: 4
Notes: GOLD EXAMPLE. Ray diagram SVG per curriculum doc. PHY2 compliance: formula sheet provided (n = sin i / sin r). Diagram spec must pass DIA5.
```

---

#### Topic 14: Sound

```
Scenario ID: phy_14
Mark target: 9
Parts: 5
Icon: 🔊

Required subtopics:
- Sound as longitudinal wave — must appear
- Speed of sound in different media — must appear
- Pitch and loudness — must appear
- Echo calculations / ultrasound — must appear

Interaction types:
- Part (a): mcq — AO1 — 1 mark (recall: sound is a longitudinal wave — identify correct description)
- Part (b): numeric_with_unit — AO2 — 2 marks (calculate distance to a reflecting surface from echo time: d = vt/2)
- Part (c): graph_reading — AO2 — 2 marks (read amplitude and frequency from an oscilloscope trace)
- Part (d): mcq — AO1 — 1 mark (identify which change increases pitch: amplitude, frequency, wavelength, or speed)
- Part (e): self_assessed — AO3 — 3 marks (explain why sound travels faster in solids than in gases — link to particle arrangement and spacing)

Required misconceptions:
- confuses-pitch-loudness
- thinks-sound-travels-in-vacuum
- confuses-transverse-longitudinal
- confuses-ultrasound-applications

Graph/Diagram/Data table requirements:
- Oscilloscope trace showing two sound waves with different frequencies and amplitudes. Graph type: wave displacement-time.

AO spread: AO1: 2, AO2: 4, AO3: 3
Notes: PHY1 compliance: graph type is wave displacement-time (oscilloscope trace). Graph reading tolerance ±2%.
```

---

### Group 4 · Energy

---

#### Topic 15: Thermal Energy

```
Scenario ID: phy_15
Mark target: 10
Parts: 5
Icon: 🌡️

Required subtopics:
- Conduction, convection, radiation — must appear
- Specific heat capacity (Q = mcΔT) — must appear
- Specific latent heat — must appear
- Heating/cooling curves — must appear

Interaction types:
- Part (a): mcq — AO1 — 1 mark (recall: which method of heat transfer does not require a medium)
- Part (b): graph_reading — AO2 — 2 marks (read temperature and time values from a heating/cooling curve; identify the flat section as a state change)
- Part (c): calculation — AO2 — 2 marks (calculate energy using Q = mcΔT)
- Part (d): mcq — AO1 — 1 mark (identify what is happening during the flat section of a heating curve — state change at constant temperature)
- Part (e): self_assessed — AO3 — 4 marks (explain why a metal spoon feels colder than a wooden spoon at the same temperature — link to conduction and thermal conductivity)

Required misconceptions:
- confuses-heat-temperature
- thinks-cold-transfers-to-hot
- confuses-conduction-convection-radiation
- confuses-shc-latent-heat

Graph/Diagram/Data table requirements:
- Heating/cooling curve showing temperature vs time with clear state-change plateaux. Graph type: heating/cooling.

AO spread: AO1: 2, AO2: 4, AO3: 4
Notes: PHY1 compliance: graph type is heating/cooling. PHY2 compliance: formula sheet provided (Q = mcΔT). Graph reading tolerance ±2%.
```

---

#### Topic 16: Energy Resources

```
Scenario ID: phy_16
Mark target: 9
Parts: 5
Icon: 🌍

Required subtopics:
- Renewable vs non-renewable energy sources — must appear
- Sankey diagrams and energy transfer — must appear
- Environmental impact — must appear

Interaction types:
- Part (a): mcq — AO1 — 1 mark (recall: identify which source is renewable from a list)
- Part (b): diagram_label — AO1 — 2 marks (label energy transfers on a Sankey diagram: useful output, wasted output)
- Part (c): data_table — AO2 — 2 marks (interpret a table of energy source data: compare efficiency or output)
- Part (d): mcq — AO1 — 1 mark (identify the main disadvantage of fossil fuels)
- Part (e): self_assessed — AO3 — 3 marks (evaluate the advantages and disadvantages of nuclear power vs wind power for a specific location)

Required misconceptions:
- thinks-renewable-means-unlimited
- confuses-sankey-arrow-widths
- confuses-energy-force

Graph/Diagram/Data table requirements:
- Sankey diagram (SVG) showing energy input, useful output, and wasted energy for a power station. Hotspots for labels.
- Data table comparing 4–5 energy sources: type, annual output (GWh), reliability, CO₂ emissions.

AO spread: AO1: 4, AO2: 2, AO3: 3
Notes: Sankey diagram SVG per curriculum doc. Diagram spec must pass DIA5.
```

---

#### Topic 17: Pressure

```
Scenario ID: phy_17
Mark target: 9
Parts: 5
Icon: 🎈

Required subtopics:
- Pressure = force / area — must appear
- Pressure in fluids and depth (P = hρg) — must appear
- Boyle's Law (PV = constant) — must appear
- Atmospheric pressure — preferred

Interaction types:
- Part (a): mcq — AO1 — 1 mark (recall: the equation for pressure)
- Part (b): numeric_with_unit — AO2 — 2 marks (calculate pressure exerted by an object: P = F/A)
- Part (c): calculation — AO2 — 2 marks (calculate pressure at a depth in a fluid: P = hρg)
- Part (d): mcq — AO1 — 1 mark (identify what happens to gas volume when pressure doubles at constant temperature — Boyle's Law)
- Part (e): self_assessed — AO3 — 3 marks (explain why deep-sea divers must ascend slowly — link to pressure change with depth and dissolved gases)

Required misconceptions:
- confuses-pressure-force
- forgets-depth-pressure-relationship
- confuses-boyles-law-direction
- forgets-to-convert-units

Graph/Diagram/Data table requirements:
- None

AO spread: AO1: 2, AO2: 4, AO3: 3
Notes: PHY2 compliance: formula sheet provided (P = F/A, P = hρg). Clean integers per DIF3.
```

---

### Group 5 · Radioactivity & Space

---

#### Topic 18: Atomic Structure & Radioactivity

```
Scenario ID: phy_18
Mark target: 10
Parts: 5
Icon: ☢️

Required subtopics:
- Proton number, nucleon number, isotopes — must appear
- Alpha, beta, gamma radiation properties — must appear
- Penetration, ionisation, and uses — must appear

Interaction types:
- Part (a): diagram_label — AO1 — 3 marks (label parts of an atom: proton, neutron, electron on a nuclear model diagram)
- Part (b): mcq — AO1 — 1 mark (recall: identify what defines an isotope)
- Part (c): keyword_match — AO2 — 2 marks (match radiation type to its properties: alpha — most ionising, gamma — most penetrating, beta — deflected by electric field)
- Part (d): mcq — AO2 — 1 mark (identify the correct use of gamma radiation from a list: sterilising equipment, not smoke detectors)
- Part (e): self_assessed — AO3 — 3 marks (explain why alpha sources are used in smoke detectors — link to ionisation, penetration, and detection mechanism)

Required misconceptions:
- confuses-alpha-beta-gamma-properties
- confuses-proton-nucleon-number
- confuses-isotopes-elements
- thinks-radiation-makes-radioactive

Graph/Diagram/Data table requirements:
- Nuclear model diagram showing protons, neutrons in nucleus and electrons in shells. Hotspots for labels. Label bank with distractors (e.g. photon, positron, quark).

AO spread: AO1: 4, AO2: 3, AO3: 3
Notes: Diagram spec must pass DIA5.
```

---

#### Topic 19: Radioactive Decay & Half-Life

```
Scenario ID: phy_19
Mark target: 10
Parts: 5
Icon: ⏳

Required subtopics:
- Decay equations (alpha and beta) — must appear
- Half-life definition and calculation — must appear
- Decay graphs — must appear
- Background radiation — preferred

Interaction types:
- Part (a): graph_reading — AO2 — 2 marks (read the count rate at given times from a decay curve; identify the half-life)
- Part (b): calculation — AO2 — 2 marks (calculate the remaining activity after a given number of half-lives)
- Part (c): mcq — AO1 — 1 mark (recall: definition of half-life)
- Part (d): numeric_with_unit — AO2 — 2 marks (determine the number of half-lives elapsed given initial and final activity)
- Part (e): self_assessed — AO3 — 3 marks (explain why a radioactive source with a long half-life is suitable for medical tracers vs industrial gauges — link to half-life, type, and application)

Required misconceptions:
- thinks-half-life-means-half-gone
- confuses-decay-equation-balancing
- thinks-background-radiation-harmful
- thinks-radiation-makes-radioactive

Graph/Diagram/Data table requirements:
- Radioactive decay curve showing activity (count rate) vs time with clear half-life intervals. Graph type: decay curve.

AO spread: AO1: 1, AO2: 6, AO3: 3
Notes: GOLD EXAMPLE. PHY1 compliance: graph type is decay curve. Graph reading tolerance ±2%. AO2 is elevated (60%) due to the calculation-heavy nature of half-life — subject-level and group-level checks govern balance.
```

---

#### Topic 20: Fission & Fusion

```
Scenario ID: phy_20
Mark target: 9
Parts: 5
Icon: ⚛️

Required subtopics:
- Nuclear fission and chain reactions — must appear
- Nuclear fusion and required conditions — must appear
- Nuclear reactor components — must appear
- E = mc² (awareness level) — preferred

Interaction types:
- Part (a): diagram_label — AO1 — 2 marks (label parts of a fission chain reaction diagram: fuel rod, control rod, neutron)
- Part (b): mcq — AO1 — 1 mark (recall: identify the fuel used in most nuclear power stations)
- Part (c): numeric_with_unit — AO2 — 2 marks (calculate energy released using given mass defect and c² — simple multiplication)
- Part (d): mcq — AO1 — 1 mark (identify the conditions required for nuclear fusion — very high temperature and pressure)
- Part (e): self_assessed — AO3 — 3 marks (compare fission and fusion — products, conditions, waste, sustainability)

Required misconceptions:
- confuses-fission-fusion
- confuses-alpha-beta-gamma-properties
- thinks-radiation-makes-radioactive

Graph/Diagram/Data table requirements:
- Fission chain reaction diagram showing neutron hitting nucleus, splitting, releasing neutrons, which hit more nuclei. Hotspots for labels. Distractors in label bank.

AO spread: AO1: 4, AO2: 2, AO3: 3
Notes: PHY2 compliance: formula sheet provided (E = mc²). Diagram spec must pass DIA5.
```

---

#### Topic 21: Space Physics

```
Scenario ID: phy_21
Mark target: 10
Parts: 5
Icon: 🌟

Required subtopics:
- Stellar life cycle — must appear
- Big Bang theory — must appear
- Redshift and CMBR as evidence — must appear

Interaction types:
- Part (a): process_sequence — AO2 — 3 marks (order stages of stellar life cycle: nebula → protostar → main sequence → red giant → ... → white dwarf/neutron star/black hole)
- Part (b): mcq — AO1 — 1 mark (recall: what does a star spend most of its life as)
- Part (c): diagram_label — AO1 — 2 marks (label features on an HR diagram or stellar evolution poster: main sequence, red giant, white dwarf)
- Part (d): mcq — AO1 — 1 mark (identify what redshift in galaxy spectra tells us about the universe)
- Part (e): self_assessed — AO3 — 3 marks (explain how CMBR and redshift provide evidence for the Big Bang theory)

Required misconceptions:
- confuses-star-lifecycle-stages
- thinks-big-bang-was-explosion
- confuses-redshift-blueshift

Graph/Diagram/Data table requirements:
- Stellar lifecycle diagram or HR diagram with hotspot labels. Distractors in label bank.

AO spread: AO1: 4, AO2: 3, AO3: 3
Notes: Diagram spec must pass DIA5.
```

---

#### Topic 22: Gravitational Fields

```
Scenario ID: phy_22
Mark target: 9
Parts: 5
Icon: 🪐

Required subtopics:
- Gravitational field strength — must appear
- Weight vs mass in different gravitational fields — must appear
- Orbital motion and satellites — must appear

Interaction types:
- Part (a): mcq — AO1 — 1 mark (recall: what is gravitational field strength measured in)
- Part (b): calculation — AO2 — 2 marks (calculate weight on Mars given mass and g_Mars)
- Part (c): numeric_with_unit — AO2 — 2 marks (calculate orbital speed given radius and period: v = 2πr/T)
- Part (d): mcq — AO1 — 1 mark (identify what provides the centripetal force for orbital motion — gravity)
- Part (e): self_assessed — AO3 — 3 marks (explain why astronauts appear weightless in orbit — link to free fall, not absence of gravity)

Required misconceptions:
- confuses-weight-mass-space
- thinks-heavier-objects-orbit-faster
- confuses-mass-weight

Graph/Diagram/Data table requirements:
- None

AO spread: AO1: 2, AO2: 4, AO3: 3
Notes: PHY2 compliance: formula sheet provided (W = mg, v = 2πr/T). Clean integers per DIF3.
```

---

## AO Distribution Summary

Calculated from actual per-contract AO values. All figures verified by arithmetic.

| Group | Topics | Total Marks | AO1 | AO2 | AO3 |
|-------|--------|-------------|-----|-----|-----|
| Group 1 · Forces & Motion | T1–T5 | 48 | 13 (27%) | 20 (42%) | 15 (31%) |
| Group 2 · Electricity & Magnetism | T6–T10 | 48 | 15 (31%) | 18 (38%) | 15 (31%) |
| Group 3 · Waves & Light | T11–T14 | 38 | 11 (29%) | 14 (37%) | 13 (34%) |
| Group 4 · Energy | T15–T17 | 28 | 8 (29%) | 10 (36%) | 10 (36%) |
| Group 5 · Radioactivity & Space | T18–T22 | 48 | 15 (31%) | 18 (38%) | 15 (31%) |
| **TOTAL** | **T1–T22** | **210** | **62 (30%)** | **80 (38%)** | **68 (32%)** |

**Subject-level ceiling check:** No AO category exceeds 40%. ✅
**Group-level ceiling check:** No AO category exceeds 45% in any group. ✅

Group 1 AO2 is the highest at 42% — within the 45% ceiling. This is expected given the graph-reading and calculation intensity of Forces & Motion topics.

---

## Validation Checklist (Self-Check)

- [x] All 22 contracts present (phy_01 through phy_22)
- [x] Every contract's parts sum to its mark target (verified per contract)
- [x] Every contract's AO marks sum to its mark target (verified per contract)
- [x] All misconception tags exist in the master list (76 entries)
- [x] All interaction types are from the SC1 approved list
- [x] AO distribution table is calculated from actual per-contract values
- [x] No AO category exceeds 40% at subject level (max is AO2 at 38%)
- [x] No AO category exceeds 45% at group level (max is Group 1 AO2 at 42%)
- [x] PHY1 compliance: every graph_reading part specifies graph type (d-t, v-t, I-V, wave, heating/cooling, decay)
- [x] PHY2 compliance: all equation-of-motion scenarios note "formula sheet provided"
- [x] Grand total marks: 210 (within 208–212 hard range)

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-27 | Initial version. 22 coverage contracts, master misconceptions list (76 entries), AO distribution summary. Driven by Physics_Curriculum_v1_0.docx. 5 gold examples designated: phy_01, phy_02, phy_06, phy_13, phy_19. |

---

**End of Physics Content Brief v1.0**
