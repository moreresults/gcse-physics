# Science Content Creation Roadmap
## GCSE Revision Platform — Biology, Chemistry, Physics
### Version 1.3 · February 2026

**v1.3 changelog:** Incorporated GPT QA round 3. Bumped authoring rules reference to v1.1. Four micro-fixes applied to authoring rules: TAG1–TAG2 (misconception master list control to prevent synonym drift at scale), MC15 tightened (lowest whole-number coefficients only for equation balancer), DIA5 added (illustrator reproducibility test), macro-level AO distribution check added to academic QA. Each subject content brief now required to include a master misconceptions list. Roadmap declared production-ready — no further structural changes before authoring begins.

**v1.2 changelog:** Incorporated GPT QA round 2. Added difficulty calibration rules (DIF1–DIF5) to authoring rules. Added cross-subject consistency clause (CS1–CS4). Added scope control rules (SC1–SC4) preventing interaction type creep. Added Biology-specific rules: cross-topic dependency control (BIO1–BIO2), Punnett strictness (MC9–MC10 with ratio simplification, probability format acceptance), graph precision alignment (GR2, MC14). All new rules are now in `SCIENCE_CONTENT_AUTHORING_RULES_v1_1.md` — the roadmap references rather than duplicates.

**v1.1 changelog:** Incorporated GPT QA round 1. Added operational authoring rules with marking conventions and tag taxonomy. Added per-topic coverage contracts. Standardised content repo structure. Split QA into mechanical + academic layers. Added assembly-line authoring process with enforced step order. Tightened project file sets into must-have vs recommended.

---

## 1. Strategic Context

The maths platform (ReviseMaths) has achieved full curriculum coverage with 72 template generators across 28 topics, producing 4.5M+ unique question variants. While maths continues through launch, monetisation, and diagnostic assessment development, there is a significant opportunity to **parallelise science content creation** so that when the science platform is ready to build, the content is already waiting.

Content creation is the slow, labour-intensive part of each subject. Template generation for maths took multiple sprint briefs and dozens of hours per sprint. Science scenarios are even more involved — each is a multi-part exam-style question with context paragraphs, diagram specifications, worked solutions, and misconception tags.

**The goal:** Keep Claude Code building content continuously. When it's not fixing maths bugs or implementing maths features, it should be authoring science scenario JSON files.

---

## 2. Scope Summary

| Subject | Exam Board | Spec Code | Topics | Scenarios | Est. Questions | Est. Marks |
|---------|-----------|-----------|--------|-----------|---------------|------------|
| Physics | Edexcel IGCSE | 4PH1 | 19 | 21 | ~100 | ~205 |
| Biology | Edexcel IGCSE | 4BI1 | 21 | 21 | ~100 | ~200 |
| Chemistry | Edexcel IGCSE | 4CH1 | 23 | 23 | ~110 | ~220 |
| **Total** | | | **63** | **65** | **~310** | **~625** |

All three subjects follow the same scenario-based architecture: multi-part questions with interactive components, conforming to the Unified Scenario Schema v1.3.

---

## 3. Key Architectural Difference: Maths vs Sciences

**Maths content model:** Topic JSON files containing individual standalone questions (static + template-generated). Template generators produce numeric variants. The platform is a Next.js app with client-side quiz sessions.

**Science content model:** Scenario JSON files containing multi-part exam questions. Each scenario has a context paragraph, optional diagrams/graphs/data tables, and 4–5 linked parts progressing through a narrative. Content format is fundamentally different — scenarios, not topic question banks.

**What this means for content creation:** Science scenarios are self-contained JSON files. They can be authored entirely independently of the platform code. Each scenario file is a complete, validated data object that a future platform simply loads and renders. Content has **zero dependency on platform code**.

---

## 4. Claude Project Organisation

### 4.1 Project Structure

| Project | Purpose | Status |
|---------|---------|--------|
| **GCSE Maths** (this project) | Maths platform dev, launch, monetisation | Active |
| **GCSE Physics — Content** | Physics scenario authoring | To create |
| **GCSE Biology — Content** | Biology scenario authoring | To create |
| **GCSE Chemistry — Content** | Chemistry scenario authoring | To create |

### 4.2 Project File Sets

