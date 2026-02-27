45.19 KB •1,174 lines
•
Formatting may be inconsistent from source

# Unified Scenario Schema â€” v1.3

## Purpose

This document supersedes the scenario data model in the platform PRD (Section 7) and the Biology Claude Code Brief (Section 7). It resolves the diagram/graph referencing inconsistency, standardises the marker contract, defines exam-mode scoring treatment for teacher-marked items, and incorporates implementation lessons learned from both the Physics and Biology app builds.

All scenario JSON files â€” Physics, Biology, Chemistry, and any future subject â€” must conform to this schema.

### Changes from v1.2

- **MCQ options moved to part level.** The app's MCQ renderer reads `part.options`, not `answerSchema.options`. The `answerSchema` for MCQ now contains only `{ type: "mcq", correct: "opt_b" }`. This matches the actual `src/lib/marking.js` implementation.
- **Graph `data` â†’ `lines` format.** The Physics `Graph.js` renderer iterates `spec.lines[].points`, not `spec.data`. Each line has `id`, `color`, and `points`. The `lineType` field is removed (the renderer determines rendering from the data shape).
- **Diagram `imageSrc` must be root-relative.** Paths must start with `./src/assets/diagrams/` because the app is served from `index.html` at the project root. Bare filenames or partial paths will 404.
- **Restored `marks` in `answerSchema` for Biology types.** v1.2 removed `answerSchema.marks` to make `part.marks` the single source of truth. However, the Biology marking adapters (`keyword_match`, `diagram_label`, `self_assessed`) read `answerSchema.marks` directly. Until the marking engine is refactored to pass context, `answerSchema.marks` must be present and must equal `part.marks`. This is intentionally redundant â€” a dev-time validator checks they don't drift (Section 10.6).
- **Added `interactiveMode` to GraphSpec.** The Physics graph component distinguishes `"read"` (crosshair reading) from `"plot-points"` (student places points). This field was missing from the schema.
- **Added scenario registration requirement.** New scenarios must be added to the `ids` array in `src/app.js` `loadScenarios()` to be loaded by the app.
- **Added placeholder SVG creation guidance** for new diagram assets.
- **Added quick-fix Python script** (Section 11) to convert "natural" authored JSON to app-compatible format.
- **Added MCQ and GraphSpec validators** (Sections 10.3, 10.4).

### Changes from v1.1

- Fixed ProcessSequence breakdown semantics.
- Made `breakdown` optional in `MarkResult`.
- Added validation rules (Section 10).
- Improved seeded shuffle with `attemptId`.
- Renamed `teacherMarkedInExam` â†’ `isTeacherMarkedInExam`.
- Added graph y-axis clamping rule.
- Added unanswered vs incorrect distinction in MarkResult.

---

## 1. Scenario Object

```jsonc
{
  // â€”â€”â€” Identity â€”â€”â€”
  "id": "bio_07",                          // Unique across all subjects. Convention: {subject}_{nn}
  "title": "Lungs & Gas Exchange",
  "icon": "ðŸ«",                            // Emoji or icon reference
  "subject": "biology",                    // Must match the subject module id

  // â€”â€”â€” Context â€”â€”â€”
  "context": "A student is studying the structure of the lungs and how they are adapted for gas exchange...",
  "difficulty": "foundation-higher",       // "foundation" | "higher" | "foundation-higher"

  // â€”â€”â€” Shared Resources (keyed maps, not single objects) â€”â€”â€”
  "diagrams": {                            // Map<string, DiagramSpec> â€” null or omit if none
    "lungs": { /* DiagramSpec */ },
    "alveolus": { /* DiagramSpec */ }
  },
  "graphs": {                              // Map<string, GraphSpec> â€” null or omit if none
    "enzymeCurve": { /* GraphSpec */ }
  },
  "dataTables": {                          // Map<string, DataTableSpec> â€” null or omit if none
    "pondweedResults": { /* DataTableSpec */ }
  },

  // â€”â€”â€” Question Parts â€”â€”â€”
  "parts": [ /* Part[] â€” see Section 3 */ ]
}
```

### Why keyed maps instead of single objects

The previous schema used `diagramSpec` (singular) at scenario level. This breaks when a scenario needs more than one diagram â€” Scenario 7 (Lungs & Gas Exchange) requires both a lung overview and an alveolus close-up.

Keyed maps solve this cleanly. Each resource gets a stable string key. Parts reference resources by key. The core renderer never needs to know what the resources contain â€” it passes them to the subject component by reference.

### Scenario Registration

After adding a new scenario JSON file to `src/data/scenarios/`, you must also add its ID to the `ids` array in `src/app.js` inside `loadScenarios()`. The app does not auto-discover scenario files.

---

## 2. Shared Resource Specs

### 2.1 DiagramSpec

```jsonc
{
  "imageSrc": "./src/assets/diagrams/lungs.svg",   // MUST be root-relative from project root
  "imageAlt": "Diagram of the human respiratory system showing trachea, bronchi, and alveoli",
  "width": 600,                            // Intrinsic width hint (px) â€” layout, not enforced
  "aspectRatio": "4:3",                    // Aspect ratio hint for container sizing

  "hotspots": [
    {
      "id": "label_a",
      "x": 50,                             // % of image width (0â€“100)
      "y": 15,                             // % of image height (0â€“100)
      "correct": "trachea"                 // Term ID from termBank
    },
    { "id": "label_b", "x": 35, "y": 40, "correct": "bronchi" },
    { "id": "label_c", "x": 60, "y": 65, "correct": "alveoli" }
  ],

  "termBank": [
    { "id": "trachea", "text": "Trachea" },
    { "id": "bronchi", "text": "Bronchi" },
    { "id": "alveoli", "text": "Alveoli" },
    { "id": "diaphragm", "text": "Diaphragm" },
    { "id": "bronchioles", "text": "Bronchioles" }
  ]
}
```

