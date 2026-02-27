# Science Content Authoring Rules
## GCSE Revision Platform — Biology, Chemistry, Physics
### Version 1.2 · February 2026

This document governs all science scenario authoring across Biology, Chemistry, and Physics. It is the science equivalent of the Maths Template Generator Ground Rules — not guidelines, but enforceable conventions. Every scenario JSON file must comply with every applicable rule in this document.

**Scope:** All 65 scenarios across 3 subjects (21 Biology, 21 Physics, 23 Chemistry).

**Schema:** All scenarios conform to `UNIFIED_SCENARIO_SCHEMA_v1_3.md`. This document does not duplicate the schema — it specifies the conventions, quality standards, and constraints that sit above the schema.

---

## 1. Scenario Structure Rules

**S1 — Schema compliance is non-negotiable.** Every scenario JSON must conform to `UNIFIED_SCENARIO_SCHEMA_v1_3.md`. Validate after completion. No placeholder fields, no "fix later" values, no partial answer schemas.

**S2 — Exam authenticity.** Context paragraphs describe realistic experimental setups, observations, or data in 2–4 sentences. They read like the stem of an Edexcel IGCSE paper question. Avoid overly creative or narrative framing — these are exam questions, not stories.

**S3 — Active revision, not recognition.** Prioritise interaction types that require students to produce answers. MCQ is used sparingly — typically for opening recall parts or genuinely discriminating conceptual questions where all four options test a distinct understanding. Diagram labels, process sequences, keyword match, Punnett grids, and calculations are preferred over MCQ wherever the content allows.

**S4 — Scenario count follows the curriculum plan.** Each subject's curriculum document specifies the scenario count per topic. Most topics get one scenario. High-weight topics that receive two are explicitly listed in the curriculum document. Do not add or remove scenarios beyond what the curriculum plan specifies.

**S5 — Mark targets.** Each scenario targets 8–12 marks total. Individual parts: 1–4 marks each. 4–5 parts per scenario. The sum of part marks must exactly equal the scenario's total marks in the manifest.

**S6 — AO progression within scenarios.** Parts should generally progress from AO1 (recall) through AO2 (application) to AO3 (analysis/evaluation). This is not rigid — a scenario may open with an AO2 graph reading if the context demands it — but the overall trajectory should move from easier to harder. The coverage contract for each topic specifies the target AO spread.

**S7 — Context paragraphs are self-contained.** A student should be able to answer every part using only the context paragraph, the visual assets (diagram/graph/data table), and their subject knowledge. No part should require information from outside the scenario.

---

## 2. Difficulty Calibration

**DIF1 — Default difficulty is Foundation/Higher overlap.** Unless the coverage contract specifies otherwise, scenarios target the overlap band — accessible to strong Foundation students, routine for Higher students. This matches the Edexcel IGCSE tier structure where most content is shared.

**DIF2 — AO3 parts must not require content beyond the curriculum document.** Analysis and evaluation questions test deeper thinking about curriculum content, not additional knowledge. If a "predict the outcome" question requires facts not in the spec, it's too hard.

**DIF3 — Calculations must avoid calculator traps unless explicitly testing them.** Numbers should produce clean answers (integers or simple decimals). Avoid values that create recurring decimals, require rounding decisions, or produce ambiguous sig-fig situations — unless the calculation skill being tested is specifically about rounding or significant figures.

**DIF4 — One "stretch" part per scenario maximum.** A stretch part is anything that a competent student might find genuinely challenging (e.g. multi-step AO3 explain, unfamiliar context application). Scenarios should not stack multiple stretch parts — this discourages students and distorts analytics.

**DIF5 — Opening parts must be accessible.** Part (a) should be answerable by any student who has studied the topic. It establishes confidence and provides a mark-earning entry point. Typically AO1, 1–2 marks.

---

## 3. Marking Conventions

These conventions define how answer schemas are constructed and how the marking engine will evaluate student responses. They override subject-specific intuition — a Biology author cannot relax numeric tolerance just because "Biology is less mathematical."

### 3.1 Numeric Answers

**MC1 — Numeric tolerance by subject:**

