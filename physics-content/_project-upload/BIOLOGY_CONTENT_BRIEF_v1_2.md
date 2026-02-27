# GCSE Biology — Content Brief
## Edexcel IGCSE Biology (4BI1) · Higher Tier
### Version 1.2 · February 2026

**Purpose:** This document defines the 21 coverage contracts that govern Biology scenario authoring. Each contract specifies exactly what a scenario must contain — required subtopics, interaction types, AO spread, mark targets, and misconceptions. It also contains the master misconceptions list (per TAG1–TAG2 in the authoring rules).

**Governing documents:**
- `SCIENCE_CONTENT_AUTHORING_RULES_v1_1.md` — quality rules, marking conventions, tag taxonomy
- `UNIFIED_SCENARIO_SCHEMA_v1_3.md` — JSON schema
- `Biology_Curriculum_v1_0.docx` — curriculum source of truth

**Build order (by exam weight):**
1. Group 2 — Infection, Response & Bioenergetics (T6–T10): 5 scenarios
2. Group 5 — Genetics, Evolution & Ecology (T18–T21): 4 scenarios
3. Group 1 — Cell Biology & Organisation (T1–T5): 5 scenarios
4. Group 3 — Exchange & Transport (T11–T13): 3 scenarios
5. Group 4 — Nervous System & Homeostasis (T14–T17): 4 scenarios

**Existing head start:** Scenarios bio_01 through bio_10 are fully specified in `BIOLOGY_CLAUDE_CODE_BRIEF.md`. Sprint 2a transcribes these into schema-compliant JSON. Sprint 2b authors the remaining 11 scenarios (T11–T21) from these contracts.

**Target totals:** 21 scenarios, ~100 questions, ~200 marks.

**Target AO distribution (subject-level):** AO1: ~30%, AO2: ~40%, AO3: ~30%. Per CS2/academic QA: no individual AO category may exceed 40% of total marks.

---

## Master Misconceptions List

Per TAG1–TAG2, all misconception tags used in Biology scenarios must be selected from this list. New tags require formal addition here before use in any scenario file.

Each entry includes the tag and a one-line description of the real student error it represents.

### Cell Biology & Organisation
| Tag | Student Error |
|-----|---------------|
| `confuses-organelles` | Places cell wall in animal cells, or chloroplasts in animal cells |
| `confuses-mitochondria-chloroplast` | Swaps the functions of mitochondria and chloroplasts |
| `resolution-vs-magnification` | Thinks higher magnification automatically means better resolution |
| `forgets-unit-conversion-microscopy` | Fails to convert mm to µm (or vice versa) in magnification calculations |
| `confuses-prokaryotic-eukaryotic` | Confuses prokaryotic (no membrane-bound nucleus) and eukaryotic (membrane-bound nucleus) cells |
| `thinks-mitosis-produces-gametes` | Confuses mitosis (growth/repair) with meiosis (gamete production) |
| `thinks-stem-cells-only-in-embryos` | Doesn't know adult stem cells exist (e.g. bone marrow) |
| `confuses-diffusion-osmosis` | Uses "diffusion" when the question is about water moving through a membrane |
| `confuses-osmosis-direction` | Thinks water moves from high to low concentration (instead of low to high solute) |
| `forgets-active-transport-needs-energy` | Thinks all transport across membranes is passive |
| `confuses-enzyme-substrate` | Swaps enzyme and substrate roles in lock-and-key model |
| `confuses-digestive-organs-order` | Puts digestive organs in wrong sequence (e.g. stomach before oesophagus) |
| `thinks-bile-is-an-enzyme` | Believes bile chemically digests fats rather than emulsifying them |
| `confuses-arteries-veins` | Swaps structural features or functions of arteries and veins |
| `thinks-all-blood-vessels-have-valves` | Doesn't know only veins have valves |
| `confuses-double-single-circulation` | Doesn't understand why blood passes through the heart twice |