**Rules:**
- **`imageSrc` must be root-relative**, starting with `./src/assets/diagrams/`. The app is served from `index.html` at the project root. Bare filenames (`"lungs.svg"`) or partial paths (`"assets/lungs.svg"`) will 404.
- Hotspot coordinates are always percentages (0â€“100), never pixels.
- `termBank` may contain distractors (more terms than hotspots).
- `correct` values must be valid `termBank` IDs.
- A single diagram can be referenced by multiple parts. Each part specifies which `hotspotIds` subset it uses.

**Creating new diagram SVGs:**
- Use existing SVGs in `src/assets/diagrams/` as reference.
- Target 550â€“600px wide, flat-colour line art.
- Place letter markers (A, B, Câ€¦) at hotspot positions using `#007AFF` blue circles.
- Do NOT bake label text into the SVG â€” the interactive component adds labels.

### 2.2 GraphSpec

```jsonc
{
  "xAxis": {
    "label": "Temperature (Â°C)",
    "min": 0,
    "max": 80,
    "step": 10
  },
  "yAxis": {
    "label": "Rate of reaction (cmÂ³/min)",
    "min": 0,
    "max": 30,
    "step": 5
  },
  "lines": [                               // Array of line objects â€” NOT a flat "data" array
    {
      "id": "enzymeCurve",                 // Unique line ID (use the graph key for single-line graphs)
      "color": "#007AFF",                  // Line colour (use Apple system blue as default)
      "points": [                          // Array of {x, y} data points
        { "x": 10, "y": 5 },
        { "x": 20, "y": 12 },
        { "x": 30, "y": 22 },
        { "x": 37, "y": 28 },
        { "x": 40, "y": 25 },
        { "x": 50, "y": 10 },
        { "x": 60, "y": 2 },
        { "x": 70, "y": 0 }
      ]
    }
  ],
  "interactiveMode": "read"                // "read" (crosshair reading) | "plot-points" (student places points)
}
```

**Rules:**
- **Use `lines` array, NOT a flat `data` array.** The Physics `Graph.js` renderer iterates `spec.lines` and accesses `line.points`. A top-level `data` array will be silently ignored.
- **No `lineType` field.** The renderer determines smooth vs straight from the component context. Biology curves render smooth (Catmull-Rom spline, tension 0.5) by default.
- **Y-axis clamping:** When rendering smooth curves, clamp interpolated y-values to the axis range (`yAxis.min` to `yAxis.max`). Prevents visual overshoot at peaks/troughs.
- **Negative y-axis:** The renderer supports negative values on both axes. Physics scenario_04 uses negative velocity.
- **`interactiveMode`:** `"read"` enables crosshair + value readout. `"plot-points"` lets the student place data points on the graph. Uses bidirectional `toPixel()` / `toData()` conversion with snapping.
- **Graph padding** is fixed at `{ top: 24, right: 24, bottom: 56, left: 64 }` in the renderer. Don't encode padding in the data.
- Multiple lines are supported. Each gets its own `id` and `color`.

### 2.3 DataTableSpec

```jsonc
{
  "caption": "Pondweed bubble count results",
  "headers": ["Light intensity (arbitrary units)", "Bubbles per minute"],
  "rows": [
    [1, 5],
    [2, 10],
    [3, 18],
    [4, 23],
    [5, 26],
    [6, 27],
    [7, 27]
  ]
}
```

---

## 3. Part Object

Each part represents one question sub-part (a, b, câ€¦). Parts reference shared resources by key.

```jsonc
{
  // â€”â€”â€” Identity â€”â€”â€”
  "id": "bio_07_a",                        // Unique. Convention: {scenario_id}_{partLabel}
  "partLabel": "a",                        // Display label: "a", "b", "c"...

  // â€”â€”â€” Question â€”â€”â€”
  "type": "diagram_label",                 // Determines which component renders the interaction
  "marks": 3,                              // Total marks available â€” SINGLE SOURCE OF TRUTH
  "question": "Label structures A, B, and C on the lung diagram.",

  // â€”â€”â€” MCQ Options (MCQ type only) â€”â€”â€”
  // For MCQ parts, options live HERE at part level, not inside answerSchema.
  // "options": [ { "id": "opt_a", "text": "..." }, ... ]

  // â€”â€”â€” Resource References â€”â€”â€”
  "diagramRef": "lungs",                   // Key into scenario.diagrams â€” null if not applicable
  "graphRef": null,                        // Key into scenario.graphs â€” null if not applicable
  "dataTableRef": null,                    // Key into scenario.dataTables â€” null if not applicable

  // â€”â€”â€” Answer Schema â€”â€”â€”
  "answerSchema": {
    "type": "diagram_label",               // Must match the marking adapter key
    "hotspotIds": ["label_a", "label_b", "label_c"],
    "marks": 3                             // Must equal part.marks â€” see Section 3.1
  },

  // â€”â€”â€” Method Marks (optional) â€”â€”â€”
  "methodMarks": null,                     // Array of { id, description, marks } or null

  // â€”â€”â€” Feedback â€”â€”â€”
  "solutionSteps": [
    { "text": "A = Trachea â€” the windpipe that carries air from the mouth/nose to the lungs." },
    { "text": "B = Bronchi â€” the two tubes that branch from the trachea into each lung." },
    { "text": "C = Alveoli â€” tiny air sacs where gas exchange occurs." }
  ],

  // â€”â€”â€” Tagging â€”â€”â€”
  "topicTags": ["lung-structure"],
  "skillTags": ["identify-structures"],
  "misconceptionTags": ["confuses-bronchi-bronchioles"],

  // â€”â€”â€” Exam-Mode Flags â€”â€”â€”
  "isTeacherMarkedInExam": false           // True for self_assessed / extended response parts
}
```

### 3.1 The `marks` field â€” why it appears in two places

`part.marks` is the single source of truth for the UI (progress display, results dashboard, total calculation). However, the Biology marking adapters currently read `answerSchema.marks` directly rather than receiving marks through a context object.

Until the marking engine is refactored to consistently pass `ctx.part.marks` to all adapters, **`answerSchema.marks` must be present for Biology-specific types** and must equal `part.marks`. A dev-time validator (Section 10.6) catches any drift between the two values.