| Subject | Default Tolerance | Rationale |
|---------|------------------|-----------|
| Physics | ±2% | Accommodates intermediate rounding in multi-step calculations |
| Chemistry (mole calculations) | ±1% | Tighter precision expected for stoichiometry |
| Chemistry (other calculations) | ±2% | Aligns with Physics |
| Biology | Exact integers, zero tolerance | Magnification, cell counts, sampling — answers are inherently exact |
| Biology (rate calculations) | ±2% | Rate = amount ÷ time can produce decimals |

If a specific question requires different tolerance (e.g. a Biology question involving concentration calculations), specify it explicitly in the answer schema and document why.

**MC2 — Unit handling.** Units must always be specified in the answer schema. `unitOptions` provides the dropdown choices. `correctUnit` is the accepted answer. Equivalent units are NOT auto-accepted — if the answer is in mm and the student enters cm, it is marked wrong. This matches Edexcel marking conventions where unit errors lose marks.

**MC3 — Significant figures.** Unless the question explicitly asks for a specific number of significant figures, accept answers to the same precision as the model answer. Do not penalise trailing zeros (e.g. accept both `500` and `500.0` for ×500 magnification).

### 3.2 MCQ

**MC4 — MCQ option construction.** Every MCQ must have exactly 4 options. Exactly 1 is correct. The 3 distractors must each target a distinct, identifiable misconception or error — not random wrong answers. Every distractor should be an answer a real student might arrive at through a specific mistake (e.g. forgetting to convert units, confusing two similar concepts, applying the wrong formula).

**MC5 — MCQ option ordering.** Options are authored in a logical order (e.g. ascending numeric values, or alphabetical for text). The platform shuffles at display time — authors should not try to position the correct answer.

### 3.3 Diagram Labels

**MC6 — Diagram label marking.** Each hotspot = 1 mark. Labels come from a dropdown (not free text), so marking is binary per hotspot. Case-insensitive matching. Label banks must include 2–4 distractors beyond the correct answers. Distractors must be plausible structures from the same system (e.g. for a heart diagram: "pulmonary artery" as a distractor when the hotspot is on the aorta).

### 3.4 Process Sequences

**MC7 — Process sequence marking.** Adjacent-pair scoring: compare each consecutive pair in the student's order against the correct order. Score = (correct adjacent pairs) / (total pairs) × marks available, rounded down to nearest integer. This gives partial credit for "mostly right" sequences while penalising fundamental ordering errors.

### 3.5 Keyword Match

**MC8 — Keyword match strictness.** Blanks accept only exact word-bank matches via dropdown selection (not free text). Word banks include 2–4 distractors beyond the correct answers. Distractors must target common misconceptions — e.g. for aerobic respiration blanks, include "lactic acid" as a distractor.

### 3.6 Punnett Grids

**MC9 — Punnett grid cell marking.** Each cell = 1 mark. Case-insensitive. Allele-order-insensitive: `Ff` = `fF` = correct.

**MC10 — Punnett-derived ratio and probability answers:**
- Ratio answers must be in simplest form. `3:1` is correct; `6:2` is not.
- Probability answers must accept fraction OR decimal to 2dp OR percentage. E.g. for a 1-in-4 chance: `1/4`, `0.25`, and `25%` are all correct.
- The ratio/probability question is marked as a separate part from the grid itself — never bundled into the grid marks.

### 3.7 Self-Assessed / Explain

**MC11 — Self-assessed marking.** In practice mode: student self-marks against a checklist of mark-scheme points. `maxCheckable` equals the marks available for the part. In exam mode: flagged as teacher-marked, 0 auto-marks awarded.

**MC12 — Mark-scheme points must be specific and unambiguous.** Each point is a single assessable statement. "Mentions diffusion" is acceptable. "Explains gas exchange well" is not — too subjective. Points should be checkable as true/false by a student without subject expertise beyond what they've studied.

### 3.8 Graph Reading

**MC13 — Graph reading tolerance.** Accept values within ±0.5 of the smallest visible grid division. If gridlines are every 5 units and the correct answer is 35, accept 34.5–35.5. This matches the precision achievable by reading from a screen with crosshairs.

**MC14 — Graph data must not require interpolation beyond visible grid resolution.** If grid lines are at 10, 20, 30, 40 — do not set a correct answer of 27 (requires estimating between gridlines with false precision). Answers should fall on or very near gridlines.

### 3.9 Equation Balancing (Chemistry Only)