### Infection, Response & Bioenergetics
| Tag | Student Error |
|-----|---------------|
| `confuses-bacteria-viruses` | Attributes virus characteristics to bacteria or vice versa |
| `thinks-antibiotics-kill-viruses` | Believes antibiotics work against viral infections |
| `confuses-antibodies-antigens` | Swaps the definitions of antibodies and antigens |
| `thinks-vaccination-contains-active-pathogen` | Believes vaccines inject live, dangerous pathogens |
| `confuses-phagocytosis-antibody-response` | Mixes up non-specific and specific immune responses |
| `thinks-white-cells-eat-all-pathogens` | Oversimplifies — forgets antibody/antitoxin responses |
| `confuses-photosynthesis-respiration-equations` | Swaps the word equations for photosynthesis and respiration |
| `thinks-plants-only-photosynthesise` | Doesn't know plants also respire |
| `thinks-photosynthesis-happens-at-night` | Confuses when photosynthesis and respiration occur |
| `confuses-limiting-factors` | Cannot identify which factor is limiting from a graph |
| `thinks-enzymes-die-at-high-temp` | Says enzymes "die" rather than "denature" at high temperatures |
| `confuses-rate-with-amount` | Confuses rate of reaction with total amount of product |
| `thinks-all-enzymes-have-same-optimum` | Doesn't know different enzymes have different optimal temperatures/pH |
| `thinks-respiration-is-breathing` | Equates cellular respiration with the physical act of breathing |
| `confuses-aerobic-anaerobic-products` | Mixes up the products of aerobic and anaerobic respiration |
| `thinks-anaerobic-produces-no-energy` | Believes anaerobic respiration releases no energy at all |
| `forgets-oxygen-debt` | Doesn't mention oxygen debt when explaining post-exercise recovery |

### Exchange & Transport
| Tag | Student Error |
|-----|---------------|
| `confuses-respiration-gas-exchange` | Uses "respiration" to mean gas exchange in the lungs |
| `thinks-oxygen-actively-pumped` | Believes O₂ is actively transported rather than diffusing |
| `forgets-co2-moves-opposite` | Omits that CO₂ diffuses in the opposite direction to O₂ |
| `confuses-alveoli-adaptations` | Cannot explain why thin walls/large SA/good blood supply aid gas exchange |
| `confuses-trachea-oesophagus` | Mixes up the windpipe and food pipe |
| `confuses-stomata-function` | Doesn't understand stomata allow gas exchange and water loss |
| `thinks-transpiration-is-photosynthesis` | Confuses water loss through leaves with photosynthesis |
| `confuses-xylem-phloem` | Swaps the functions of xylem (water up) and phloem (sugars up/down) |
| `thinks-translocation-is-passive` | Doesn't know translocation requires energy (active process) |
| `confuses-transpiration-factors` | Cannot predict how humidity/wind/temperature affect transpiration rate |

### Nervous System, Hormones & Homeostasis
| Tag | Student Error |
|-----|---------------|
| `confuses-neuron-types` | Swaps sensory, relay, and motor neuron functions or positions |
| `confuses-reflex-arc-order` | Gets the sequence of the reflex arc wrong |
| `thinks-brain-controls-reflexes` | Believes reflex actions involve conscious brain processing |
| `confuses-cns-pns` | Mixes up central and peripheral nervous system components |
| `confuses-brain-regions` | Swaps functions of cerebrum, cerebellum, and medulla |
| `confuses-eye-structures` | Mislabels or swaps functions of lens, retina, iris, pupil |
| `confuses-accommodation` | Doesn't understand how the lens changes shape for near/far vision |
| `confuses-insulin-glucagon` | Swaps the roles of insulin (lowers blood glucose) and glucagon (raises it) |
| `thinks-diabetes-type1-is-diet` | Confuses cause of Type 1 (autoimmune) with Type 2 (lifestyle) |
| `confuses-negative-feedback-direction` | Thinks negative feedback amplifies rather than reverses a change |
| `confuses-adh-function` | Doesn't understand ADH increases water reabsorption in kidneys |
| `confuses-thermoregulation-responses` | Swaps vasoconstriction/vasodilation or shivering/sweating responses |
| `confuses-hormones-nerves` | Cannot distinguish hormonal (slow, long-lasting) from nervous (fast, short) responses |

### Genetics, Evolution & Ecology
| Tag | Student Error |
|-----|---------------|
| `confuses-gene-allele-chromosome` | Cannot distinguish between gene, allele, and chromosome |
| `dominant-means-more-common` | Thinks dominant alleles are always more frequent in a population |
| `confuses-genotype-phenotype` | Swaps genotype (genetic makeup) and phenotype (observable trait) |
| `confuses-homozygous-heterozygous` | Mixes up Ff (heterozygous) and FF/ff (homozygous) |
| `punnett-allele-order-error` | Places alleles incorrectly in Punnett square headers |
| `confuses-continuous-discontinuous` | Cannot distinguish continuous (height) from discontinuous (blood group) variation |
| `thinks-mutations-always-harmful` | Doesn't know mutations can be neutral or beneficial |
| `confuses-natural-artificial-selection` | Mixes up natural selection (environment) with selective breeding (humans) |
| `thinks-evolution-is-intentional` | Believes organisms "choose" to evolve or adapt deliberately |
| `confuses-classification-groups` | Gets the order of taxonomic groups wrong (kingdom → species) |
| `confuses-food-chain-energy-flow` | Thinks energy is recycled rather than lost at each trophic level |
| `forgets-sampling-method-limitations` | Doesn't acknowledge quadrat/transect limitations when interpreting data |
| `confuses-biodiversity-abundance` | Thinks more individuals = more biodiversity (ignores species richness) |
| `confuses-abiotic-biotic` | Mixes up living (biotic) and non-living (abiotic) factors |