This applies to: `diagram_label`, `keyword_match`, `process_sequence`, `punnett_grid`, `self_assessed`.

Core types (`mcq`, `numeric_with_unit`, `calculation`) do not need `answerSchema.marks` â€” the core marking engine already reads `part.marks`.

### 3.2 MCQ options â€” why they live at part level

The app's MCQ renderer reads `part.options` to display choices. The `answerSchema` for MCQ contains only the correct answer ID. This separation means the renderer doesn't need to know about answer schemas, and the marker doesn't need to know about display text.

**MCQ part structure:**

```jsonc
{
  "id": "bio_07_c",
  "partLabel": "c",
  "type": "mcq",
  "marks": 1,
  "question": "Which process moves oxygen from the alveoli into the blood?",
  "options": [                             // OPTIONS LIVE HERE, at part level
    { "id": "opt_a", "text": "Osmosis" },
    { "id": "opt_b", "text": "Active transport" },
    { "id": "opt_c", "text": "Diffusion" },
    { "id": "opt_d", "text": "Respiration" }
  ],
  "answerSchema": {
    "type": "mcq",
    "correct": "opt_c"                     // Just the correct option ID
  }
}
```

**Common mistake:** Putting `options` inside `answerSchema` with `isCorrect: true/false` flags on each option. This will silently fail â€” the MCQ renderer won't find any options to display.

### Resource Reference Rules

| Part type | Expects `diagramRef` | Expects `graphRef` | Expects `dataTableRef` |
|-----------|---------------------|--------------------|------------------------|
| `diagram_label` | âœ“ required | â€” | â€” |
| `graph_reading` | â€” | âœ“ required | optional |
| `process_sequence` | â€” | â€” | â€” |
| `keyword_match` | â€” | â€” | â€” |
| `punnett_grid` | â€” | â€” | â€” |
| `self_assessed` | â€” | â€” | â€” |
| `mcq` | â€” | â€” | â€” |
| `numeric_with_unit` | â€” | â€” | optional |
| `calculation` | â€” | â€” | optional |

**The core Test Runner resolves references before passing props to components:**

```javascript
const diagram = part.diagramRef ? scenario.diagrams[part.diagramRef] : null;
const graph = part.graphRef ? scenario.graphs[part.graphRef] : null;
const dataTable = part.dataTableRef ? scenario.dataTables[part.dataTableRef] : null;

component.render({ part, diagram, graph, dataTable, onAnswer, answer, disabled, showSolution });
```

Components never navigate up to the scenario object. They receive everything they need as flat props.

---

## 4. Answer Schema â€” Per Type

### 4.1 `diagram_label`

```jsonc
{
  "type": "diagram_label",
  "hotspotIds": ["label_a", "label_b", "label_c"],
  "marks": 3
}
```

**Student answer:** `{ "label_a": "trachea", "label_b": "bronchi", "label_c": "alveoli" }` â€” unanswered hotspots are `null`.

### 4.2 `process_sequence`

```jsonc
{
  "type": "process_sequence",
  "steps": [
    { "id": "step_1", "text": "Receptor detects stimulus" },
    { "id": "step_2", "text": "Sensory neuron carries impulse to spinal cord" },
    { "id": "step_3", "text": "Impulse passes through relay neuron" },
    { "id": "step_4", "text": "Motor neuron carries impulse to effector" },
    { "id": "step_5", "text": "Muscle contracts to move hand" }
  ],
  "correctOrder": ["step_1", "step_2", "step_3", "step_4", "step_5"],
  "marks": 2
}
```

**Student answer:** `{ "order": ["step_1", "step_3", "step_2", "step_4", "step_5"], "initialOrder": [...] }` â€” `initialOrder` stores the seeded shuffle (Section 6).

### 4.3 `keyword_match`

```jsonc
{
  "type": "keyword_match",
  "passage": "glucose + {blank_1} â†’ {blank_2} + water",
  "blanks": [
    { "id": "blank_1", "correct": "oxygen" },
    { "id": "blank_2", "correct": "carbon_dioxide" }
  ],
  "wordBank": [
    { "id": "oxygen", "text": "oxygen" },
    { "id": "carbon_dioxide", "text": "carbon dioxide" },
    { "id": "lactic_acid", "text": "lactic acid" },
    { "id": "ethanol", "text": "ethanol" }
  ],
  "marks": 2
}
```

**Student answer:** `{ "blank_1": "oxygen", "blank_2": null }` â€” unanswered blanks are `null`.

### 4.4 `punnett_grid`

```jsonc
{
  "type": "punnett_grid",
  "parentAlleles": { "parent1": ["F", "f"], "parent2": ["F", "f"] },
  "gridSize": 2,
  "correctCells": { "cell_0_0": "FF", "cell_0_1": "Ff", "cell_1_0": "Ff", "cell_1_1": "ff" },
  "marks": 4
}
```

**v1 constraints:** Single gene, two alleles, genotype length exactly 2, grid size 2Ã—2 only.

**Student answer:** `{ "cell_0_0": "FF", "cell_0_1": "Ff", "cell_1_0": "fF", "cell_1_1": "" }` â€” unanswered cells are empty strings.

### 4.5 `self_assessed`

```jsonc
{
  "type": "self_assessed",
  "modelAnswer": "The alveoli are adapted for efficient gas exchange...",
  "markSchemePoints": [
    { "id": "p1", "text": "Large surface area" },
    { "id": "p2", "text": "Thin walls / one cell thick / short diffusion distance" },
    { "id": "p3", "text": "Good blood supply / rich capillary network" },
    { "id": "p4", "text": "Moist lining to dissolve gases" },
    { "id": "p5", "text": "Steep concentration gradient maintained" }
  ],
  "maxCheckable": 4,
  "marks": 4
}
```

Part must also set `"isTeacherMarkedInExam": true`.

**Student answer:** `{ "text": "student's response...", "checkedPoints": ["p1", "p2", "p3"] }`

### 4.6 `mcq`

```jsonc
{
  "type": "mcq",
  "correct": "opt_c"
}
```

**No `options` array, no `isCorrect` flags, no `marks` field.** Options live at `part.options` (Section 3.2). Core marking engine reads `part.marks`.

