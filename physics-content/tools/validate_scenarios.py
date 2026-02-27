#!/usr/bin/env python3
"""
validate_scenarios.py — Mechanical QA for Biology scenario JSON files
Run: python3 validate_scenarios.py EXAMPLE_SCENARIO_bio_04.json [...]
Or:  python3 validate_scenarios.py *.json

Checks all items from the Sprint 2a-T2 Task Brief validation checklist.
Exit code 0 = all pass, 1 = failures found.
"""

import json
import sys
import os
from pathlib import Path

# ── Controlled vocabulary ─────────────────────────────────────────────────────

VALID_SKILLS = {
    "recall-fact", "recall-definition", "recall-equation", "label-diagram",
    "apply-equation", "rearrange-equation", "interpret-graph", "describe-trend",
    "calculate", "order-process", "complete-punnett", "interpret-ratio",
    "balance-equation", "classify", "convert-units", "interpret-data-table",
    "explain-mechanism", "evaluate-method", "predict-outcome", "compare-contrast",
    "justify-conclusion", "suggest-improvement",
}

VALID_TYPES = {
    "mcq", "numeric_with_unit", "calculation", "graph_reading",
    "diagram_label", "process_sequence", "keyword_match", "punnett_grid",
    "self_assessed", "equation_balancer", "data_table",
}

REQUIRED_PART_FIELDS = {
    "id", "partLabel", "type", "marks", "question",
    "diagramRef", "graphRef", "dataTableRef",
    "answerSchema", "methodMarks", "solutionSteps",
    "topicTags", "skillTags", "misconceptionTags",
    "isTeacherMarkedInExam",
}

REQUIRED_TOP_FIELDS = {
    "id", "title", "icon", "subject", "context", "difficulty",
    "diagrams", "graphs", "dataTables", "parts",
}

REQUIRED_DIAGRAM_FIELDS = {
    "imageSrc", "imageAlt", "title", "description",
    "width", "aspectRatio", "hotspots", "termBank",
}

# ── Contracts (from Content Brief v1.2) ───────────────────────────────────────

CONTRACTS = {
    "bio_04": {
        "marks": 10, "parts": 5,
        "subtopics": ["digest", "enzyme", "bile"],
        "misconceptions": {"confuses-enzyme-substrate", "thinks-bile-is-an-enzyme", "confuses-digestive-organs-order"},
    },
    "bio_05": {
        "marks": 10, "parts": 5,
        "subtopics": ["heart", "blood-vessel", "circulation"],
        "misconceptions": {"confuses-arteries-veins", "thinks-all-blood-vessels-have-valves", "confuses-double-single-circulation"},
    },
    "bio_10": {
        "marks": 11, "parts": 5,
        "subtopics": ["lock-and-key", "temperature", "denaturation"],
        "misconceptions": {"thinks-enzymes-die-at-high-temp", "confuses-rate-with-amount", "thinks-all-enzymes-have-same-optimum"},
    },
    "bio_18": {
        "marks": 11, "parts": 5,
        "subtopics": ["allele", "genotype", "punnett"],
        "misconceptions": {"confuses-gene-allele-chromosome", "dominant-means-more-common", "confuses-genotype-phenotype", "confuses-homozygous-heterozygous", "punnett-allele-order-error"},
    },
    "bio_21": {
        "marks": 10, "parts": 5,
        "subtopics": ["food-chain", "quadrat", "biodiversity"],
        "misconceptions": {"confuses-food-chain-energy-flow", "forgets-sampling-method-limitations", "confuses-biodiversity-abundance", "confuses-abiotic-biotic"},
    },
    # Gold standards (for re-validation)
    "bio_01": {"marks": 10, "parts": 5, "subtopics": ["organelle", "cell-structure", "microscop"], "misconceptions": {"confuses-mitochondria-chloroplast", "resolution-vs-magnification", "confuses-organelles", "confuses-prokaryotic-eukaryotic"}},
    "bio_08": {"marks": 11, "parts": 5, "subtopics": ["equation", "limiting-factor", "leaf"], "misconceptions": {"confuses-photosynthesis-respiration-equations", "thinks-plants-only-photosynthesise", "confuses-limiting-factors"}},
    "bio_09": {"marks": 9, "parts": 5, "subtopics": ["aerobic", "anaerobic", "oxygen-debt"], "misconceptions": {"thinks-respiration-is-breathing", "confuses-aerobic-anaerobic-products", "forgets-oxygen-debt", "thinks-anaerobic-produces-no-energy"}},
    "bio_11": {"marks": 11, "parts": 5, "subtopics": ["lung-structure", "alveoli", "diffusion"], "misconceptions": {"confuses-respiration-gas-exchange", "thinks-oxygen-actively-pumped", "forgets-co2-moves-opposite", "confuses-alveoli-adaptations"}},
    "bio_14": {"marks": 10, "parts": 5, "subtopics": ["reflex-arc", "neuron", "reaction-time"], "misconceptions": {"confuses-neuron-types", "confuses-reflex-arc-order", "thinks-brain-controls-reflexes", "includes-anomalies-in-mean"}},
}