### Cross-Topic — Investigation & Data Handling
| Tag | Student Error |
|-----|---------------|
| `includes-anomalies-in-mean` | Includes obvious outliers when calculating a mean instead of identifying and excluding them |

---

## Coverage Contracts

### Group 1 · Cell Biology & Organisation

---

#### Topic 1: Cell Structure

```
Scenario ID: bio_01
Mark target: 10
Parts: 5
Icon: 🔬

Required subtopics:
- Animal & plant cell organelles — must appear
- Prokaryotic vs eukaryotic — must appear
- Microscopy & magnification calculations — must appear

Interaction types:
- Part (a): diagram_label — AO1 — 5 marks (label plant cell structures)
- Part (b): mcq — AO1 — 1 mark (prokaryotic vs eukaryotic)
- Part (c): mcq — AO2 — 1 mark (organelle function — application)
- Part (d): calculation — AO2 — 2 marks (magnification = image size ÷ actual size)
- Part (e): mcq — AO2 — 1 mark (microscope type for seeing ribosomes)

Required misconceptions:
- confuses-mitochondria-chloroplast
- resolution-vs-magnification
- confuses-organelles
- confuses-prokaryotic-eukaryotic

Diagram requirements:
- Plant cell with 5 hotspots for cell wall, nucleus, chloroplast, vacuole, 
  cell membrane. Label bank includes distractors: mitochondria, ribosome, cytoplasm.

AO spread: AO1: 6, AO2: 4, AO3: 0
Notes: Existing scenario in BIOLOGY_CLAUDE_CODE_BRIEF.md — transcribed with contract corrections.
  Original contract had AO spread summing to 8 (not 10). Resolved by increasing 
  diagram to 5 marks. Part (c) upgraded from AO1 recall to AO2 application.
```

---

#### Topic 2: Cell Division

```
Scenario ID: bio_02
Mark target: 9
Parts: 4
Icon: 🧬

Required subtopics:
- Mitosis stages (PMAT) — must appear
- Cell cycle — must appear
- Stem cells — must appear

Interaction types:
- Part (a): process_sequence — AO2 — 3 marks (order mitosis stages)
- Part (b): mcq — AO1 — 1 mark (purpose of mitosis)
- Part (c): diagram_label — AO1 — 2 marks (label chromosome structures)
- Part (d): explain — AO3 — 3 marks (advantages and risks of stem cell use)

Required misconceptions:
- thinks-mitosis-produces-gametes
- thinks-stem-cells-only-in-embryos

Diagram requirements:
- Cell diagram showing chromosomes at a stage of mitosis

AO spread: AO1: 3, AO2: 3, AO3: 3
```

---

#### Topic 3: Transport in Cells

```
Scenario ID: bio_03
Mark target: 10
Parts: 5
Icon: 💧

Required subtopics:
- Diffusion — must appear
- Osmosis — must appear
- Active transport — must appear
- SA:V ratio — preferred

Interaction types:
- Part (a): mcq — AO1 — 1 mark (definition of diffusion)
- Part (b): graph_reading — AO2 — 2 marks (read osmosis data from graph)
- Part (c): numeric — AO2 — 2 marks (calculate percentage change in mass)
- Part (d): mcq — AO2 — 1 mark (identify active transport scenario)
- Part (e): explain — AO3 — 4 marks (explain why SA:V ratio matters for cells)

Required misconceptions:
- confuses-diffusion-osmosis
- confuses-osmosis-direction
- forgets-active-transport-needs-energy

Graph requirements:
- Mass change vs sucrose concentration for osmosis investigation

AO spread: AO1: 1, AO2: 5, AO3: 4
```

---

#### Topic 4: Organisation — Digestion

```
Scenario ID: bio_04
Mark target: 10
Parts: 5
Icon: 🍽️

Required subtopics:
- Digestive system organs and order — must appear
- Enzymes (amylase, protease, lipase) — must appear
- Bile function — must appear

Interaction types:
- Part (a): diagram_label — AO1 — 3 marks (label digestive organs)
- Part (b): process_sequence — AO2 — 2 marks (order of digestion stages)
- Part (c): mcq — AO1 — 1 mark (enzyme-substrate matching)
- Part (d): graph_reading — AO2 — 2 marks (read enzyme activity vs pH)
- Part (e): explain — AO3 — 2 marks (explain role of bile)

Required misconceptions:
- confuses-enzyme-substrate
- thinks-bile-is-an-enzyme
- confuses-digestive-organs-order

Diagram requirements:
- Digestive system overview with hotspots for mouth, oesophagus, stomach, 
  small intestine, large intestine, liver, pancreas

Graph requirements:
- Enzyme activity vs pH curve (bell-shaped, optimum at pH ~2 for pepsin)

AO spread: AO1: 4, AO2: 4, AO3: 2
```