**Must-have (required to start authoring):**

| Document | Purpose |
|----------|---------|
| `UNIFIED_SCENARIO_SCHEMA_v1_3.md` | Canonical JSON schema for all scenarios |
| `SCIENCE_CONTENT_AUTHORING_RULES_v1_1.md` | Operational rules: marking, tagging, solutions, diagrams, difficulty, scope control, cross-subject consistency |
| `[SUBJECT]_Curriculum_v1_0.docx` | Subject-specific curriculum plan (already exists) |
| `[SUBJECT]_CONTENT_BRIEF.md` | Per-topic coverage contracts + build order |
| `EXAMPLE_SCENARIO_bio_01.json` | Gold-standard reference scenario |

**Strongly recommended (prevents rework at scale):**

| Document | Purpose |
|----------|---------|
| `BIOLOGY_CLAUDE_CODE_BRIEF.md` | Existing full brief with 10 scenario specs (Biology project only) |

The tag taxonomy, marking conventions, difficulty calibration, cross-subject consistency rules, and scope control rules are all embedded in `SCIENCE_CONTENT_AUTHORING_RULES_v1_1.md`. This is the single governing document for content quality across all three subjects.

---

## 5. Content Repo Structure

Every science project uses the same directory layout. Consistency is non-negotiable.

```
/scenarios/
  bio_01.json
  bio_02.json
  ...
  bio_21.json
  _manifest.json       # Index of all scenarios with metadata + QA status

/diagram-specs/
  bio_01_cell.json     # Split out only when diagramSpec exceeds ~20 lines inline

/validation/
  validate-scenario.md # Checklist reference (mirrors authoring rules Step 7)
```

**File naming:** `[subject_prefix]_[topic_number].json` — e.g. `phy_01.json`, `bio_07.json`, `chem_15.json`. Two-digit zero-padded. No exceptions.

**Manifest file** (`_manifest.json`):
```json
{
  "subject": "biology",
  "specCode": "4BI1",
  "schemaVersion": "1.3",
  "authoringRulesVersion": "1.1",
  "scenarios": [
    { "id": "bio_01", "file": "bio_01.json", "topic": "Cell Structure", "status": "complete", "marks": 10, "parts": 5 },
    { "id": "bio_02", "file": "bio_02.json", "topic": "Cell Division", "status": "draft", "marks": 9, "parts": 4 },
    { "id": "bio_03", "file": "bio_03.json", "topic": "Transport in Cells", "status": "qa-flagged", "marks": 10, "parts": 5, "qaNote": "MC1 tolerance query on osmosis calculation" }
  ]
}
```

---

## 6. Governing Documents

Content quality is controlled by three documents working together:

| Document | Governs | Versioned? |
|----------|---------|------------|
| `UNIFIED_SCENARIO_SCHEMA_v1_3.md` | JSON structure — what fields exist and their types | Yes (locked at v1.3 for all content creation) |
| `SCIENCE_CONTENT_AUTHORING_RULES_v1_1.md` | Content quality — how fields are populated, marking logic, tagging, difficulty, solutions, scope | Yes |
| `[SUBJECT]_CONTENT_BRIEF.md` | Coverage — what each scenario must contain, topic by topic | Yes (per subject) |

The schema defines structure. The authoring rules define quality. The content brief defines coverage. All three must be satisfied for a scenario to pass QA.

---

## 7. What Gets Created Now vs Later

### Phase A — Content Creation (NOW, parallelised with maths work)

- Scenario JSON files — complete, schema-valid, rules-compliant
- Diagram specifications — hotspot positions, label banks, structure descriptions (per DIA1–DIA5)
- Graph specifications — axis ranges, data points, line types, interactive modes (per GR1–GR4)
- Data table specifications — row/column data
- Worked solutions — full step-by-step per SOL1–SOL5
- All three tag types on every part per the controlled taxonomy
- Manifest files tracking completion and QA status

### Phase B — Platform Build (LATER, after maths launch stabilises)

- Interactive components (shared + subject-specific)
- SVG diagram assets from specs
- Marking engine adapters
- Subject module registration and quiz runner integration
- Persistence, feature gating, results dashboard

Phase B depends on Phase A being complete. Phase A has zero dependency on Phase B.