### 4.7 Core types (unchanged)

`numeric_with_unit`, `graph_reading`, `calculation` â€” schemas remain as defined in the Physics prototype. Graph-reading parts use `graphRef` to link to `scenario.graphs`.

---

## 5. Marker Contract

All marking adapters â€” core and subject-specific â€” must conform to this contract.

### 5.1 Function Signature

```typescript
type MarkerContext = {
  mode: 'practice' | 'exam';
  part: Part;
  scenario: Scenario;
};

type BreakdownItem = {
  studentValue: any;
  correctValue: any;
  isCorrect: boolean;
  wasAttempted: boolean;         // False if student left this item blank/unanswered
};

type MarkResult = {
  marksAwarded: number;
  maxMarks: number;              // Always read from ctx.part.marks
  isCorrect: boolean;            // marksAwarded === maxMarks
  isPartiallyCorrect: boolean;   // 0 < marksAwarded < maxMarks
  feedback: string;              // Human-readable summary
  breakdown?: Record<string, BreakdownItem>;  // Optional for simple types
  teacherMarked: boolean;        // True if not auto-scored
  methodMarksAwarded?: string[]; // IDs of method marks earned (calculation types)
};

function mark(studentAnswer: any, answerSchema: AnswerSchema, ctx: MarkerContext): MarkResult;
```

### 5.2 Implementation note

The Biology marking adapters in the current codebase read `answerSchema.marks` rather than `ctx.part.marks`. Both values must be present and equal until the marking engine is refactored. See Section 3.1.

### 5.3 Why `breakdown` is optional

Simple types like MCQ have a single answer item. Multi-item types (diagram_label, keyword_match, punnett_grid, process_sequence) should always provide a populated breakdown for the review UI.

### 5.4 Why `wasAttempted` in BreakdownItem

The review UI distinguishes three states: correct (green), incorrect (red), and unanswered (grey). Without `wasAttempted`, the UI can't tell "student chose wrong" from "student didn't answer."

### 5.5 Adapter Implementations

#### `markDiagramLabel`

```javascript
export function markDiagramLabel(studentAnswer, answerSchema, ctx) {
  const diagram = ctx.scenario.diagrams[ctx.part.diagramRef];
  const activeHotspots = diagram.hotspots.filter(h =>
    answerSchema.hotspotIds.includes(h.id)
  );
  const maxMarks = ctx.part.marks;
  let correct = 0;
  const breakdown = {};

  for (const hotspot of activeHotspots) {
    const studentChoice = studentAnswer?.[hotspot.id] ?? null;
    const wasAttempted = studentChoice !== null;
    const isCorrect = wasAttempted && studentChoice === hotspot.correct;
    if (isCorrect) correct++;
    breakdown[hotspot.id] = { studentValue: studentChoice, correctValue: hotspot.correct, isCorrect, wasAttempted };
  }

  return {
    marksAwarded: correct, maxMarks,
    isCorrect: correct === maxMarks,
    isPartiallyCorrect: correct > 0 && correct < maxMarks,
    feedback: correct === maxMarks ? 'All labels correct.' : `${correct} of ${maxMarks} labels correct.`,
    breakdown, teacherMarked: false
  };
}
```

#### `markProcessSequence`

```javascript
export function markProcessSequence(studentAnswer, answerSchema, ctx) {
  const { correctOrder } = answerSchema;
  const maxMarks = ctx.part.marks;
  const studentOrder = studentAnswer?.order || [];
  const totalPairs = correctOrder.length - 1;
  const breakdown = {};
  let correctPairs = 0;

  for (let i = 0; i < totalPairs; i++) {
    const expectedA = correctOrder[i];
    const expectedB = correctOrder[i + 1];
    const idxA = studentOrder.indexOf(expectedA);
    const idxB = studentOrder.indexOf(expectedB);
    const isCorrect = idxA !== -1 && idxB !== -1 && idxB === idxA + 1;
    if (isCorrect) correctPairs++;

    const studentA = idxA !== -1 ? expectedA : '?';
    const studentNext = idxA !== -1 && idxA + 1 < studentOrder.length ? studentOrder[idxA + 1] : '?';

    breakdown[`pair_${i}`] = {
      studentValue: `${studentA} â†’ ${studentNext}`,
      correctValue: `${expectedA} â†’ ${expectedB}`,
      isCorrect, wasAttempted: studentOrder.length > 0
    };
  }

  const fullyCorrect = JSON.stringify(studentOrder) === JSON.stringify(correctOrder);
  const marksAwarded = fullyCorrect ? maxMarks
    : totalPairs === 0 ? 0
    : Math.floor((correctPairs / totalPairs) * maxMarks);

  return {
    marksAwarded, maxMarks, isCorrect: fullyCorrect,
    isPartiallyCorrect: marksAwarded > 0 && !fullyCorrect,
    feedback: fullyCorrect ? 'Correct order!' : `${correctPairs} of ${totalPairs} adjacent pairs correct.`,
    breakdown, teacherMarked: false
  };
}
```

#### `markKeywordMatch`

```javascript
export function markKeywordMatch(studentAnswer, answerSchema, ctx) {
  const { blanks } = answerSchema;
  const maxMarks = ctx.part.marks;
  let correct = 0;
  const breakdown = {};

  for (const blank of blanks) {
    const studentChoice = studentAnswer?.[blank.id] ?? null;
    const wasAttempted = studentChoice !== null;
    const isCorrect = wasAttempted && studentChoice === blank.correct;
    if (isCorrect) correct++;
    breakdown[blank.id] = { studentValue: studentChoice, correctValue: blank.correct, isCorrect, wasAttempted };
  }

  return {
    marksAwarded: correct, maxMarks,
    isCorrect: correct === maxMarks,
    isPartiallyCorrect: correct > 0 && correct < maxMarks,
    feedback: correct === maxMarks ? 'All terms correctly placed.' : `${correct} of ${maxMarks} terms correct.`,
    breakdown, teacherMarked: false
  };
}
```

#### `markPunnettGrid`

