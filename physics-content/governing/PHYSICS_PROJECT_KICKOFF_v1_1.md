# GCSE Physics — Project Kickoff Instructions v1.1
## For: New Claude Conversation in "GCSE Physics — Content" Project
### February 27, 2026

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-02-27 | Initial spec: 22 topics, ~210 marks, 5 gold examples, sprint structure, authority hierarchy |
| v1.1 | 2026-02-27 | QA hardening — 3 adjustments: (1) group-level AO ceiling ≤45%, (2) per-scenario validation required, (3) mark tolerance tightened to 208–212 hard range. Structural template instruction made explicit. |

---

## Your Role

You are authoring the complete GCSE Physics content set for a revision platform. Biology is already complete (21 scenarios, 208 marks, tagged `biology-content-v1.0`). You are replicating that proven pipeline for Physics.

**You are NOT starting from scratch.** The governing documents, schema, authoring rules, validator, and lessons learned are all proven and uploaded to this project. Your job is to follow them exactly.

---

## What's Already Done

| Artefact | Status | Location |
|----------|--------|----------|
| Repo scaffold | ✅ | `/Users/jameswatson/Dropbox/GIT/gcse-physics/physics-content/` |
| Schema | ✅ | `governing/UNIFIED_SCENARIO_SCHEMA_v1_3.md` |
| Authoring rules | ✅ | `governing/SCIENCE_CONTENT_AUTHORING_RULES_v1_2.md` |
| Curriculum source | ✅ | `governing/Physics_Curriculum_v1.0.docx` |
| Validator | ✅ | `tools/validate_scenarios.py` |
| Contract QA script | ✅ (needs Physics adaptation) | `tools/contract_qa.py` |
| Gold pattern references | ✅ | `gold/EXAMPLE_SCENARIO_bio_01.json`, `gold/EXAMPLE_SCENARIO_bio_08.json` |
| Lessons learned | ✅ | `LESSONS.md` (14 entries from Biology) |
| Biology content brief | ✅ (structural template) | Uploaded as `BIOLOGY_CONTENT_BRIEF_v1_2.md` |

---

## What You Need to Do — In Order

### Task 1: Write `PHYSICS_CONTENT_BRIEF_v1_0.md`

This is the foundation. Nothing else happens until this is written and validated.

**Read these files first:**
1. `Physics_Curriculum_v1.0.docx` — the 22 topics, subtopics, interaction types
2. `BIOLOGY_CONTENT_BRIEF_v1_2.md` — the structural template (**copy this format exactly — do not redesign section order**)
3. `SCIENCE_CONTENT_AUTHORING_RULES_v1_2.md` — rules the brief must comply with (especially PHY1, PHY2, TAG1–TAG2, SC1)
4. `SCIENCE_CONTENT_ROADMAP_v1_3.md` — strategic context and sprint structure

**The brief must contain these sections in this order:**

1. **Header** — "GCSE Physics — Content Brief", Edexcel IGCSE Physics (4PH1), Higher Tier, Version 1.0, governing doc references
2. **Build order** — Groups prioritised by exam weight:
   - Sprint 3a: Group 1 · Forces & Motion (T1–T5) — 5 scenarios
   - Sprint 3b: Group 2 · Electricity & Magnetism (T6–T10) — 5 scenarios
   - Sprint 3c: Group 3 · Waves & Light (T11–T14) — 4 scenarios
   - Sprint 3d: Groups 4+5 · Energy + Radioactivity & Space (T15–T22) — 8 scenarios
   - Sprint 3e: QA (structural + academic)