---

## 8. Per-Topic Coverage Contracts

Each subject's content brief (`[SUBJECT]_CONTENT_BRIEF.md`) defines a coverage contract for every topic, following this template:

```
## Topic [N]: [Topic Name]

Scenario ID: [subject]_[nn]
Mark target: [8–12]
Parts: [4–5]

### Required subtopics (from curriculum doc):
- [Subtopic A] — must appear in at least one part
- [Subtopic B] — must appear in at least one part

### Interaction types:
- Part (a): [type] — [AO level] — [marks]
- Part (b): [type] — [AO level] — [marks]
- ...

### Required misconceptions (must be tagged):
- [misconception-tag]: [brief description]

### Diagram/graph requirements:
- [What visuals are needed]

### AO spread:
- AO1: [n] marks, AO2: [n] marks, AO3: [n] marks
```

Coverage contracts prevent authoring drift and make mechanical QA deterministic. The full set of contracts (21 for Biology, 19+2 for Physics, 23 for Chemistry) are written in the subject-specific content briefs.

Each subject content brief must also include a **master misconceptions list** — the approved set of misconception tags for that subject (per TAG1–TAG2 in the authoring rules). Authors select from this list; new tags require formal addition to the list before use in any scenario.

---

## 9. Subject-Specific Build Notes

### 9.1 Biology

**Unique component:** Punnett grid

**Head start:** Scenarios bio_01 through bio_10 already fully specified in `BIOLOGY_CLAUDE_CODE_BRIEF.md`.