```javascript
export function markPunnettGrid(studentAnswer, answerSchema, ctx) {
  const { correctCells } = answerSchema;
  const maxMarks = ctx.part.marks;
  let correct = 0;
  const breakdown = {};

  const normalise = (g) => g.trim().split('').sort((a, b) =>
    a.toLowerCase().localeCompare(b.toLowerCase())).join('');

  for (const [cellId, correctGenotype] of Object.entries(correctCells)) {
    const studentGenotype = studentAnswer?.[cellId] ?? '';
    const wasAttempted = studentGenotype.trim().length > 0;
    const isCorrect = wasAttempted && studentGenotype.trim().length === 2
      && normalise(studentGenotype) === normalise(correctGenotype);
    if (isCorrect) correct++;
    breakdown[cellId] = { studentValue: studentGenotype || null, correctValue: correctGenotype, isCorrect, wasAttempted };
  }

  return {
    marksAwarded: correct, maxMarks,
    isCorrect: correct === maxMarks,
    isPartiallyCorrect: correct > 0 && correct < maxMarks,
    feedback: correct === maxMarks ? 'All cells correct.' : `${correct} of ${maxMarks} cells correct.`,
    breakdown, teacherMarked: false
  };
}
```

#### `markSelfAssessed`

```javascript
export function markSelfAssessed(studentAnswer, answerSchema, ctx) {
  const { markSchemePoints, maxCheckable } = answerSchema;
  const maxMarks = ctx.part.marks;
  const checkedPoints = studentAnswer?.checkedPoints || [];
  const text = studentAnswer?.text || '';
  const breakdown = {};

  for (const point of markSchemePoints) {
    const checked = checkedPoints.includes(point.id);
    breakdown[point.id] = { studentValue: checked, correctValue: point.text, isCorrect: checked, wasAttempted: text.trim().length > 0 };
  }

  if (ctx.mode === 'exam') {
    return { marksAwarded: 0, maxMarks, isCorrect: false, isPartiallyCorrect: false,
      feedback: 'This question requires teacher marking.', breakdown, teacherMarked: true };
  }

  const selfMarks = Math.min(checkedPoints.length, maxCheckable ?? maxMarks);
  return {
    marksAwarded: selfMarks, maxMarks,
    isCorrect: selfMarks === maxMarks,
    isPartiallyCorrect: selfMarks > 0 && selfMarks < maxMarks,
    feedback: text.trim() ? `Self-assessed: ${selfMarks} of ${maxMarks} marks.` : 'No answer provided.',
    breakdown, teacherMarked: false
  };
}
```

---

## 6. Seeded Shuffle for ProcessSequence

### Rules

1. On first render (no saved answer), generate a seeded shuffle using `seed = scenarioId + partId + attemptId`.
2. `attemptId` is a random string generated once when the test starts and stored in session state (localStorage). More stable than `sessionTimestamp` â€” survives session resumes.
3. Store `initialOrder` in the student answer immediately via `onAnswer({ order: shuffledOrder, initialOrder: shuffledOrder })`.
4. On subsequent renders (saved answer exists), use `answer.initialOrder` â€” never re-shuffle.
5. In review/solution mode, display the correct order from `answerSchema.correctOrder`.

### Implementation

```javascript
function seededShuffle(array, seed) {
  let h = seed;
  const random = () => {
    h = (h + 0x6D2B79F5) | 0;
    let t = Math.imul(h ^ (h >>> 15), 1 | h);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };

  if (typeof seed === 'string') {
    h = 0;
    for (let i = 0; i < seed.length; i++) {
      h = ((h << 5) - h + seed.charCodeAt(i)) | 0;
    }
  }

  const shuffled = [...array];
  for (let i = shuffled.length - 1; i > 0; i--) {
    const j = Math.floor(random() * (i + 1));
    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
  }
  return shuffled;
}

function generateAttemptId() {
  return Date.now().toString(36) + Math.random().toString(36).slice(2, 8);
}
```

The `attemptId` lives in the session state object in localStorage (alongside answers, timer, flags). It is not part of the MarkerContext or scenario schema.

---

## 7. Exam-Mode Scoring

### The Problem

If a test has 96 marks and 20 are from `self_assessed` parts (scored as 0 in exam mode), the percentage is computed against 96 â€” making the score look artificially low.

### The Solution

```javascript
const allParts = scenarios.flatMap(s => s.parts);
const autoMax = allParts.filter(p => !p.isTeacherMarkedInExam).reduce((sum, p) => sum + p.marks, 0);
const teacherMax = allParts.filter(p => p.isTeacherMarkedInExam).reduce((sum, p) => sum + p.marks, 0);
```

| Label | Value | Notes |
|-------|-------|-------|
| Auto-marked score | `autoScore / autoMax` | Primary score with percentage and grade |
| Teacher-marked questions | `teacherMax` marks | "X marks require teacher review" |
| Total marks available | `autoMax + teacherMax` | Context |

Grade boundaries apply to `autoScore / autoMax` only, with note: "Grade is provisional â€” {teacherMax} marks pending teacher review."

In **practice mode**, self-assessed marks are included in the total as normal.

---

## 8. Concrete Example â€” Scenario 7 (Lungs & Gas Exchange)

Demonstrates: multiple diagrams, MCQ options at part level, root-relative image paths, `lines` graph format, and teacher-marked flag.