---

#### Topic 5: Organisation — Circulation

```
Scenario ID: bio_05
Mark target: 10
Parts: 5
Icon: ❤️

Required subtopics:
- Heart structure (4 chambers) — must appear
- Blood vessels (artery, vein, capillary) — must appear
- Double circulation — must appear

Interaction types:
- Part (a): diagram_label — AO1 — 3 marks (label heart chambers and vessels)
- Part (b): process_sequence — AO2 — 2 marks (blood flow through heart)
- Part (c): mcq — AO2 — 1 mark (compare artery and vein features)
- Part (d): mcq — AO1 — 1 mark (function of valves)
- Part (e): explain — AO3 — 3 marks (explain why double circulation is more efficient)

Required misconceptions:
- confuses-arteries-veins
- thinks-all-blood-vessels-have-valves
- confuses-double-single-circulation

Diagram requirements:
- Heart cross-section with hotspots for left/right atrium, left/right ventricle,
  aorta, pulmonary artery, vena cava, pulmonary vein. Label bank includes 
  distractors: coronary artery, septum.

AO spread: AO1: 4, AO2: 3, AO3: 3
```

---

### Group 2 · Infection, Response & Bioenergetics

---

#### Topic 6: Infection & Disease

```
Scenario ID: bio_06
Mark target: 9
Parts: 4
Icon: 🦠

Required subtopics:
- Types of pathogens (bacteria, viruses, fungi, protists) — must appear
- How diseases spread — must appear
- Plant disease — preferred

Interaction types:
- Part (a): mcq — AO1 — 1 mark (identify pathogen type from description)
- Part (b): keyword_match — AO1 — 2 marks (match pathogen types to diseases)
- Part (c): mcq — AO2 — 1 mark (identify transmission method)
- Part (d): explain — AO3 — 3 marks (explain how a named disease spreads and can be prevented)

Required misconceptions:
- confuses-bacteria-viruses
- thinks-antibiotics-kill-viruses

Diagram requirements: None

AO spread: AO1: 3, AO2: 3, AO3: 3
Notes: Existing scenario spec in BIOLOGY_CLAUDE_CODE_BRIEF.md (maps to original scenario 3 "Infection & Response").
```

---

#### Topic 7: Immune Response

```
Scenario ID: bio_07
Mark target: 10
Parts: 5
Icon: 🛡️

Required subtopics:
- Non-specific defences (skin, mucus, cilia) — must appear
- Phagocytosis — must appear
- Antibodies & vaccination — must appear

Interaction types:
- Part (a): mcq — AO1 — 1 mark (identify non-specific defence)
- Part (b): process_sequence — AO2 — 2 marks (order phagocytosis steps)
- Part (c): diagram_label — AO1 — 2 marks (label phagocyte/antibody diagram)
- Part (d): mcq — AO2 — 1 mark (why vaccination prevents disease)
- Part (e): explain — AO3 — 4 marks (explain why antibiotics don't work on viruses)

Required misconceptions:
- confuses-antibodies-antigens
- thinks-vaccination-contains-active-pathogen
- confuses-phagocytosis-antibody-response
- thinks-antibiotics-kill-viruses

Diagram requirements:
- Phagocytosis sequence diagram or antibody-antigen binding diagram

AO spread: AO1: 3, AO2: 3, AO3: 4
```

---

#### Topic 8: Photosynthesis

```
Scenario ID: bio_08
Mark target: 11
Parts: 5
Icon: 🌿

Required subtopics:
- Word/symbol equation — must appear
- Limiting factors (light, CO₂, temperature) — must appear
- Leaf structure adaptations — must appear

Interaction types:
- Part (a): keyword_match — AO1 — 2 marks (complete photosynthesis equation)
- Part (b): graph_reading — AO2 — 2 marks (read rate from light intensity graph)
- Part (c): mcq — AO2 — 1 mark (identify the limiting factor from graph)
- Part (d): diagram_label — AO1 — 3 marks (label leaf cross-section structures)
- Part (e): explain — AO3 — 3 marks (explain how leaves are adapted for photosynthesis)

Required misconceptions:
- confuses-photosynthesis-respiration-equations
- thinks-plants-only-photosynthesise
- confuses-limiting-factors

Graph requirements:
- Rate of photosynthesis vs light intensity curve (plateau at high intensity)

Diagram requirements:
- Leaf cross-section with hotspots for upper epidermis, palisade mesophyll,
  spongy mesophyll, guard cells, stomata, vein/vascular bundle. Distractors:
  cuticle, air space.

AO spread: AO1: 5, AO2: 3, AO3: 3
```