**Subject-specific rules (from authoring rules):** BIO1 (cross-topic allowed but can't replace required subtopics), BIO2 (no forward-dependency on later topics), BIO3 (Punnett grid completion and interpretation are always separate parts).

**Build priority:**
1. Group 2 — Infection, Response & Bioenergetics (T6–T10): 5 scenarios
2. Group 5 — Genetics, Evolution & Ecology (T18–T21): 4 scenarios
3. Group 1 — Cell Biology & Organisation (T1–T5): 5 scenarios
4. Group 3 — Exchange & Transport (T11–T13): 3 scenarios
5. Group 4 — Nervous System & Homeostasis (T14–T17): 4 scenarios

### 9.2 Physics

**Unique component:** Interactive SVG graph with crosshair reading

**Subject-specific rules:** PHY1 (graph type must be explicit), PHY2 (formulae provided, not recalled).

**Build priority:**
1. Group 1 — Forces & Motion (T1–T5): 6 scenarios (T1 gets 2)
2. Group 2 — Electricity & Magnetism (T6–T9): 5 scenarios (T6 gets 2)
3. Group 3 — Waves (T10–T13): 4 scenarios
4. Group 4 — Thermal & Energy (T14–T16): 3 scenarios
5. Group 5 — Radioactivity & Space (T17–T19): 3 scenarios

### 9.3 Chemistry

**Unique components (5):** Equation balancer, dot-and-cross diagrams, electrolysis diagram, periodic table picker, energy profile diagram

**Subject-specific rules:** CHEM1 (Unicode subscript notation), CHEM2 (state symbols required), CHEM3 (full method chain for mole calculations). Plus MC15–MC16 for equation balancer schemas.

**Component dependency note:** Scenarios requiring unique components should still have complete JSON with correct `answerSchema` types. Content is authored regardless of whether the rendering component exists yet (SC1–SC2 apply).

**Build priority:**
1. Group 3 — Reactions & Calculations (T9–T15): 7 scenarios
2. Group 1 — Particles & Structure (T1–T4): 4 scenarios
3. Group 4 — Inorganic Chemistry (T16–T19): 4 scenarios
4. Group 2 — Periodic Table (T5–T8): 4 scenarios
5. Group 5 — Organic & Earth (T20–T23): 4 scenarios

---

## 10. Execution Roadmap

### Sprint 1 — Foundation Setup (2–3 hours)

| Task | Est. Time |
|------|-----------|
| Write `SCIENCE_CONTENT_AUTHORING_RULES_v1_1.md` | ✅ Complete |
| Write `BIOLOGY_CONTENT_BRIEF.md` with 21 coverage contracts | 45 min |
| Extract `bio_01.json` gold-standard example from existing brief | 15 min |
| Create "GCSE Biology — Content" Claude project + upload docs | 20 min |
| Create "GCSE Physics — Content" project (docs follow later) | 10 min |
| Create "GCSE Chemistry — Content" project (docs follow later) | 10 min |
| Write `PHYSICS_CONTENT_BRIEF.md` with 19+2 coverage contracts | 45 min |
| Write `CHEMISTRY_CONTENT_BRIEF.md` with 23 coverage contracts | 45 min |

### Sprint 2 — Biology Content

**Target:** 21 scenarios, ~100 questions, ~200 marks

| Phase | Scenarios | Notes | Est. Hours |
|-------|-----------|-------|------------|
| 2a — Existing 10 | bio_01 to bio_10 | Transcribe from existing brief, validate against schema + rules | 8–10 |
| 2b — Remaining 11 | bio_11 to bio_21 | New authoring from coverage contracts | 15–20 |
| 2c — Mechanical QA | All 21 | Step 7 checklist on every file | 2–3 |
| 2d — Academic QA | All 21 | GPT adversarial review, batch by curriculum group | 3–4 |
| **Total** | **21** | | **28–37 hrs** |

### Sprint 3 — Physics Content

**Target:** 21 scenarios, ~100 questions, ~205 marks

| Phase | Scenarios | Notes | Est. Hours |
|-------|-----------|-------|------------|
| 3a — Group 1 (Forces) | phy_01 to phy_06 | 6 scenarios, graph-heavy | 10–12 |
| 3b — Group 2 (Electricity) | phy_07 to phy_11 | 5 scenarios, circuit diagrams | 8–10 |
| 3c — Groups 3–5 | phy_12 to phy_21 | 10 scenarios, varied | 12–15 |
| 3d — QA (both layers) | All 21 | Mechanical + academic | 4–5 |
| **Total** | **21** | | **34–42 hrs** |

### Sprint 4 — Chemistry Content

**Target:** 23 scenarios, ~110 questions, ~220 marks

| Phase | Scenarios | Notes | Est. Hours |
|-------|-----------|-------|------------|
| 4a — Group 3 (Reactions) | chem_09 to chem_15 | 7 scenarios, calculation-heavy | 12–14 |
| 4b — Group 1 (Particles) | chem_01 to chem_04 | 4 scenarios | 6–8 |
| 4c — Groups 2, 4, 5 | chem_05–08, chem_16–23 | 12 scenarios | 15–18 |
| 4d — QA (both layers) | All 23 | Mechanical + academic | 4–5 |
| **Total** | **23** | | **37–45 hrs** |

### Total Content Creation Estimate

| Subject | Scenarios | Est. Hours |
|---------|-----------|------------|
| Foundation setup | — | 2–3 |
| Biology | 21 | 28–37 |
| Physics | 21 | 34–42 |
| Chemistry | 23 | 37–45 |
| **Grand Total** | **65** | **101–127 hrs** |

---

## 11. Sequencing Rationale

**Biology first:** Most existing documentation (10 pre-specified scenarios). Fewest unique components (Punnett grid only). Fastest path to a complete subject — validates the authoring pipeline before tackling harder subjects.

**Physics second:** Graph reading component is well-understood from the original prototype. Calculation-heavy content is structurally simpler. Builds momentum from Biology sprint.

**Chemistry last:** Most unique components (5 new types). Most scenarios (23). Equation-balancer answer schemas require the most careful design. Benefits from lessons learned on Biology and Physics.

---

## 12. Instructions for Claude Code

When Claude Code picks up a science content sprint:

> **Your task:** Author scenario JSON files for [Subject] conforming to the Unified Scenario Schema v1.3.
>
> **Read first (in this order):**
> 1. `SCIENCE_CONTENT_AUTHORING_RULES_v1_1.md` — marking, tagging, solutions, diagrams, difficulty, scope, cross-subject rules
> 2. `UNIFIED_SCENARIO_SCHEMA_v1_3.md` — JSON schema
> 3. `[SUBJECT]_CONTENT_BRIEF.md` — per-topic coverage contracts and build order
> 4. `EXAMPLE_SCENARIO_bio_01.json` — gold-standard reference
> 5. `[Subject]_Curriculum_v1_0.docx` — exam board spec alignment
>
> **Process:** Follow the 7-step assembly line (authoring rules Section 11) for every scenario. Do not skip steps. Do not move to the next scenario until Step 7 validation passes.
>
> **Output:** One JSON file per scenario in `/scenarios/`. Update `_manifest.json` after each scenario.
>
> **Build order:** Follow the priority order in the subject content brief.
>
> **Do not:** Write any platform code, component code, CSS, or TypeScript. This is pure content authoring.

---

## 13. Risk Register

| Risk | Impact | Mitigation |
|------|--------|------------|
| Schema drift between content creation and platform build | High | Schema locked at v1.3 for all content creation. Changes require migration plan before approval |
| Diagram specs insufficient for SVG creation | Medium | DIA1–DIA5 enforce completeness. Academic QA flags ambiguous specs |
| Chemistry equation balancer schemas are wrong | Medium | MC15–MC16 define the rules. Validate against known stoichiometry |
| Tag taxonomy drifts across subjects | Medium | CS1 locks skill tags to controlled vocabulary. Single authoring rules doc shared across all projects |
| Difficulty drifts across subjects | Medium | DIF1–DIF5 + CS2 enforce consistent calibration. Academic QA checks cross-subject alignment |
| Interaction type scope creep | Medium | SC1–SC3 lock the type inventory. New types require schema version bump + formal approval |
| Content accuracy (scientific errors) | High | Two-layer QA. Academic QA with GPT adversarial review |
| Claude Code context window limits | Low | One scenario per session. Carry forward only schema + rules + curriculum doc + coverage contract for current topic |

---

## 14. Success Criteria

Content creation is complete when:

- [ ] 65 scenario JSON files exist across three subjects
- [ ] Every file passes mechanical QA (schema-valid, marks add up, all fields present, tags from controlled vocabulary)
- [ ] Every file passes academic QA (accurate, authentic, defensible, difficulty-calibrated)
- [ ] Every part has complete answer schemas, solution steps, and all three tag types
- [ ] Every diagram-dependent part has a spec following DIA1–DIA5
- [ ] Every graph-dependent part has a spec following GR1–GR4
- [ ] Manifest files are accurate, all scenarios show `"complete"` status
- [ ] Tag taxonomy is consistent across all 65 scenarios (no synonymous tags, no naming drift)
- [ ] Difficulty calibration is consistent across subjects (DIF1–DIF5 + CS2 verified)

---

## 15. Immediate Next Steps

| Step | Deliverable | Status |
|------|-------------|--------|
| 1 | `SCIENCE_CONTENT_AUTHORING_RULES_v1_1.md` | ✅ Complete — send to GPT for final stress-test |
| 2 | `BIOLOGY_CONTENT_BRIEF.md` (21 coverage contracts + master misconceptions list) | Next |
| 3 | `EXAMPLE_SCENARIO_bio_01.json` (gold-standard) | After step 2 |
| 4 | Create Biology Claude project + upload 5 must-have docs | After step 3 |
| 5 | Start Sprint 2a — transcribe existing 10 scenarios | After step 4 |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Feb 2026 | Initial roadmap. Project structure, scope, sequencing, high-level authoring approach. |
| 1.1 | Feb 2026 | GPT QA round 1: Operational authoring rules, per-topic coverage contracts, standardised repo structure, two-layer QA, assembly-line process, tightened project file sets. |
| 1.2 | Feb 2026 | GPT QA round 2: Difficulty calibration (DIF1–DIF5), cross-subject consistency (CS1–CS4), scope control (SC1–SC4), Biology rules (BIO1–BIO3), Punnett strictness (MC9–MC10), graph precision (GR2, MC14). All rules in standalone authoring rules doc. Governing documents section added. `authoringRulesVersion` added to manifest schema. |
| 1.3 | Feb 2026 | GPT QA round 3: Authoring rules bumped to v1.1. TAG1–TAG2 (misconception master list control), MC15 tightened (lowest whole-number coefficients only), DIA5 (illustrator reproducibility test), macro-level AO balance check in academic QA. Subject content briefs now required to include master misconceptions list. Roadmap declared production-ready. |

---

**End of Science Content Roadmap v1.3**