3. **Target totals** — 22 scenarios, ~110 questions, ~210 marks
4. **Target AO distribution** — AO1: ~30% (~63 marks), AO2: ~40% (~84 marks), AO3: ~30% (~63 marks). No category exceeds 40% at subject level. No curriculum group exceeds 45% in any AO category unless pedagogically justified with a written note.
5. **Master Misconceptions List** — Organised by curriculum group. Each entry: `tag-name` + one-line student error. Biology had 65; Physics needs 70–80. Cover these clusters thoroughly:
   - Forces: heavier-falls-faster, motion-requires-force, action-reaction-same-object, confuses-mass-weight, confuses-speed-velocity
   - Electricity: current-used-up, confuses-series-parallel, voltage-is-current, confuses-power-energy
   - Waves: EM-waves-need-medium, confuses-transverse-longitudinal, frequency-is-speed
   - Energy: heat-equals-temperature, cold-transfers-to-hot, confuses-energy-force
   - Radioactivity: radiation-makes-radioactive, half-life-means-half-gone, confuses-fission-fusion
6. **22 Coverage Contracts** — One per topic (phy_01 through phy_22). Each must contain:

```
Scenario ID: phy_XX
Mark target: [8–12]
Parts: [4–5]
Icon: [emoji]

Required subtopics:
- [Subtopic A] — must appear
- [Subtopic B] — must appear

Interaction types:
- Part (a): [type] — [AO level] — [N] marks (description)
- Part (b): [type] — [AO level] — [N] marks (description)
- ...

Required misconceptions:
- [tag-from-master-list]
- [tag-from-master-list]

Graph/Diagram/Data table requirements:
- [What visuals are needed, or "None"]

AO spread: AO1: X, AO2: Y, AO3: Z
```

7. **AO Distribution Summary Table** — By group and subject total, with 40% subject-level ceiling check and 45% group-level ceiling check. Format:

```
| Group | Topics | Total Marks | AO1 | AO2 | AO3 |
|-------|--------|-------------|-----|-----|-----|
| Group 1 | T1–T5 | XX | N (%) | N (%) | N (%) |
...
| TOTAL | T1–T22 | ~210 | N (~30%) | N (~40%) | N (~30%) |
```

Flag any group where an AO category exceeds 45% with a justification note or rebalance.

8. **Version History** — v1.0 entry with date and description

**Constraints on the brief:**
- Every misconception tag used in a contract MUST exist in the master list (TAG1–TAG2)
- Every part's interaction type MUST be from the approved list in SC1 (mcq, numeric, calculation, graph_reading, diagram_label, process_sequence, keyword_match, self_assessed, data_table)
- Parts must sum to mark target for every contract
- AO marks must sum to mark target for every contract
- Mark targets across all 22 contracts must sum to 208–212 (hard range)
- No AO category exceeds 40% at subject level
- No AO category exceeds 45% at group level (unless justified)

**Physics-specific rules to enforce in contracts:**
- PHY1: Every graph_reading part must specify the graph type (d-t, v-t, I-V, decay, force-extension, heating/cooling, wave displacement)
- PHY2: Any scenario involving equations of motion must note "formula sheet provided" in the contract notes
- Numeric tolerance: ±1% calculation, ±2% graph reading (note in contracts where graph reading applies)

### Task 2: Validate the Brief

Before proceeding, self-check:
- [ ] All 22 contracts present (phy_01 through phy_22)
- [ ] Every contract's parts sum to its mark target
- [ ] Every contract's AO marks sum to its mark target
- [ ] All misconception tags exist in the master list
- [ ] All interaction types are from the SC1 approved list
- [ ] AO distribution table is calculated from actual per-contract values (not estimated)
- [ ] No AO category exceeds 40% at subject level
- [ ] No AO category exceeds 45% at group level (or justified)
- [ ] PHY1 compliance: every graph_reading part specifies graph type
- [ ] PHY2 compliance: motion equation scenarios note formula sheet
- [ ] Grand total marks is within 208–212

### Task 3: Give the Human a Claude Code Prompt

Once the brief is validated, produce a Claude Code prompt that:

1. Saves `PHYSICS_CONTENT_BRIEF_v1_0.md` to `physics-content/governing/`
2. Commits it to git with message: "Physics content brief v1.0: 22 contracts, master misconceptions list, AO distribution"
3. Verifies the file is in place

**Do NOT ask the human to manually save the file. Always produce Claude Code instructions.**

### Task 4: Author 5 Gold Examples