---

#### Topic 9: Respiration

```
Scenario ID: bio_09
Mark target: 9
Parts: 5
Icon: 🔥

Required subtopics:
- Aerobic respiration equation — must appear
- Anaerobic respiration (animals and yeast) — must appear
- Oxygen debt — must appear

Interaction types:
- Part (a): keyword_match — AO1 — 2 marks (complete aerobic respiration equation)
- Part (b): mcq — AO1 — 1 mark (organelle for aerobic respiration)
- Part (c): keyword_match — AO1 — 1 mark (anaerobic in humans → lactic acid)
- Part (d): mcq — AO2 — 1 mark (anaerobic in yeast → ethanol + CO₂)
- Part (e): explain — AO3 — 4 marks (explain muscle fatigue and oxygen debt)

Required misconceptions:
- thinks-respiration-is-breathing
- confuses-aerobic-anaerobic-products
- forgets-oxygen-debt
- thinks-anaerobic-produces-no-energy

Diagram requirements: None

AO spread: AO1: 4, AO2: 1, AO3: 4
Notes: Existing scenario spec in BIOLOGY_CLAUDE_CODE_BRIEF.md (scenario 8).
```

---

#### Topic 10: Enzyme Action

```
Scenario ID: bio_10
Mark target: 11
Parts: 5
Icon: ⚗️

Required subtopics:
- Lock-and-key / enzyme-substrate specificity — must appear
- Effect of temperature on enzyme activity — must appear
- Denaturation — must appear

Interaction types:
- Part (a): graph_reading — AO2 — 2 marks (read optimum temperature from curve)
- Part (b): explain — AO3 — 3 marks (explain why activity decreases above optimum)
- Part (c): calculation — AO2 — 2 marks (calculate rate of reaction from data)
- Part (d): mcq — AO1 — 1 mark (lock-and-key model identification)
- Part (e): explain — AO3 — 3 marks (predict effect of pH change on enzyme)

Required misconceptions:
- thinks-enzymes-die-at-high-temp
- confuses-rate-with-amount
- thinks-all-enzymes-have-same-optimum

Graph requirements:
- Enzyme activity vs temperature curve (bell-shaped, optimum at ~37°C, 
  x-axis 0–80°C step 10, y-axis 0–30 arbitrary units step 5, smooth line)

AO spread: AO1: 1, AO2: 4, AO3: 6
```

---

### Group 3 · Exchange & Transport

---

#### Topic 11: Gas Exchange — Lungs

```
Scenario ID: bio_11
Mark target: 11
Parts: 5
Icon: 🫁

Required subtopics:
- Lung structure (trachea, bronchi, alveoli) — must appear
- Alveoli adaptations for gas exchange — must appear
- Diffusion of O₂ and CO₂ — must appear

Interaction types:
- Part (a): diagram_label — AO1 — 3 marks (label lung structures)
- Part (b): diagram_label — AO2 — 2 marks (label O₂/CO₂ diffusion directions on alveolus)
- Part (c): mcq — AO1 — 1 mark (process that moves O₂ into blood)
- Part (d): explain — AO3 — 4 marks (explain alveoli adaptations for gas exchange)
- Part (e): mcq — AO2 — 1 mark (identify what would NOT increase gas exchange rate)

Required misconceptions:
- confuses-respiration-gas-exchange
- thinks-oxygen-actively-pumped
- forgets-co2-moves-opposite
- confuses-alveoli-adaptations

Diagram requirements:
- Lung overview: trachea, bronchi, bronchioles, diaphragm with hotspots. 
  Distractors: oesophagus, larynx.
- Alveolus close-up: capillary, red blood cells, O₂/CO₂ diffusion arrows, 
  thin wall indication.

AO spread: AO1: 4, AO2: 3, AO3: 4
Notes: Existing scenario spec in PRD Section 14.1.
```

---

#### Topic 12: Gas Exchange — Plants