```json
{
  "id": "bio_07",
  "title": "Lungs & Gas Exchange",
  "icon": "ðŸ«",
  "subject": "biology",
  "context": "A student is studying the structure of the lungs and how they are adapted for gas exchange. They examine a diagram of the respiratory system and a close-up of an alveolus.",
  "difficulty": "foundation-higher",

  "diagrams": {
    "lungs": {
      "imageSrc": "./src/assets/diagrams/lungs.svg",
      "imageAlt": "Diagram of the human respiratory system showing trachea, bronchi, bronchioles, and diaphragm",
      "width": 500,
      "aspectRatio": "3:4",
      "hotspots": [
        { "id": "label_a", "x": 50, "y": 12, "correct": "trachea" },
        { "id": "label_b", "x": 35, "y": 35, "correct": "bronchi" },
        { "id": "label_c", "x": 62, "y": 60, "correct": "alveoli" }
      ],
      "termBank": [
        { "id": "trachea", "text": "Trachea" },
        { "id": "bronchi", "text": "Bronchi" },
        { "id": "alveoli", "text": "Alveoli" },
        { "id": "diaphragm", "text": "Diaphragm" },
        { "id": "bronchioles", "text": "Bronchioles" },
        { "id": "pleural_membrane", "text": "Pleural membrane" }
      ]
    },
    "alveolus": {
      "imageSrc": "./src/assets/diagrams/alveolus.svg",
      "imageAlt": "Close-up diagram of an alveolus showing capillary, red blood cells, and diffusion arrows",
      "width": 400,
      "aspectRatio": "1:1",
      "hotspots": [
        { "id": "arrow_o2", "x": 45, "y": 55, "correct": "oxygen_into_blood" },
        { "id": "arrow_co2", "x": 55, "y": 45, "correct": "co2_into_alveolus" }
      ],
      "termBank": [
        { "id": "oxygen_into_blood", "text": "Oxygen diffuses into the blood" },
        { "id": "co2_into_alveolus", "text": "Carbon dioxide diffuses into the alveolus" },
        { "id": "oxygen_into_alveolus", "text": "Oxygen diffuses into the alveolus" },
        { "id": "co2_into_blood", "text": "Carbon dioxide diffuses into the blood" }
      ]
    }
  },
  "graphs": null,
  "dataTables": null,

  "parts": [
    {
      "id": "bio_07_a",
      "partLabel": "a",
      "type": "diagram_label",
      "marks": 3,
      "question": "Label structures A, B, and C on the lung diagram.",
      "diagramRef": "lungs",
      "graphRef": null,
      "dataTableRef": null,
      "answerSchema": {
        "type": "diagram_label",
        "hotspotIds": ["label_a", "label_b", "label_c"],
        "marks": 3
      },
      "methodMarks": null,
      "solutionSteps": [
        { "text": "A = Trachea â€” the windpipe carrying air from mouth/nose to lungs." },
        { "text": "B = Bronchi â€” the two main airways branching from the trachea." },
        { "text": "C = Alveoli â€” tiny air sacs where gas exchange takes place." }
      ],
      "topicTags": ["lung-structure"],
      "skillTags": ["identify-structures"],
      "misconceptionTags": ["confuses-bronchi-bronchioles"],
      "isTeacherMarkedInExam": false
    },
    {
      "id": "bio_07_b",
      "partLabel": "b",
      "type": "diagram_label",
      "marks": 2,
      "question": "On the alveolus diagram, label the direction of oxygen and carbon dioxide diffusion.",
      "diagramRef": "alveolus",
      "graphRef": null,
      "dataTableRef": null,
      "answerSchema": {
        "type": "diagram_label",
        "hotspotIds": ["arrow_o2", "arrow_co2"],
        "marks": 2
      },
      "methodMarks": null,
      "solutionSteps": [
        { "text": "Oxygen diffuses from the alveolus (high conc.) into the blood (low conc.)." },
        { "text": "Carbon dioxide diffuses from the blood (high conc.) into the alveolus (low conc.)." }
      ],
      "topicTags": ["alveoli"],
      "skillTags": ["identify-diffusion-direction"],
      "misconceptionTags": ["reverses-gas-directions"],
      "isTeacherMarkedInExam": false
    },
    {
      "id": "bio_07_c",
      "partLabel": "c",
      "type": "mcq",
      "marks": 1,
      "question": "Which process moves oxygen from the alveoli into the blood?",
      "options": [
        { "id": "opt_a", "text": "Osmosis" },
        { "id": "opt_b", "text": "Active transport" },
        { "id": "opt_c", "text": "Diffusion" },
        { "id": "opt_d", "text": "Respiration" }
      ],
      "diagramRef": null,
      "graphRef": null,
      "dataTableRef": null,
      "answerSchema": {
        "type": "mcq",
        "correct": "opt_c"
      },
      "methodMarks": null,
      "solutionSteps": [
        { "text": "Oxygen moves by diffusion â€” down its concentration gradient, high to low." },
        { "text": "This is passive and does not require energy." }
      ],
      "topicTags": ["alveoli"],
      "skillTags": ["recall-transport-processes"],
      "misconceptionTags": ["confuses-diffusion-active-transport"],
      "isTeacherMarkedInExam": false
    },
    {
      "id": "bio_07_d",
      "partLabel": "d",
      "type": "self_assessed",
      "marks": 4,
      "question": "Explain how the alveoli are adapted for efficient gas exchange. [4 marks]",
      "diagramRef": null,
      "graphRef": null,
      "dataTableRef": null,
      "answerSchema": {
        "type": "self_assessed",
        "modelAnswer": "The alveoli have a very large surface area for diffusion. Their walls are very thin (one cell thick), giving a short diffusion distance. A rich capillary network maintains a good blood supply and steep concentration gradient. The moist lining allows gases to dissolve before diffusing.",
        "markSchemePoints": [
          { "id": "p1", "text": "Large surface area" },
          { "id": "p2", "text": "Thin walls / one cell thick / short diffusion distance" },
          { "id": "p3", "text": "Good blood supply / rich capillary network" },
          { "id": "p4", "text": "Moist lining to dissolve gases" },
          { "id": "p5", "text": "Steep concentration gradient maintained" }
        ],
        "maxCheckable": 4,
        "marks": 4
      },
      "methodMarks": null,
      "solutionSteps": [
        { "text": "Large surface area for diffusion." },
        { "text": "Walls one cell thick â€” short diffusion distance." },
        { "text": "Rich capillary network â€” good blood supply, maintains gradient." },
        { "text": "Moist lining â€” gases dissolve before diffusing." }
      ],
      "topicTags": ["alveoli"],
      "skillTags": ["explain-adaptation"],
      "misconceptionTags": ["forgets-concentration-gradient"],
      "isTeacherMarkedInExam": true
    },
    {
      "id": "bio_07_e",
      "partLabel": "e",
      "type": "mcq",
      "marks": 1,
      "question": "Which of the following would NOT increase the rate of gas exchange?",
      "options": [
        { "id": "opt_a", "text": "Increasing surface area" },
        { "id": "opt_b", "text": "Increasing wall thickness" },
        { "id": "opt_c", "text": "Increasing blood flow" },
        { "id": "opt_d", "text": "Maintaining a concentration gradient" }
      ],
      "diagramRef": null,
      "graphRef": null,
      "dataTableRef": null,
      "answerSchema": {
        "type": "mcq",
        "correct": "opt_b"
      },
      "methodMarks": null,
      "solutionSteps": [
        { "text": "Thicker walls increase diffusion distance â€” slowing gas exchange." },
        { "text": "All other options increase the rate of diffusion." }
      ],
      "topicTags": ["alveoli"],
      "skillTags": ["evaluate-factors"],
      "misconceptionTags": ["confuses-thickness-with-permeability"],
      "isTeacherMarkedInExam": false
    }
  ]
}
```

