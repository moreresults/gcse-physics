# Scenario JSON Schema Fixes — Lessons Learned
## GCSE Biology Content Pipeline
### v1.1

Every new scenario JSON must be post-processed before it will work with the app. Here are the required changes:

## 1. MCQ Options — Move to Part Level

**Problem:** Scenario authors put `options` inside `answerSchema` with an `isCorrect` flag on each option.

**App expects:** `options` at the **part** level (not inside `answerSchema`), with a separate `answerSchema.correct` string set to the winning option ID.

**Before (wrong):**
```json
{
  "id": "bio_11_c",
  "type": "mcq",
  "answerSchema": {
    "type": "mcq",
    "options": [
      { "id": "opt_a", "text": "...", "isCorrect": false },
      { "id": "opt_b", "text": "...", "isCorrect": true }
    ]
  }
}
```

**After (correct):**
```json
{
  "id": "bio_11_c",
  "type": "mcq",
  "options": [
    { "id": "opt_a", "text": "..." },
    { "id": "opt_b", "text": "..." }
  ],
  "answerSchema": {
    "type": "mcq",
    "correct": "opt_b"
  }
}
```

**Fix:** Move `answerSchema.options` → `part.options`, strip `isCorrect` from each option, add `answerSchema.correct` = the `id` of the option that had `isCorrect: true`.

---

## 2. Diagram `imageSrc` — Must Be Root-Relative

**Problem:** Authors use bare filenames like `"heart.svg"` or partial paths like `"assets/cilia-damage.svg"`.

**App expects:** Root-relative paths starting with `./src/assets/diagrams/` because the app is served from `index.html` at the project root.

**Before (wrong):**
```json
"imageSrc": "heart.svg"
"imageSrc": "assets/cilia-damage.svg"
```

**After (correct):**
```json
"imageSrc": "./src/assets/diagrams/heart.svg"
"imageSrc": "./src/assets/diagrams/cilia-damage.svg"
```

**Fix:** Prefix all `imageSrc` values with `./src/assets/diagrams/`, stripping any existing partial path.

---

## 3. Graph Spec — `data` → `lines` Format

**Problem:** Authors use `{ data: [{x, y}], lineType: "smooth" }`.

**App expects:** `{ lines: [{ id, color, points: [{x, y}] }] }` — the Physics `Graph.js` renderer iterates `spec.lines` and accesses `line.points`.

**Before (wrong):**
```json
"graphs": {
  "enzymeCurve": {
    "xAxis": { ... },
    "yAxis": { ... },
    "data": [{ "x": 10, "y": 5 }, ...],
    "lineType": "smooth"
  }
}
```

**After (correct):**
```json
"graphs": {
  "enzymeCurve": {
    "xAxis": { ... },
    "yAxis": { ... },
    "lines": [{
      "id": "enzymeCurve",
      "color": "#007AFF",
      "points": [{ "x": 10, "y": 5 }, ...]
    }]
  }
}
```

**Fix:** Wrap `data` array into `lines[0].points`, add `id` (use the graph key) and `color` (`"#007AFF"`), delete `data` and `lineType`.

---

## 4. Answer Schema `marks` Field

**Problem:** Some answer schemas (especially `keyword_match`, `diagram_label`, `self_assessed`) are missing the `marks` field inside the schema object.

**App expects:** `answerSchema.marks` to exist for Biology types so the marking engine knows the max marks.

**Fix:** Copy `part.marks` into `answerSchema.marks` if absent.

---

## 5. Add `bio_XX` to App Scenario List

After adding the JSON file to `src/data/scenarios/`, update `src/app.js` — add the new ID to the `ids` array in `loadScenarios()`.

---

## 6. Create Placeholder SVG If Needed

If the scenario references a new diagram, create a matching SVG in `src/assets/diagrams/`. Use the existing SVGs as reference — 550-600px wide, `#007AFF` blue letter markers at hotspot positions, flat-colour line art.

---

## 7. Always Produce Claude Code Instructions, Not Manual Steps

**When a task can be executed by Claude Code, the output should be a Claude Code prompt — not a list of manual terminal commands for the human to run.**

During Sprint 2b academic QA, corrected JSON files were produced and the human was given manual instructions: copy files from Downloads, run the validator, run verification scripts, stage files, commit, and tag. This is exactly the kind of deterministic, multi-step, error-prone work that Claude Code exists to automate.

**The correct pattern:**
1. Identify the fixes needed (with reasoning).
2. Package them as a single, self-contained Claude Code prompt with explicit file paths, exact edits, validation commands, and commit instructions.
3. The human pastes one prompt. Claude Code does the rest.

**The anti-pattern:**
- "Open Terminal and run…"
- "Copy the downloaded file to…"
- "Then run this command to check…"
- Any instruction that assumes the human will manually move files between their browser downloads folder and a git repo.

**Why this matters:** Manual steps introduce transcription errors, missed steps, and wasted time. Claude Code can read the files, make the edits in place, validate, and commit — all in one execution. The human's job is to review the output and approve the commit, not to be a copy-paste relay between two AI systems.

**Rule of thumb:** If you're writing more than 3 lines of terminal commands for the human, you should be writing a Claude Code prompt instead.

---

## Summary: The Five-Minute Checklist

Before handing off any new scenario JSON:

- [ ] MCQ options at part level with `answerSchema.correct` (Lesson 1)
- [ ] Diagram `imageSrc` uses `./src/assets/diagrams/` prefix (Lesson 2)
- [ ] Graph uses `lines[].points` format, not `data` (Lesson 3)
- [ ] `answerSchema.marks` present for keyword_match, diagram_label, self_assessed (Lesson 4)
- [ ] Scenario ID added to app scenario list (Lesson 5)
- [ ] Placeholder SVG created if new diagram referenced (Lesson 6)
- [ ] Automation delivered as Claude Code prompts, not manual steps (Lesson 7)

---

## Quick-Fix Python Script

Run this on any new scenario JSON to apply all fixes at once:

```python
import json, sys

with open(sys.argv[1]) as f:
    d = json.load(f)

for p in d['parts']:
    s = p['answerSchema']
    # Fix 1: MCQ options
    if s['type'] == 'mcq' and 'options' in s:
        correct_id = next(o['id'] for o in s['options'] if o.get('isCorrect'))
        p['options'] = [{'id': o['id'], 'text': o['text']} for o in s['options']]
        s['correct'] = correct_id
        del s['options']
    # Fix 4: marks in schema
    if s['type'] in ('keyword_match', 'diagram_label', 'self_assessed') and 'marks' not in s:
        s['marks'] = p['marks']

# Fix 2: imageSrc paths
for diag in d.get('diagrams', {}).values():
    src = diag.get('imageSrc', '')
    if src and not src.startswith('./src/'):
        diag['imageSrc'] = f'./src/assets/diagrams/{src.split("/")[-1]}'

# Fix 3: graph data -> lines
for key, g in d.get('graphs', {}).items():
    if 'data' in g and 'lines' not in g:
        g['lines'] = [{'id': key, 'color': '#007AFF', 'points': g['data']}]
        del g['data']
        g.pop('lineType', None)

with open(sys.argv[1], 'w') as f:
    json.dump(d, f, indent=2)
    f.write('\n')
```

Usage: `python3 fix_scenario.py src/data/scenarios/bio_12.json`

---

*End of Lessons — v1.1*