**MC15 — Equation balancer schemas accept only lowest whole-number coefficients.** Many equations can be balanced with scalar multiples (e.g. 2H₂ + O₂ → 2H₂O is equivalent to 4H₂ + 2O₂ → 4H₂O). Only the lowest whole-number coefficient set is accepted as correct. The answer schema must specify this single correct set. The marking engine reduces student-entered coefficients to lowest terms before comparing — so `4,2,4` is auto-reduced to `2,1,2` and marked correct. This must be explicit in every equation balancer answer schema.

**MC16 — Coefficients of 1 are implicit.** Students may omit a coefficient of 1 (standard chemistry convention). The marking engine must treat empty/absent coefficients as 1.

---

## 4. Tag Taxonomy

Tags power analytics, diagnostics, and adaptive learning. Inconsistent tags create false signals and are worse than no tags. All tags are lowercase, kebab-case, and follow the formats below.

### 4.1 Topic Tags

Hierarchical, dot-separated. Every part gets at least one.

```
Format: [subject].[group-name].[topic-name].[subtopic]

Biology examples:
  bio.cell-biology.cell-structure.organelles
  bio.cell-biology.cell-structure.microscopy
  bio.cell-biology.cell-division.mitosis
  bio.bioenergetics.photosynthesis.limiting-factors
  bio.bioenergetics.enzyme-action.temperature
  bio.genetics.inheritance.punnett-squares
  bio.ecology.sampling.quadrats

Physics examples:
  phy.forces.motion-graphs.velocity-time
  phy.forces.momentum.conservation
  phy.electricity.circuits.series-parallel
  phy.waves.light.refraction
  phy.thermal.energy-transfer.conduction

Chemistry examples:
  chem.particles.states-of-matter.changes-of-state
  chem.reactions.mole-calculations.relative-formula-mass
  chem.reactions.rates.collision-theory
  chem.periodic-table.groups.halogens
  chem.organic.hydrocarbons.alkenes
```

**Group names** match the curriculum document's group labels (kebab-cased). **Topic names** match the curriculum document's topic names (kebab-cased). **Subtopics** are specific to the part being assessed.

### 4.2 Skill Tags

Controlled vocabulary. Use these exact tags. Do not invent synonyms — if none fits, extend this list in a future version of this document (not ad hoc in a scenario file).

```
# AO1 — Recall and knowledge
recall-fact                # State, name, or identify a fact
recall-definition          # Define a specific term
recall-equation            # State or select the correct equation
label-diagram              # Identify structures on a diagram

# AO2 — Application
apply-equation             # Substitute values into a formula and solve
rearrange-equation         # Rearrange a formula before substitution
interpret-graph            # Read values or identify features from a graph
describe-trend             # Identify and describe a pattern in data
calculate                  # Multi-step calculation (not just formula substitution)
order-process              # Sequence steps in correct order
complete-punnett           # Fill in a Punnett square correctly
interpret-ratio            # Derive ratio or probability from genetic cross
balance-equation           # Balance a chemical equation
classify                   # Assign items to correct categories
convert-units              # Change between measurement units
interpret-data-table       # Extract and use information from tabular data

# AO3 — Analysis, evaluation, synthesis
explain-mechanism          # Explain how or why a process works
evaluate-method            # Assess strengths and weaknesses of an experimental method
predict-outcome            # Predict what would happen under changed conditions
compare-contrast           # Identify and explain similarities and differences
justify-conclusion         # Use evidence to support a conclusion
suggest-improvement        # Propose changes to an experimental design
```

### 4.3 Misconception Tags

Kebab-case, descriptive. Follow one of these naming patterns:

| Pattern | When to use | Example |
|---------|------------|---------|
| `confuses-x-y` | Student mixes up two concepts | `confuses-diffusion-osmosis` |
| `thinks-x` | Student holds a specific wrong belief | `thinks-enzymes-die-at-high-temp` |
| `assumes-x` | Student makes an unwarranted assumption | `assumes-heavier-falls-faster` |
| `forgets-x` | Student omits a required step | `forgets-to-convert-units` |
| `omits-x` | Student leaves out a key element | `omits-control-variable` |
| `inverse-x` | Student reverses a relationship | `inverse-speed-time-relationship` |
| `x-vs-y` | Student confuses related but distinct concepts | `resolution-vs-magnification` |