---

## 9. Migration Checklist

When updating existing scenario files and code to this schema:

- [ ] Replace `scenario.diagramSpec` (single) â†’ `scenario.diagrams` (keyed map)
- [ ] Replace `scenario.graphSpec` (single) â†’ `scenario.graphs` (keyed map)
- [ ] Replace `scenario.dataTable` (single) â†’ `scenario.dataTables` (keyed map)
- [ ] Add `diagramRef`, `graphRef`, `dataTableRef` to every part (null if unused)
- [ ] Rename `teacherMarkedInExam` â†’ `isTeacherMarkedInExam` on every part
- [ ] **MCQ parts:** Move `answerSchema.options` â†’ `part.options`, strip `isCorrect` flags, set `answerSchema.correct` to the correct option ID
- [ ] **Diagram `imageSrc`:** Prefix all paths with `./src/assets/diagrams/`
- [ ] **Graph specs:** Convert `data` array â†’ `lines[0].points`, add `id` and `color`, remove `lineType`
- [ ] **Biology answer schemas:** Ensure `answerSchema.marks` is present and equals `part.marks` for `diagram_label`, `keyword_match`, `process_sequence`, `punnett_grid`, `self_assessed`
- [ ] Add `hotspotIds` to every `diagram_label` answerSchema
- [ ] Update all marker functions to accept `(studentAnswer, answerSchema, ctx)` signature
- [ ] Update all marker functions to return the standardised `MarkResult` shape
- [ ] Update ProcessSequence answer format to include `initialOrder`
- [ ] Generate `attemptId` at test start, store in session state
- [ ] Update results dashboard to separate auto-marked and teacher-marked scores in exam mode
- [ ] Update core Test Runner to resolve resource refs before passing to components
- [ ] Add new scenario ID to `src/app.js` `loadScenarios()` `ids` array
- [ ] Add dev-time validation (see Section 10)

---

## 10. Validation Rules

Run these checks at scenario load time in dev builds. They catch broken references and schema violations before runtime.

### 10.1 Resource Reference Validation

```javascript
function validateScenario(scenario) {
  const errors = [];
  for (const part of scenario.parts) {
    if (part.diagramRef && !scenario.diagrams?.[part.diagramRef])
      errors.push(`Part ${part.id}: diagramRef "${part.diagramRef}" not found in scenario.diagrams`);
    if (part.graphRef && !scenario.graphs?.[part.graphRef])
      errors.push(`Part ${part.id}: graphRef "${part.graphRef}" not found in scenario.graphs`);
    if (part.dataTableRef && !scenario.dataTables?.[part.dataTableRef])
      errors.push(`Part ${part.id}: dataTableRef "${part.dataTableRef}" not found in scenario.dataTables`);
  }
  return errors;
}
```

### 10.2 Diagram Label Validation

```javascript
function validateDiagramLabel(part, scenario) {
  const errors = [];
  if (part.type !== 'diagram_label') return errors;
  if (!part.diagramRef) { errors.push(`Part ${part.id}: diagram_label requires diagramRef`); return errors; }

  const diagram = scenario.diagrams?.[part.diagramRef];
  if (!diagram) return errors;

  const hotspotIds = part.answerSchema?.hotspotIds || [];
  const diagramHotspotIds = diagram.hotspots.map(h => h.id);
  const termBankIds = diagram.termBank.map(t => t.id);

  for (const hid of hotspotIds) {
    if (!diagramHotspotIds.includes(hid))
      errors.push(`Part ${part.id}: hotspotId "${hid}" not found in diagram "${part.diagramRef}"`);
  }
  for (const hotspot of diagram.hotspots) {
    if (!termBankIds.includes(hotspot.correct))
      errors.push(`Diagram "${part.diagramRef}": hotspot "${hotspot.id}" correct value "${hotspot.correct}" not in termBank`);
  }
  if (diagram.imageSrc && !diagram.imageSrc.startsWith('./src/assets/diagrams/'))
    errors.push(`Diagram "${part.diagramRef}": imageSrc must start with "./src/assets/diagrams/"`);

  return errors;
}
```

### 10.3 MCQ Validation

```javascript
function validateMcq(part) {
  const errors = [];
  if (part.type !== 'mcq') return errors;

  if (!part.options || !Array.isArray(part.options))
    errors.push(`Part ${part.id}: MCQ requires part.options array`);
  if (part.answerSchema?.options)
    errors.push(`Part ${part.id}: MCQ options must be at part level, not inside answerSchema`);
  if (!part.answerSchema?.correct)
    errors.push(`Part ${part.id}: MCQ answerSchema requires "correct" field`);
  if (part.options && part.answerSchema?.correct) {
    const optionIds = part.options.map(o => o.id);
    if (!optionIds.includes(part.answerSchema.correct))
      errors.push(`Part ${part.id}: answerSchema.correct "${part.answerSchema.correct}" not found in part.options`);
  }
  return errors;
}
```

### 10.4 Graph Spec Validation