```
Scenario ID: bio_12
Mark target: 10
Parts: 5
Icon: 🍃

Required subtopics:
- Stomata and guard cells — must appear
- Transpiration — must appear
- Factors affecting transpiration rate — must appear

Interaction types:
- Part (a): diagram_label — AO1 — 2 marks (label stomata/guard cells on leaf surface)
- Part (b): mcq — AO1 — 1 mark (function of stomata)
- Part (c): graph_reading — AO2 — 2 marks (read transpiration rate from potometer data)
- Part (d): numeric — AO2 — 2 marks (calculate transpiration rate = distance ÷ time)
- Part (e): explain — AO3 — 3 marks (explain how humidity affects transpiration rate)

Required misconceptions:
- confuses-stomata-function
- thinks-transpiration-is-photosynthesis
- confuses-transpiration-factors

Graph requirements:
- Transpiration rate vs time under different conditions (e.g. with/without fan)

Diagram requirements:
- Leaf surface view showing open stomata, guard cells. Distractors: 
  palisade cell, epidermal cell.

AO spread: AO1: 3, AO2: 4, AO3: 3
```

---

#### Topic 13: Transport in Plants

```
Scenario ID: bio_13
Mark target: 9
Parts: 4
Icon: 🌳

Required subtopics:
- Xylem and phloem structure and function — must appear
- Translocation — must appear
- Root hair cell absorption — preferred

Interaction types:
- Part (a): diagram_label — AO1 — 3 marks (label xylem, phloem, root hair cell on plant cross-section)
- Part (b): mcq — AO2 — 1 mark (identify which tissue transports sugars)
- Part (c): process_sequence — AO2 — 2 marks (order of water transport from soil to leaf)
- Part (d): explain — AO3 — 3 marks (explain why phloem transport requires energy but xylem doesn't)

Required misconceptions:
- confuses-xylem-phloem
- thinks-translocation-is-passive

Diagram requirements:
- Plant stem cross-section or root cross-section with hotspots for xylem, phloem, 
  root hair cell, cortex. Distractors: cambium, epidermis.

AO spread: AO1: 3, AO2: 3, AO3: 3
```

---

### Group 4 · Nervous System, Hormones & Homeostasis

---

#### Topic 14: Nervous System

```
Scenario ID: bio_14
Mark target: 10
Parts: 5
Icon: ⚡

Required subtopics:
- Reflex arc (receptor → sensory → relay → motor → effector) — must appear
- Neuron types — must appear
- Reaction time investigation — preferred

Interaction types:
- Part (a): diagram_label — AO1 — 3 marks (label neuron types on reflex arc)
- Part (b): process_sequence — AO2 — 2 marks (order reflex arc steps)
- Part (c): mcq — AO1 — 1 mark (why reflexes are fast and automatic)
- Part (d): numeric — AO2 — 2 marks (calculate mean reaction time from data)
- Part (e): explain — AO3 — 2 marks (explain why reflexes don't involve conscious thought)

Required misconceptions:
- confuses-neuron-types
- confuses-reflex-arc-order
- thinks-brain-controls-reflexes

Diagram requirements:
- Reflex arc diagram showing receptor, sensory neuron, relay neuron (in spinal cord),
  motor neuron, effector (muscle). Distractors: brain, interneuron.

AO spread: AO1: 4, AO2: 4, AO3: 2
Notes: Existing scenario spec in BIOLOGY_CLAUDE_CODE_BRIEF.md (scenario 9).
```

---

#### Topic 15: The Brain & Eye

```
Scenario ID: bio_15
Mark target: 9
Parts: 4
Icon: 👁️

Required subtopics:
- Brain regions (cerebrum, cerebellum, medulla) — must appear
- Eye structure — must appear
- Accommodation (focusing) — must appear

Interaction types:
- Part (a): diagram_label — AO1 — 3 marks (label brain regions)
- Part (b): mcq — AO1 — 1 mark (match brain region to function)
- Part (c): diagram_label — AO1 — 3 marks (label eye structures)
- Part (d): explain — AO3 — 2 marks (explain how the eye focuses on near objects)

Required misconceptions:
- confuses-brain-regions
- confuses-eye-structures
- confuses-accommodation

Diagram requirements:
- Brain diagram with hotspots for cerebrum, cerebellum, medulla oblongata.
  Distractors: hypothalamus, pituitary gland.
- Eye cross-section with hotspots for cornea, iris, lens, retina, optic nerve.
  Distractors: sclera, pupil (note: pupil is a gap, not a structure).

AO spread: AO1: 7, AO2: 0, AO3: 2
Notes: Heavy AO1 by design — this topic is recall/labelling-dense. AO3 comes from accommodation explanation.
```

---

#### Topic 16: Hormones & Endocrine System