Every part must have at least 1 misconception tag. Misconceptions must be **real and common** — things students actually get wrong, documented in examiner reports or well-known in teaching. If unsure whether a misconception is genuinely common, flag it with a JSON comment or a note in the manifest for academic QA review.

**TAG1 — Misconception tags must be selected from the subject's approved master list.** Each subject content brief includes a master misconceptions list. Authors select from this list. Do not invent new misconception tags ad hoc in a scenario file.

**TAG2 — New misconception tags require formal addition.** If a scenario genuinely needs a misconception not on the master list, add it to the subject content brief's master list first (with a brief description of the real student error it represents), then reference it in the scenario. This prevents synonym drift — e.g. `confuses-rate-with-speed`, `confuses-speed-and-rate`, and `speed-rate-confusion` all meaning the same thing but being analytically distinct strings.

### 4.4 Tag Minimums Per Part

| Tag type | Minimum per part | Maximum per part |
|----------|-----------------|-----------------|
| Topic tags | 1 | 3 |
| Skill tags | 1 | 2 |
| Misconception tags | 1 | 3 |

---

## 5. Solution Step Rules

Solutions are the primary teaching mechanism. They're what students see after answering. Bad solutions undermine the entire product.

**SOL1 — Solutions teach, not just state.** Every part must have `solutionSteps`. They explain reasoning, build understanding, and address why the wrong answer is wrong — not just confirm the right answer.

**SOL2 — Calculation solutions show every step:**
1. State the formula (with `"formula": true` flag)
2. Show substitution with actual values from the question
3. Show the arithmetic/calculation result
4. State the final answer with correct units
5. Note any rounding applied

Example:
```json
[
  { "text": "Use the magnification formula:" },
  { "text": "magnification = image size ÷ actual size", "formula": true },
  { "text": "magnification = 25 mm ÷ 0.05 mm", "formula": true },
  { "text": "magnification = ×500", "formula": true },
  { "text": "The magnification of the microscope is ×500." }
]
```

**SOL3 — Conceptual solutions address the misconception.** Structure:
1. State the correct answer and explain why it's correct (1–2 sentences)
2. Name the most common wrong answer and explain why it's wrong (1–2 sentences)

Example:
```json
[
  { "text": "The correct answer is the electron microscope." },
  { "text": "Ribosomes are very small (~20 nm), below the resolution limit of light microscopes (~200 nm)." },
  { "text": "A common mistake is choosing 'light microscope' — while these can magnify enough to see cells, they cannot resolve structures smaller than ~200 nm." }
]
```

**SOL4 — The `formula` flag.** Set `"formula": true` on steps containing equations, substitutions, chemical formulae, or numerical results. This tells the renderer to use monospace/mathematical formatting. Do not set it on prose explanations.

**SOL5 — Solution length.** Target 3–5 steps per part. 1-mark recall parts may have 2 steps. 3–4 mark explain parts may have 5–6 steps. Never exceed 7 steps for a single part — if it needs more, the question is probably over-scoped.

---

## 6. Diagram Specification Rules

Diagrams are specifications during content creation, not assets. The actual SVG artwork is created during platform build (Phase B). Specs must be detailed enough that an SVG artist or generator can produce the visual without ambiguity.

**DIA1 — Hotspot positions use percentage coordinates.** `{ "x": 45, "y": 30 }` means 45% from left edge, 30% from top edge. This makes specs resolution-independent.

**DIA2 — Every diagram spec includes (field names match Unified Scenario Schema v1.3):**
- `imageSrc` — Root-relative path to the SVG asset (e.g. `"./src/assets/diagrams/bio_01_plant_cell.svg"`). During content creation this is a placeholder path — the actual SVG is created in Phase B.
- `imageAlt` — Accessible alt text describing the diagram (e.g. `"Diagram of a plant cell showing five labelled structures"`)
- `title` — Short title of what the diagram shows (e.g. `"Plant cell structure"`). Not in the base schema — added for authoring clarity.
- `description` — Prose description sufficient for an artist to draw it (3–6 sentences covering visual layout, key structures, relative positions, sizes, and visual cues). Include size hints inline (e.g. "the nucleus is a large, dark-stained oval, approximately 1/4 of the cell diameter"). This field is the primary input for Phase B illustration.
- `width` — Intrinsic width hint in pixels (typically 550–600). Layout hint, not enforced.
- `aspectRatio` — Aspect ratio hint for container sizing (e.g. `"4:3"`)
- `hotspots` — Array of labellable structures, each with `id`, `x` and `y` (percentage coordinates per DIA1), and `correct` (the matching `termBank` ID)
- `termBank` — Full set of label options offered to students, each with `id` and `text`. Includes correct labels plus distractors per DIA3.