```javascript
function validateGraphSpec(scenario) {
  const errors = [];
  for (const [key, graph] of Object.entries(scenario.graphs || {})) {
    if (graph.data && !graph.lines)
      errors.push(`Graph "${key}": uses "data" array â€” must convert to "lines" format`);
    if (!graph.lines || !Array.isArray(graph.lines))
      errors.push(`Graph "${key}": missing "lines" array`);
    else {
      for (const line of graph.lines) {
        if (!line.id) errors.push(`Graph "${key}": line missing "id"`);
        if (!line.color) errors.push(`Graph "${key}": line missing "color"`);
        if (!line.points || !Array.isArray(line.points))
          errors.push(`Graph "${key}": line "${line.id}" missing "points" array`);
      }
    }
    if (graph.lineType)
      errors.push(`Graph "${key}": "lineType" field is not supported â€” remove it`);
  }
  return errors;
}
```

### 10.5 Process Sequence Validation

```javascript
function validateProcessSequence(part) {
  const errors = [];
  if (part.type !== 'process_sequence') return errors;

  const stepIds = part.answerSchema.steps.map(s => s.id);
  const correctOrder = part.answerSchema.correctOrder;

  if (correctOrder.length !== stepIds.length)
    errors.push(`Part ${part.id}: correctOrder length (${correctOrder.length}) !== steps length (${stepIds.length})`);
  for (const id of correctOrder) {
    if (!stepIds.includes(id))
      errors.push(`Part ${part.id}: correctOrder contains "${id}" which is not in steps`);
  }
  return errors;
}
```

### 10.6 Marks Consistency Validation

```javascript
function validateMarksConsistency(part) {
  const errors = [];
  const biologyTypes = ['diagram_label', 'keyword_match', 'process_sequence', 'punnett_grid', 'self_assessed'];

  if (biologyTypes.includes(part.type)) {
    if (part.answerSchema?.marks === undefined)
      errors.push(`Part ${part.id}: Biology type "${part.type}" requires answerSchema.marks (must equal part.marks = ${part.marks})`);
    else if (part.answerSchema.marks !== part.marks)
      errors.push(`Part ${part.id}: answerSchema.marks (${part.answerSchema.marks}) !== part.marks (${part.marks})`);
  }
  return errors;
}
```

### 10.7 Self-Assessed Validation

```javascript
function validateSelfAssessed(part) {
  const errors = [];
  if (part.type !== 'self_assessed') return errors;

  const { markSchemePoints, maxCheckable } = part.answerSchema;
  if (maxCheckable > markSchemePoints.length)
    errors.push(`Part ${part.id}: maxCheckable (${maxCheckable}) > markSchemePoints count (${markSchemePoints.length})`);
  if (!part.isTeacherMarkedInExam)
    errors.push(`Part ${part.id}: self_assessed part should have isTeacherMarkedInExam: true`);
  return errors;
}
```

### 10.8 Keyword Match Validation

```javascript
function validateKeywordMatch(part) {
  const errors = [];
  if (part.type !== 'keyword_match') return errors;

  const { passage, blanks, wordBank } = part.answerSchema;
  const wordBankIds = wordBank.map(w => w.id);

  for (const blank of blanks) {
    if (!wordBankIds.includes(blank.correct))
      errors.push(`Part ${part.id}: blank "${blank.id}" correct value "${blank.correct}" not in wordBank`);
    if (!passage.includes(`{${blank.id}}`))
      errors.push(`Part ${part.id}: blank "${blank.id}" not found as {${blank.id}} in passage`);
  }
  return errors;
}
```

### 10.9 Running Validation

```javascript
function validateAllScenarios(scenarios, isDev = false) {
  if (!isDev) return;

  for (const scenario of scenarios) {
    const errors = [
      ...validateScenario(scenario),
      ...validateGraphSpec(scenario),
      ...scenario.parts.flatMap(p => [
        ...validateDiagramLabel(p, scenario),
        ...validateMcq(p),
        ...validateProcessSequence(p),
        ...validateMarksConsistency(p),
        ...validateSelfAssessed(p),
        ...validateKeywordMatch(p)
      ])
    ];

    if (errors.length > 0) {
      console.error(`âŒ Scenario "${scenario.id}" validation errors:`);
      errors.forEach(e => console.error(`  â€¢ ${e}`));
    }
  }
}
```

---

## 11. Quick-Fix Script for New Scenarios

When a content author produces a new scenario JSON, it will likely use the "natural" format (options inside answerSchema, bare image paths, flat data arrays). Run this Python script to convert to app-compatible format:

```python
import json, sys

with open(sys.argv[1]) as f:
    d = json.load(f)

for p in d['parts']:
    s = p['answerSchema']
    # Fix 1: MCQ options â†’ part level
    if s['type'] == 'mcq' and 'options' in s:
        correct_id = next(o['id'] for o in s['options'] if o.get('isCorrect'))
        p['options'] = [{'id': o['id'], 'text': o['text']} for o in s['options']]
        s['correct'] = correct_id
        del s['options']
    # Fix 2: marks in answerSchema for Biology types
    if s['type'] in ('keyword_match', 'diagram_label', 'self_assessed',
                      'process_sequence', 'punnett_grid') and 'marks' not in s:
        s['marks'] = p['marks']

# Fix 3: imageSrc paths
for diag in (d.get('diagrams') or {}).values():
    src = diag.get('imageSrc', '')
    if src and not src.startswith('./src/'):
        diag['imageSrc'] = f'./src/assets/diagrams/{src.split("/")[-1]}'

# Fix 4: graph data â†’ lines
for key, g in (d.get('graphs') or {}).items():
    if 'data' in g and 'lines' not in g:
        g['lines'] = [{'id': key, 'color': '#007AFF', 'points': g['data']}]
        del g['data']
        g.pop('lineType', None)

with open(sys.argv[1], 'w') as f:
    json.dump(d, f, indent=2)
    f.write('\n')

print(f'âœ… Fixed {sys.argv[1]}')
```

**Usage:** `python3 fix_scenario.py src/data/scenarios/bio_12.json`

After running, add the scenario ID to `src/app.js` `loadScenarios()`.

---

**End of Schema Document**