# ── Validator ─────────────────────────────────────────────────────────────────

def validate(filepath: str) -> list[str]:
    """Returns list of error strings. Empty = pass."""
    errors = []

    # 1. JSON parse
    try:
        with open(filepath) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return [f"FATAL: JSON parse error: {e}"]

    sid = data.get("id", "UNKNOWN")

    # 2. Top-level fields
    missing_top = REQUIRED_TOP_FIELDS - set(data.keys())
    if missing_top:
        errors.append(f"Missing top-level fields: {sorted(missing_top)}")

    parts = data.get("parts", [])

    # 3. Part count + marks (contract check)
    contract = CONTRACTS.get(sid)
    if contract:
        if len(parts) != contract["parts"]:
            errors.append(f"Part count: {len(parts)} (contract: {contract['parts']})")
        total_marks = sum(p.get("marks", 0) for p in parts)
        if total_marks != contract["marks"]:
            errors.append(f"Mark total: {total_marks} (contract: {contract['marks']})")
    else:
        total_marks = sum(p.get("marks", 0) for p in parts)

    # 4. Part-level required fields
    for p in parts:
        pid = p.get("id", "?")
        missing_p = REQUIRED_PART_FIELDS - set(p.keys())
        if missing_p:
            errors.append(f"{pid}: missing fields {sorted(missing_p)}")

    # 5. Tag validation
    all_topic_tags = []
    all_misconception_tags = set()
    for p in parts:
        pid = p.get("id", "?")
        tt = p.get("topicTags", [])
        st = p.get("skillTags", [])
        mt = p.get("misconceptionTags", [])
        all_topic_tags.extend(tt)
        all_misconception_tags.update(mt)

        # Count bounds
        if not (1 <= len(tt) <= 3):
            errors.append(f"{pid}: topicTags count {len(tt)} (need 1-3)")
        if not (1 <= len(st) <= 2):
            errors.append(f"{pid}: skillTags count {len(st)} (need 1-2)")
        if not (1 <= len(mt) <= 3):
            errors.append(f"{pid}: misconceptionTags count {len(mt)} (need 1-3)")

        # Skill vocabulary
        for s in st:
            if s not in VALID_SKILLS:
                errors.append(f"{pid}: skill tag '{s}' NOT in controlled vocabulary")

        # Topic tag format
        for t in tt:
            if not t.startswith("bio.") or len(t.split(".")) < 3:
                errors.append(f"{pid}: topic tag format invalid: '{t}'")

    # 6. Contract: required subtopics
    if contract:
        for sub in contract.get("subtopics", []):
            if not any(sub in t for t in all_topic_tags):
                errors.append(f"Required subtopic '{sub}' not found in any topic tag")

    # 7. Contract: required misconceptions
    if contract:
        missing_m = contract.get("misconceptions", set()) - all_misconception_tags
        if missing_m:
            errors.append(f"Missing required misconceptions: {sorted(missing_m)}")

    # 8. MCQ validation
    for p in parts:
        if p.get("type") == "mcq":
            pid = p.get("id", "?")
            opts = p.get("options", [])
            if len(opts) != 4:
                errors.append(f"{pid}: MCQ has {len(opts)} options (need 4)")
            correct = p.get("answerSchema", {}).get("correct")
            if correct and not any(o.get("id") == correct for o in opts):
                errors.append(f"{pid}: MCQ correct '{correct}' not in options")
            # Check options NOT in answerSchema
            if "options" in p.get("answerSchema", {}):
                errors.append(f"{pid}: MCQ options found inside answerSchema (should be at part.options)")

    # 9. Self-assessed validation
    for p in parts:
        if p.get("type") == "self_assessed":
            pid = p.get("id", "?")
            schema = p.get("answerSchema", {})
            points = schema.get("markSchemePoints", [])
            mc = schema.get("maxCheckable", 0)
            sm = schema.get("marks", 0)
            tm = p.get("isTeacherMarkedInExam", False)
            if mc != p.get("marks"):
                errors.append(f"{pid}: maxCheckable ({mc}) != part.marks ({p.get('marks')})")
            if sm != p.get("marks"):
                errors.append(f"{pid}: schema.marks ({sm}) != part.marks ({p.get('marks')})")
            if mc > len(points):
                errors.append(f"{pid}: maxCheckable ({mc}) > markSchemePoints count ({len(points)})")
            if not tm:
                errors.append(f"{pid}: self_assessed must have isTeacherMarkedInExam: true")

    # 10. Keyword match validation
    for p in parts:
        if p.get("type") == "keyword_match":
            pid = p.get("id", "?")
            schema = p.get("answerSchema", {})
            passage = schema.get("passage", "")
            blanks = schema.get("blanks", [])
            wb = schema.get("wordBank", [])
            wb_ids = [w["id"] for w in wb]
            n_dist = len(wb) - len(blanks)
            if not (2 <= n_dist <= 4):
                errors.append(f"{pid}: wordBank distractors = {n_dist} (need 2-4)")
            for b in blanks:
                if b.get("correct") not in wb_ids:
                    errors.append(f"{pid}: blank '{b.get('id')}' correct '{b.get('correct')}' not in wordBank")
                token = "{" + b.get("id", "") + "}"
                if token not in passage:
                    errors.append(f"{pid}: blank '{b.get('id')}' token not in passage")

    # 11. Diagram validation
    diagrams = data.get("diagrams") or {}
    for name, diag in diagrams.items():
        missing_d = REQUIRED_DIAGRAM_FIELDS - set(diag.keys())
        if missing_d:
            errors.append(f"Diagram '{name}': missing fields {sorted(missing_d)}")
        n_h = len(diag.get("hotspots", []))
        n_t = len(diag.get("termBank", []))
        n_dist = n_t - n_h
        if not (2 <= n_dist <= 4):
            errors.append(f"Diagram '{name}': distractors = {n_dist} (need N+2 to N+4)")

    # DiagramRef validity
    for p in parts:
        ref = p.get("diagramRef")
        if ref and ref not in diagrams:
            errors.append(f"{p.get('id')}: diagramRef '{ref}' not found in diagrams")

    # 12. Graph validation
    graphs = data.get("graphs") or {}
    for gname, g in graphs.items():
        lines = g.get("lines", [])
        if not lines:
            errors.append(f"Graph '{gname}': no lines array")
        for line in lines:
            if "color" in line:
                errors.append(f"Graph '{gname}': line has 'color' field (remove - presentation detail)")
            if "id" not in line:
                errors.append(f"Graph '{gname}': line missing 'id'")
            if "points" not in line:
                errors.append(f"Graph '{gname}': line missing 'points'")
        if "lineType" not in g:
            errors.append(f"Graph '{gname}': missing 'lineType'")

    # GraphRef validity
    for p in parts:
        ref = p.get("graphRef")
        if ref and ref not in graphs:
            errors.append(f"{p.get('id')}: graphRef '{ref}' not found in graphs")

    # 13. Calculation: method marks present
    for p in parts:
        if p.get("type") == "calculation":
            pid = p.get("id", "?")
            mm = p.get("methodMarks")
            if mm is None or (isinstance(mm, list) and len(mm) == 0):
                errors.append(f"{pid}: calculation type must have methodMarks")

    # 14. Solution step counts
    for p in parts:
        pid = p.get("id", "?")
        steps = p.get("solutionSteps", [])
        if not (2 <= len(steps) <= 7):
            errors.append(f"{pid}: {len(steps)} solution steps (need 2-7)")

    # 15. Unique IDs
    all_ids = [p.get("id") for p in parts]
    if len(all_ids) != len(set(all_ids)):
        dupes = [x for x in all_ids if all_ids.count(x) > 1]
        errors.append(f"Duplicate part IDs: {dupes}")

    # 16. BIO3 — Punnett parts must be separate
    punnett_parts = [p for p in parts if p.get("type") == "punnett_grid"]
    if punnett_parts:
        # Check that no punnett_grid part also asks for probability/ratio
        for pp in punnett_parts:
            q = pp.get("question", "").lower()
            if "ratio" in q or "probability" in q or "chance" in q:
                errors.append(f"{pp.get('id')}: BIO3 violation — Punnett grid part must not include ratio/probability question (separate parts required)")

    # 17. isTeacherMarkedInExam consistency
    for p in parts:
        pid = p.get("id", "?")
        ptype = p.get("type")
        tm = p.get("isTeacherMarkedInExam")
        if ptype == "self_assessed" and tm is not True:
            pass  # Already caught above
        elif ptype != "self_assessed" and tm is True:
            errors.append(f"{pid}: isTeacherMarkedInExam should be false for type '{ptype}'")

    # 18. Orphan asset check — every defined diagram/graph/dataTable must be referenced
    for dname in diagrams:
        if not any(p.get("diagramRef") == dname for p in parts):
            errors.append(f"Orphan asset: diagram '{dname}' defined but never referenced by any part")
    for gname in graphs:
        if not any(p.get("graphRef") == gname for p in parts):
            errors.append(f"Orphan asset: graph '{gname}' defined but never referenced by any part")
    data_tables = data.get("dataTables") or {}
    for dtname in data_tables:
        if not any(p.get("dataTableRef") == dtname for p in parts):
            errors.append(f"Orphan asset: dataTable '{dtname}' defined but never referenced by any part")

    # 19. Non-zero tolerance must be justified by question type
    for p in parts:
        pid = p.get("id", "?")
        schema = p.get("answerSchema", {})
        tol = schema.get("tolerance")
        if tol is not None and tol != 0:
            # Tolerance > 0 is only valid for rate calculations or explicit overrides
            q = p.get("question", "").lower()
            has_rate_context = any(kw in q for kw in ["rate", "per minute", "per second", "per hour", "/min", "/s"])
            if not has_rate_context:
                errors.append(f"{pid}: tolerance={tol} but question doesn't appear to be a rate calculation — justify or set to 0")

    return errors


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    files = sys.argv[1:]
    if not files:
        # Auto-discover
        files = sorted(Path(".").glob("EXAMPLE_SCENARIO_bio_*.json"))
        if not files:
            print("Usage: python3 validate_scenarios.py <file1.json> [file2.json ...]")
            print("   Or: run from directory containing EXAMPLE_SCENARIO_bio_*.json files")
            sys.exit(1)
        files = [str(f) for f in files]

    total_errors = 0
    total_files = 0

    for filepath in files:
        total_files += 1
        fname = os.path.basename(filepath)
        errors = validate(filepath)

        if errors:
            print(f"\n❌ {fname} — {len(errors)} error(s):")
            for e in errors:
                print(f"   • {e}")
            total_errors += len(errors)
        else:
            # Quick summary
            with open(filepath) as f:
                d = json.load(f)
            parts = d.get("parts", [])
            marks = sum(p.get("marks", 0) for p in parts)
            types = [p.get("type") for p in parts]
            print(f"✅ {fname} — {len(parts)} parts, {marks} marks, types: {', '.join(types)}")

    print(f"\n{'='*50}")
    if total_errors == 0:
        print(f"ALL {total_files} FILES PASSED")
        sys.exit(0)
    else:
        print(f"{total_errors} TOTAL ERRORS across {total_files} files")
        sys.exit(1)


if __name__ == "__main__":
    main()