**DIA3 — Label banks include distractors.** If a diagram has N hotspots, the label bank must have N + 2 to N + 4 options. Distractors must be plausible structures from the same biological/physical/chemical system.

**DIA4 — Diagram descriptions must be unambiguous.** An SVG artist reading only the `description` and `hotspots` array should be able to produce a diagram that matches the intended layout. Include spatial relationships ("the mitochondria should appear as oval shapes scattered throughout the cytoplasm"), relative sizes ("the nucleus is the largest organelle, approximately 1/4 of the cell diameter"), and visual cues ("label arrows should point from outside the cell boundary to the target structure").

**DIA5 — Illustrator reproducibility test.** A diagram spec passes this test if an external illustrator with no subject knowledge could reproduce the diagram from the spec alone. If drawing the diagram requires biological, physical, or chemical knowledge not contained in the spec, the spec is underspecified. "Draw a plant cell" fails this test. "Draw a rectangular cell with a thick outer wall, large central vacuole filling ~60% of the cell, circular nucleus offset to one side, and small oval mitochondria scattered in the cytoplasm" passes.

---

## 7. Graph Specification Rules

Graph specs define the data for interactive SVG graph components. They must be precise enough to render without interpretation.

**GR1 — Every graph spec includes:**
- `xAxis`: `label`, `min`, `max`, `step` (gridline interval)
- `yAxis`: `label`, `min`, `max`, `step`
- `lines`: Array of line objects, each with `id`, `color`, `points` (array of `{x, y}`)
- `interactiveMode`: `"read"` (crosshair reading) or `"plot-points"` (student plots)
- `lineType`: `"straight"` (connect points with straight segments) or `"smooth"` (cardinal spline interpolation for biological rate curves)

**GR2 — Data must not require interpolation beyond visible grid resolution.** If gridlines are at intervals of 10 and the correct answer is a graph reading, the answer should fall on or within ±0.5 of a gridline intersection. Do not place correct answers between gridlines where precision is ambiguous.

**GR3 — Data must be scientifically realistic.** No impossible rates, no negative concentrations, no temperatures below absolute zero, no enzyme activity at pH 0 unless the question is specifically about extreme conditions. Academic QA will check this.

**GR4 — Axis ranges must show the full data with breathing room.** The axis maximum should be at least 10% above the highest data point. The axis minimum should be 0 unless negative values are meaningful (e.g. velocity-time graphs).

---

## 8. Cross-Subject Consistency Rules

These rules prevent drift across the three separately-authored subject content sets.

**CS1 — Skill tag definitions are universal.** `interpret-graph` means the same thing in Biology, Physics, and Chemistry. The controlled vocabulary in Section 4.2 is the single source of truth. Subject authors do not create subject-specific skill tags — they use the shared vocabulary.

**CS2 — AO level interpretation is consistent.** AO1 = recall/state/identify/label. AO2 = apply/calculate/describe/interpret. AO3 = explain why/evaluate/predict/justify. These definitions do not shift between subjects. A Biology "explain" and a Physics "explain" both require the same depth of reasoning for the same mark count.

**CS3 — Marking conventions override subject intuition.** The rules in Section 3 are the authority. If a Biology author feels that ±5% tolerance is more appropriate for a particular calculation, the answer is no — MC1 defines the tolerance. If a specific question genuinely requires different marking, the exception must be documented in the answer schema with a `"toleranceOverride"` field and a `"toleranceReason"` string explaining why.

**CS4 — Solution quality is uniform.** A 3-mark explain part in Biology requires the same solution depth as a 3-mark explain part in Physics. SOL1–SOL5 apply identically across subjects.

---

## 9. Scope Control Rules

Content creation is strictly bounded. These rules prevent scope creep that would delay production and force schema changes.