```
Scenario ID: bio_16
Mark target: 10
Parts: 5
Icon: 🧪

Required subtopics:
- Endocrine glands — must appear
- Insulin and glucagon (blood glucose regulation) — must appear
- Negative feedback — must appear

Interaction types:
- Part (a): diagram_label — AO1 — 2 marks (label endocrine glands on body outline)
- Part (b): mcq — AO1 — 1 mark (identify hormone from description)
- Part (c): process_sequence — AO2 — 3 marks (order negative feedback loop for blood glucose)
- Part (d): mcq — AO2 — 1 mark (what happens when blood glucose rises)
- Part (e): explain — AO3 — 3 marks (explain difference between Type 1 and Type 2 diabetes)

Required misconceptions:
- confuses-insulin-glucagon
- thinks-diabetes-type1-is-diet
- confuses-negative-feedback-direction
- confuses-hormones-nerves

Diagram requirements:
- Human body outline with hotspots for pituitary, thyroid, adrenal glands, 
  pancreas, ovaries/testes. Distractors: liver, kidneys.

AO spread: AO1: 3, AO2: 4, AO3: 3
```

---

#### Topic 17: Homeostasis

```
Scenario ID: bio_17
Mark target: 10
Parts: 5
Icon: 🌡️

Required subtopics:
- Blood glucose regulation — must appear (links to T16 but tested via graph here)
- Thermoregulation — must appear
- Osmoregulation (ADH, kidneys) — must appear

Interaction types:
- Part (a): graph_reading — AO2 — 2 marks (read blood glucose level from graph after meal)
- Part (b): mcq — AO1 — 1 mark (identify organ that monitors blood glucose)
- Part (c): process_sequence — AO2 — 2 marks (order thermoregulation response to cold)
- Part (d): mcq — AO2 — 1 mark (effect of ADH on kidney tubules)
- Part (e): explain — AO3 — 4 marks (explain how the body responds when temperature rises)

Required misconceptions:
- confuses-thermoregulation-responses
- confuses-adh-function
- confuses-negative-feedback-direction

Graph requirements:
- Blood glucose concentration vs time graph (spike after meal, insulin response,
  return to normal). x-axis: time in minutes (0–120, step 30). y-axis: 
  glucose concentration mg/dL (60–160, step 20). Smooth line.

AO spread: AO1: 1, AO2: 5, AO3: 4
Notes: BIO1 applies — references insulin/glucagon from T16 in context, but core marks test homeostasis mechanisms not hormone identity.
```

---

### Group 5 · Genetics, Evolution & Ecology

---

#### Topic 18: DNA & Inheritance

```
Scenario ID: bio_18
Mark target: 11
Parts: 5
Icon: 🧬

Required subtopics:
- DNA structure, genes, alleles — must appear
- Dominant/recessive, genotype/phenotype — must appear
- Punnett square cross — must appear

Interaction types:
- Part (a): mcq — AO1 — 1 mark (definition of allele)
- Part (b): keyword_match — AO1 — 2 marks (match genetic terms to definitions)
- Part (c): punnett_grid — AO2 — 4 marks (complete Ff × Ff cross)
- Part (d): calculate — AO2 — 1 mark (probability of homozygous recessive offspring)
- Part (e): explain — AO3 — 3 marks (explain why two carrier parents can have an affected child)

Required misconceptions:
- confuses-gene-allele-chromosome
- dominant-means-more-common
- confuses-genotype-phenotype
- confuses-homozygous-heterozygous
- punnett-allele-order-error

Diagram requirements: None (Punnett grid is the interactive component)

AO spread: AO1: 3, AO2: 5, AO3: 3
Notes: BIO3 applies — Punnett grid (part c) and probability interpretation (part d) are separate parts with separate marks.
```

---

#### Topic 19: Variation & Mutation

```
Scenario ID: bio_19
Mark target: 9
Parts: 4
Icon: 🔄

Required subtopics:
- Continuous vs discontinuous variation — must appear
- Mutations (causes and effects) — must appear
- Genetic modification / selective breeding — preferred

Interaction types:
- Part (a): mcq — AO1 — 1 mark (identify continuous vs discontinuous from examples)
- Part (b): data_table — AO2 — 4 marks (interpret variation data from a table: identify pattern, range, type of variation, justify from data)
- Part (c): mcq — AO2 — 1 mark (identify what increases mutation rate)
- Part (d): explain — AO3 — 3 marks (evaluate advantages and disadvantages of GM crops)

Required misconceptions:
- confuses-continuous-discontinuous
- thinks-mutations-always-harmful

Data table requirements:
- Table showing trait measurements across a sample (e.g. heights of 20 students,
  or blood group frequencies)

AO spread: AO1: 1, AO2: 5, AO3: 3
Notes: No graph_reading in this scenario despite curriculum doc listing it — data_table better suits variation data. Graph_reading covered extensively in T10, T11, T12, T17. Part (b) increased from 2→4 marks in v1.1 to resolve contract gap (parts previously summed to 7, not 9).
```

---