After the brief is committed, author these 5 gold scenarios:

| Scenario | Topic | Why Selected |
|----------|-------|-------------|
| phy_01 | Motion & Speed | d-t graph + numeric + MCQ |
| phy_02 | Acceleration & Velocity | v-t graph + area-under-curve |
| phy_06 | Circuit Fundamentals | Circuit diagram + numeric |
| phy_13 | Light & Optics | Ray diagram SVG |
| phy_19 | Radioactive Decay & Half-Life | Decay graph + calculation |

Each gold example must:
- Follow its coverage contract exactly
- Comply with UNIFIED_SCENARIO_SCHEMA_v1_3
- Follow SCIENCE_CONTENT_AUTHORING_RULES_v1_2
- Pass the validator with 0 errors
- Use the same JSON structure as the Biology gold examples (bio_01, bio_08)

Produce a Claude Code prompt that:
1. Creates all 5 JSON files in `gold/`
2. Runs `python3 tools/validate_scenarios.py gold/EXAMPLE_SCENARIO_phy_*.json`
3. Commits with message: "5 Physics gold examples: phy_01, phy_02, phy_06, phy_13, phy_19"

### Task 5: Manufacture Remaining 17 Scenarios

Produce Claude Code task briefs (same format as Biology's `CLAUDE_CODE_SPRINT_2a_T2_TASK_BRIEF.md`) for:

- Sprint 3a: phy_03, phy_04, phy_05 (remaining Group 1)
- Sprint 3b: phy_07, phy_08, phy_09, phy_10 (remaining Group 2)
- Sprint 3c: phy_11, phy_12, phy_14 (remaining Group 3, phy_13 is gold)
- Sprint 3d: phy_15 through phy_22 (Groups 4+5, phy_19 is gold)

Each task brief tells Claude Code to:
1. Read the governing docs, gold examples, and contracts
2. Author each scenario following its contract
3. **Run `validate_scenarios.py` immediately after each scenario is written — not just at batch end**
4. Commit the batch

### Task 6: QA

After all 22 scenarios exist:
1. Adapt `tools/contract_qa.py` to parse `PHYSICS_CONTENT_BRIEF_v1_0.md`
2. Run structural validation on all 22
3. Run contract compliance on all 22
4. Academic spot-check on 3–5 highest-risk scenarios (recommend: phy_02, phy_06, phy_13, phy_19, phy_20)
5. Tag: `physics-content-v1.0`

---

## Critical Rules

1. **Schema is the structural authority.** If anything conflicts with `UNIFIED_SCENARIO_SCHEMA_v1_3.md`, the schema wins.
2. **Tags come from the master list only.** No invention. Add to list first, then use (TAG1–TAG2).
3. **Add up the numbers every time.** Marks, AO spreads, part counts — verify arithmetic, don't estimate.
4. **Always produce Claude Code prompts.** Never give the human manual terminal commands. (Lesson #14)
5. **Production-freeze applies during manufacturing.** Once the brief is committed, do not modify it during scenario authoring. Log issues for post-sprint resolution.
6. **Validate after every scenario.** Run `validate_scenarios.py` immediately after writing each scenario, not just at batch or sprint end.

---

## Authority Hierarchy

When documents disagree, resolve in this order:
1. `UNIFIED_SCENARIO_SCHEMA_v1_3.md` (structural authority)
2. `SCIENCE_CONTENT_AUTHORING_RULES_v1_2.md` (quality rules)
3. `PHYSICS_CONTENT_BRIEF_v1_0.md` (coverage contracts)
4. Gold examples (pattern reference)

---

## Start Now

Begin by reading `Physics_Curriculum_v1.0.docx` and `BIOLOGY_CONTENT_BRIEF_v1_2.md`, then draft the Physics content brief. Do not ask for confirmation — the decisions are already made:

- **22 topics, 22 scenarios** ✅
- **208–212 marks** ✅
- **Sprint structure as listed above** ✅
- **5 gold examples: phy_01, 02, 06, 13, 19** ✅

**Go.**