**SC1 — No new interaction types during content creation.** The set of interaction types is fixed at the start of content authoring:
- MCQ
- Numeric with unit
- Calculation (with method marks)
- Graph reading
- Diagram label
- Process sequence
- Keyword match
- Punnett grid
- Self-assessed / explain
- Equation balancer (Chemistry)
- Data table reading

**SC2 — If a scenario appears to require a new interaction type, redesign within existing types.** A "drag molecules onto a diagram" question can almost always be restructured as a diagram label or process sequence. A "draw a graph" question can be restructured as a "plot points on a graph" (which is covered by `interactiveMode: "plot-points"`).

**SC3 — New interaction types require formal approval.** Any new type requires: (a) a schema version bump, (b) a marking convention added to this document, (c) a component spec, and (d) migration of any already-authored scenarios that might be affected. This is intentionally heavyweight to discourage frivolous additions.

**SC4 — Diagram specs describe, they don't design.** Diagram specifications define what the diagram shows and where hotspots are. They do not specify SVG paths, colours, line weights, or visual design decisions. Visual design is a Phase B concern.

---

## 10. Subject-Specific Rules

These rules supplement the universal rules above for specific subjects.

### 10.1 Biology

**BIO1 — Cross-topic knowledge is allowed but must not replace required subtopics.** A respiration scenario may reference enzymes, but the core marks must test respiration content, not enzyme knowledge. Required subtopics from the coverage contract take priority.

**BIO2 — No scenario may depend on a later topic's content for core marks.** Topics are numbered in curriculum order. A Topic 5 (Circulation) scenario should not require Topic 10 (Enzyme Action) knowledge for any part worth marks. Background references are acceptable in context paragraphs only.

**BIO3 — Punnett grid questions must separate grid completion from interpretation.** The grid-filling part tests whether students can complete the cross. The ratio/probability interpretation is a separate part with its own marks. Never bundle both skills into a single mark allocation.

### 10.2 Physics

**PHY1 — Every graph-reading scenario must specify the graph type explicitly.** Distance-time, velocity-time, I-V characteristic, decay curve, force-extension, etc. The graph type determines what gradient and area-under-curve represent, which affects the solution steps.

**PHY2 — Formulae are provided, not recalled.** Consistent with Edexcel 2025–2027 formula sheet provision, questions test applying the correct formula from a provided sheet — not recalling it from memory. Solution steps should reference "from the formula sheet" where applicable.

### 10.3 Chemistry

**CHEM1 — Chemical formulae use subscript notation in question text.** Write `H₂O`, `CO₂`, `NaOH` using Unicode subscript characters. Do not use plain text `H2O` or LaTeX notation.

**CHEM2 — State symbols must be included where Edexcel requires them.** Equations should include `(s)`, `(l)`, `(g)`, `(aq)` when the question or mark scheme references states of matter.

**CHEM3 — Mole calculation scenarios must show the full method chain.** Solution steps for mole calculations follow: formula → substitution → intermediate result → unit conversion (if needed) → final answer with unit. No steps may be skipped, even if the calculation is simple.

---

## 11. Authoring Assembly Line

Every scenario follows these 7 steps in this order. Do not skip steps. Do not reorder. Complete each step fully before moving to the next.

### Step 1 — Skeleton
Create the JSON file with metadata: `id`, `title`, `icon`, `difficulty`, topic number. Set up the `parts` array with `id`, `partLabel`, `type`, and `marks` matching the coverage contract. Context is a placeholder at this stage.

### Step 2 — Context + Question Text
Write the scenario context paragraph (exam-style, 2–4 sentences). Write each part's `question` text. Context must be self-contained per Rule S7.

### Step 3 — Answer Schemas
Fill every `answerSchema` precisely per the marking conventions in Section 3. MCQ: all 4 options with `isCorrect` flags, distractors targeting specific misconceptions. Numeric: `correct`, `tolerance`, `unitOptions`, `correctUnit`. Diagram label: `hotspotIds`, label bank with distractors. Process sequence: `steps`, `correctOrder`. Keyword match: `passage`, `blanks`, `wordBank` with distractors. Punnett: `parentAlleles`, `correctCells`. Self-assessed: `markSchemePoints` (specific per MC12), `maxCheckable`. Equation balancer: valid coefficient sets per MC15.