#### Topic 20: Evolution & Natural Selection

```
Scenario ID: bio_20
Mark target: 10
Parts: 5
Icon: 🦎

Required subtopics:
- Darwin's theory of natural selection — must appear
- Evidence for evolution — must appear
- Antibiotic resistance — must appear

Interaction types:
- Part (a): mcq — AO1 — 1 mark (identify Darwin from description of theory)
- Part (b): process_sequence — AO2 — 3 marks (order steps of natural selection)
- Part (c): mcq — AO2 — 1 mark (identify evidence for evolution)
- Part (d): explain — AO3 — 3 marks (explain how antibiotic resistance develops in bacteria)
- Part (e): diagram_label — AO1 — 2 marks (label features on an evolutionary tree)

Required misconceptions:
- thinks-evolution-is-intentional
- confuses-natural-artificial-selection
- confuses-classification-groups

Diagram requirements:
- Simple evolutionary tree (cladogram) with 4–5 species, branch points labelled.
  Hotspots at branch points and terminal nodes. Distractors: common ancestor label options.

AO spread: AO1: 3, AO2: 4, AO3: 3
```

---

#### Topic 21: Ecology

```
Scenario ID: bio_21
Mark target: 10
Parts: 5
Icon: 🌍

Required subtopics:
- Food chains/webs and energy flow — must appear
- Sampling methods (quadrats, transects) — must appear
- Biodiversity — must appear

Interaction types:
- Part (a): mcq — AO1 — 1 mark (identify producer/consumer/decomposer)
- Part (b): calculation — AO2 — 2 marks (calculate population estimate from quadrat data)
- Part (c): data_table — AO2 — 2 marks (interpret species frequency data from quadrat survey)
- Part (d): graph_reading — AO2 — 2 marks (read trend from transect data graph)
- Part (e): explain — AO3 — 3 marks (explain why biodiversity is important and how humans affect it)

Required misconceptions:
- confuses-food-chain-energy-flow
- forgets-sampling-method-limitations
- confuses-biodiversity-abundance
- confuses-abiotic-biotic

Graph requirements:
- Species distribution along a transect (x-axis: distance in metres, 
  y-axis: number of organisms, bar chart or line graph)

Data table requirements:
- Quadrat survey results: species name, tally, frequency across 10 quadrats

AO spread: AO1: 1, AO2: 6, AO3: 3
Notes: Heaviest calculation/data topic in Biology. Ensure quadrat calculation uses exact integers per MC1.
```

---

## AO Distribution Summary

| Group | Topics | Total Marks | AO1 | AO2 | AO3 |
|-------|--------|-------------|-----|-----|-----|
| Group 1 · Cell Biology | T1–T5 | 49 | 18 (37%) | 19 (39%) | 12 (24%) |
| Group 2 · Bioenergetics | T6–T10 | 50 | 16 (32%) | 14 (28%) | 20 (40%) |
| Group 3 · Exchange | T11–T13 | 30 | 10 (33%) | 10 (33%) | 10 (33%) |
| Group 4 · Homeostasis | T14–T17 | 39 | 15 (38%) | 13 (33%) | 11 (28%) |
| Group 5 · Genetics | T18–T21 | 40 | 8 (20%) | 20 (50%) | 12 (30%) |
| **TOTAL** | **T1–T21** | **208** | **67 (32%)** | **76 (37%)** | **65 (31%)** |

All AO categories within bounds at subject level. No category exceeds 40%. Group 2 AO3 hits exactly 40% (acceptable ceiling). Group 5 AO2 is elevated at 50% due to data-heavy genetics topics but subject-level check governs.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Feb 2026 | Initial version. 21 coverage contracts, master misconceptions list (63 entries), AO distribution summary. Driven by Biology_Curriculum_v1_0.docx. |
| 1.1 | Feb 2026 | Gold-standard QA corrections. T1 contract revised: diagram increased to 5 marks (5 hotspots on plant cell), AO spread corrected to AO1:6/AO2:4 (was AO1:4/AO2:4 summing to 8, not 10). Part (c) upgraded to AO2 application. T19 contract gap resolved: data_table increased from 2→4 marks (parts now sum to 9). Added `confuses-prokaryotic-eukaryotic` to master misconceptions list (64 entries). AO distribution table recalculated from actual per-topic AO spreads — all groups and grand total corrected. |
| 1.2 | Feb 2026 | TAG2 addition: `includes-anomalies-in-mean` added to master misconceptions list under new "Cross-Topic — Investigation & Data Handling" section (65 entries). Required by bio_14 part (d) mean calculation. Reusable in bio_21, bio_17, and Chemistry practicals. No contract changes. |

---

**End of Biology Content Brief v1.2**