### Step 4 — Solution Steps
Write `solutionSteps` for every part following rules SOL1–SOL5. Calculations: formula → substitution → result → units. Conceptual: correct answer → why correct → common mistake → why wrong.

### Step 5 — Tags
Add `topicTags`, `skillTags`, and `misconceptionTags` to every part following the taxonomy in Section 4. Respect minimums and maximums in Section 4.4. Use the controlled skill vocabulary exactly — do not invent synonyms.

### Step 6 — Visual Specs
Add `diagramSpec`, `graphSpec`, or `dataTable` where required. Follow rules DIA1–DIA5 for diagrams, GR1–GR4 for graphs.

### Step 7 — Validate
Self-check against this mechanical QA checklist:

- [ ] JSON parses without errors
- [ ] Conforms to Unified Scenario Schema v1.3
- [ ] Every part has: question text, complete answerSchema, solutionSteps, all three tag types
- [ ] Mark total matches coverage contract target (±1 mark tolerance)
- [ ] AO spread matches coverage contract
- [ ] All required subtopics from coverage contract appear in at least one part
- [ ] All required misconceptions from coverage contract are tagged
- [ ] Diagram/graph specs present where coverage contract requires them
- [ ] Diagram label banks have N+2 to N+4 options (correct + distractors)
- [ ] MCQ options: exactly 4, exactly 1 correct, each distractor targets a named misconception
- [ ] Keyword match word banks include 2–4 distractors
- [ ] All `id` fields are unique within the scenario
- [ ] No placeholder text remains
- [ ] Solution steps follow SOL1–SOL5 (calculations show every step; conceptual solutions address misconceptions)
- [ ] Skill tags are from the controlled vocabulary (Section 4.2) — no invented tags

Update `_manifest.json` with `"status": "complete"` and final mark/part counts.

---

## 12. QA Process

### Layer 1 — Mechanical QA (per scenario, immediately after authoring)

Runs the Step 7 checklist above. Binary pass/fail. If any check fails, fix before moving to the next scenario.

### Layer 2 — Academic QA (per sprint batch, with GPT adversarial review)

After completing a batch of scenarios (typically one curriculum group), run academic QA:

- **Scientific accuracy** — Are facts, equations, and values correct?
- **Exam authenticity** — Does this read like a real Edexcel IGCSE question?
- **Mark scheme defensibility** — Would a real examiner accept this mark allocation?
- **Misconception validity** — Are tagged misconceptions genuinely common?
- **Solution quality** — Do solutions teach understanding, not just confirm answers?
- **Distractor quality** — Are wrong MCQ options and label-bank distractors plausible?
- **Difficulty calibration** — Is the DIF1–DIF5 progression appropriate?
- **Cross-topic leakage** — Does any part inadvertently require knowledge from another topic?
- **Subject-level AO balance** — After completing all scenarios for a subject, verify: total AO1/AO2/AO3 marks fall within ±10% of the planned distribution. No subject may exceed 40% AO3 overall. Individual scenarios may vary, but the aggregate must be balanced. This prevents systemic skew where one subject becomes calculation-dominant (AO2-heavy) while another becomes explanation-dominant (AO3-heavy).

Flag issues at the scenario level in `_manifest.json` by changing status to `"qa-flagged"` with a `"qaNote"` field describing the issue.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Feb 2026 | Initial version. Rules from roadmap v1.1–v1.2 consolidated into standalone document. |
| 1.1 | Feb 2026 | GPT QA round 3: Added TAG1–TAG2 (misconception master list control). Tightened MC15 to explicitly require lowest whole-number coefficients only. Added DIA5 (illustrator reproducibility test). Added subject-level AO balance check to academic QA. |
| 1.2 | Feb 2026 | Schema alignment: DIA2 field names updated to match Unified Scenario Schema v1.3 (`structures` → `hotspots`, `labelBank` → `termBank`, added `imageSrc`, `imageAlt`, `width`, `aspectRatio`). Added `title` as authoring-only field. DIA4 reference updated. Resolves document misalignment caught during bio_01 gold-standard QA. |

---

**End of Science Content Authoring Rules v1.2**

This document is shared across all three science content projects. When handing a content sprint to Claude Code, include this document alongside the Unified Scenario Schema and the subject-specific content brief.
