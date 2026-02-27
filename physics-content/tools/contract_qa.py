#!/usr/bin/env python3
"""
Contract compliance checker — validates all 21 Biology scenario JSONs
against their coverage contracts in BIOLOGY_CONTENT_BRIEF_v1_3.md.

Usage:
    python3 tools/contract_qa.py
"""

import json
import re
import glob
import sys
from pathlib import Path

# ── Paths ────────────────────────────────────────────────────────────────────
BASE = Path(__file__).resolve().parent.parent
BRIEF = BASE / "governing" / "BIOLOGY_CONTENT_BRIEF_v1_3.md"
SCENARIO_DIRS = [BASE / "scenarios" / "bio", BASE / "gold"]

# ── Type mapping: contract name → JSON type ──────────────────────────────────
TYPE_MAP = {
    "explain": "self_assessed",
    "numeric": "calculation",
    "calculate": "calculation",
    "diagram_label": "diagram_label",
    "mcq": "mcq",
    "graph_reading": "graph_reading",
    "process_sequence": "process_sequence",
    "keyword_match": "keyword_match",
    "punnett_grid": "punnett_grid",
    "self_assessed": "self_assessed",
    "calculation": "calculation",
    "data_table": "data_table",
}


def load_scenarios():
    """Load all 21 scenario JSONs, keyed by scenario ID."""
    scenarios = {}
    for d in SCENARIO_DIRS:
        for f in sorted(d.glob("EXAMPLE_SCENARIO_bio_*.json")):
            with open(f) as fh:
                data = json.load(fh)
            scenarios[data["id"]] = data
    return scenarios


def parse_contracts(brief_path):
    """Parse all contract blocks from the content brief."""
    with open(brief_path) as f:
        text = f.read()

    # Split into fenced code blocks that contain "Scenario ID:"
    blocks = re.findall(r"```\n(.*?)```", text, re.DOTALL)
    contracts = {}

    for block in blocks:
        if "Scenario ID:" not in block:
            continue

        c = {}

        # Scenario ID
        m = re.search(r"Scenario ID:\s*(bio_\d+)", block)
        if not m:
            continue
        sid = m.group(1)
        c["id"] = sid

        # Mark target
        m = re.search(r"Mark target:\s*(\d+)", block)
        c["marks"] = int(m.group(1)) if m else 0

        # Parts count
        m = re.search(r"Parts:\s*(\d+)", block)
        c["parts"] = int(m.group(1)) if m else 0

        # AO spread
        m = re.search(r"AO spread:\s*AO1:\s*(\d+),\s*AO2:\s*(\d+),\s*AO3:\s*(\d+)", block)
        if m:
            c["ao"] = {"AO1": int(m.group(1)), "AO2": int(m.group(2)), "AO3": int(m.group(3))}
        else:
            c["ao"] = {"AO1": 0, "AO2": 0, "AO3": 0}

        # Interaction types per part — parse lines like:
        # - Part (a): diagram_label — AO1 — 5 marks (description)
        c["part_specs"] = []
        for pm in re.finditer(
            r"-\s*Part\s*\((\w)\):\s*(\w+)\s*—\s*(AO[123])\s*—\s*(\d+)\s*marks?",
            block,
        ):
            label = pm.group(1)
            ptype = pm.group(2).strip()
            ao = pm.group(3)
            marks = int(pm.group(4))
            c["part_specs"].append({
                "label": label,
                "type": TYPE_MAP.get(ptype, ptype),
                "ao": ao,
                "marks": marks,
            })

        # Required misconceptions
        misconceptions = []
        in_misc = False
        for line in block.split("\n"):
            if line.strip().startswith("Required misconceptions:"):
                in_misc = True
                continue
            if in_misc:
                m2 = re.match(r"^-\s*(\S+)", line.strip())
                if m2:
                    misconceptions.append(m2.group(1))
                else:
                    in_misc = False
        c["misconceptions"] = misconceptions

        # Required subtopics (those marked "must appear")
        subtopics = []
        in_sub = False
        for line in block.split("\n"):
            if line.strip().startswith("Required subtopics:"):
                in_sub = True
                continue
            if in_sub:
                if line.strip().startswith("-"):
                    if "must appear" in line.lower():
                        # Extract keyword(s) before the dash/em-dash
                        topic_text = re.sub(r"\s*—.*", "", line.strip().lstrip("- "))
                        subtopics.append(topic_text.strip())
                else:
                    in_sub = False
        c["subtopics"] = subtopics

        # Required assets
        c["needs_diagram"] = False
        c["needs_graph"] = False
        c["needs_datatable"] = False

        for line in block.split("\n"):
            stripped = line.strip()
            if stripped.startswith("Diagram requirements:"):
                rest = stripped.replace("Diagram requirements:", "").strip()
                if not rest.lower().startswith("none"):
                    c["needs_diagram"] = True
            elif stripped.startswith("Graph requirements:"):
                rest = stripped.replace("Graph requirements:", "").strip()
                if not rest.lower().startswith("none"):
                    c["needs_graph"] = True
            elif stripped.startswith("Data table requirements:"):
                rest = stripped.replace("Data table requirements:", "").strip()
                if not rest.lower().startswith("none"):
                    c["needs_datatable"] = True

        # Handle multi-line asset requirements that start with "-" on the next line
        if not c["needs_diagram"] and "Diagram requirements:" in block:
            idx = block.index("Diagram requirements:")
            after = block[idx:].split("\n")
            first_line = after[0].replace("Diagram requirements:", "").strip()
            if first_line.lower().startswith("none") or first_line == "":
                # Check if next lines have content (multi-line requirement)
                if first_line == "" and len(after) > 1 and after[1].strip().startswith("-"):
                    c["needs_diagram"] = True
            else:
                c["needs_diagram"] = True

        if not c["needs_graph"] and "Graph requirements:" in block:
            idx = block.index("Graph requirements:")
            after = block[idx:].split("\n")
            first_line = after[0].replace("Graph requirements:", "").strip()
            if first_line.lower().startswith("none") or first_line == "":
                if first_line == "" and len(after) > 1 and after[1].strip().startswith("-"):
                    c["needs_graph"] = True
            else:
                c["needs_graph"] = True

        if not c["needs_datatable"] and "Data table requirements:" in block:
            idx = block.index("Data table requirements:")
            after = block[idx:].split("\n")
            first_line = after[0].replace("Data table requirements:", "").strip()
            if first_line.lower().startswith("none") or first_line == "":
                if first_line == "" and len(after) > 1 and after[1].strip().startswith("-"):
                    c["needs_datatable"] = True
            else:
                c["needs_datatable"] = True

        contracts[sid] = c

    return contracts


def check_scenario(scenario, contract):
    """Check one scenario against its contract. Returns (results_dict, failures_list)."""
    sid = contract["id"]
    results = {}
    failures = []

    parts = scenario["parts"]

    # 1. Part count
    ok = len(parts) == contract["parts"]
    results["parts"] = ok
    if not ok:
        failures.append(f"Parts — contract says {contract['parts']} but JSON has {len(parts)}")

    # 2. Mark total
    total_marks = sum(p["marks"] for p in parts)
    ok = total_marks == contract["marks"]
    results["marks"] = ok
    if not ok:
        failures.append(f"Marks — contract says {contract['marks']} but JSON sums to {total_marks}")

    # 3. AO spread — use contract's per-part AO assignments
    ao_actual = {"AO1": 0, "AO2": 0, "AO3": 0}
    ao_ok = True
    if len(contract["part_specs"]) == len(parts):
        for i, spec in enumerate(contract["part_specs"]):
            ao_actual[spec["ao"]] += parts[i]["marks"]
        ao_ok = ao_actual == contract["ao"]
    else:
        # Can't compute AO if part counts don't match
        ao_ok = False
    results["ao"] = ao_ok
    if not ao_ok:
        failures.append(
            f"AO spread — contract says AO1:{contract['ao']['AO1']}, "
            f"AO2:{contract['ao']['AO2']}, AO3:{contract['ao']['AO3']} "
            f"but JSON gives AO1:{ao_actual['AO1']}, AO2:{ao_actual['AO2']}, AO3:{ao_actual['AO3']}"
        )

    # 4. Interaction types per part
    types_ok = True
    type_failures = []
    for i, spec in enumerate(contract["part_specs"]):
        if i < len(parts):
            json_type = parts[i]["type"]
            if json_type != spec["type"]:
                types_ok = False
                type_failures.append(
                    f"Part ({spec['label']}) contract says \"{spec['type']}\" but JSON has \"{json_type}\""
                )
    results["types"] = types_ok
    if not types_ok:
        for tf in type_failures:
            failures.append(f"Types — {tf}")

    # 5. Required misconceptions
    all_tags = set()
    for p in parts:
        for tag in p.get("misconceptionTags", []):
            all_tags.add(tag)
    missing = [t for t in contract["misconceptions"] if t not in all_tags]
    results["misconceptions"] = len(missing) == 0
    if missing:
        failures.append(f"Misconceptions — missing: {', '.join(missing)}")

    # 6. Required subtopics
    all_topic_tags = set()
    for p in parts:
        for tag in p.get("topicTags", []):
            all_topic_tags.add(tag.lower())

    subtopic_ok = True
    missing_subs = []
    for sub in contract["subtopics"]:
        # Extract key terms from the subtopic description
        keywords = _extract_subtopic_keywords(sub)
        found = False
        for tag in all_topic_tags:
            if any(kw in tag for kw in keywords):
                found = True
                break
        if not found:
            subtopic_ok = False
            missing_subs.append(sub)
    results["subtopics"] = subtopic_ok
    if not subtopic_ok:
        failures.append(f"Subtopics — not matched: {'; '.join(missing_subs)}")

    # 7. Required assets
    assets_ok = True
    asset_failures = []
    if contract["needs_diagram"]:
        diagrams = scenario.get("diagrams")
        if diagrams is None or (isinstance(diagrams, dict) and len(diagrams) == 0):
            assets_ok = False
            asset_failures.append("contract requires diagrams but JSON diagrams is null/empty")
    if contract["needs_graph"]:
        graphs = scenario.get("graphs")
        if graphs is None or (isinstance(graphs, dict) and len(graphs) == 0):
            assets_ok = False
            asset_failures.append("contract requires graphs but JSON graphs is null/empty")
    if contract["needs_datatable"]:
        dt = scenario.get("dataTables")
        if dt is None or (isinstance(dt, dict) and len(dt) == 0):
            assets_ok = False
            asset_failures.append("contract requires dataTables but JSON dataTables is null/empty")
    results["assets"] = assets_ok
    if not assets_ok:
        for af in asset_failures:
            failures.append(f"Assets — {af}")

    return results, failures


def _extract_subtopic_keywords(subtopic_text):
    """
    Extract lowercase keyword fragments from a subtopic description.
    E.g. 'Osmosis — must appear' → ['osmosis']
    E.g. 'Punnett square cross' → ['punnett']
    E.g. 'Blood glucose regulation' → ['blood-glucose', 'glucose']
    """
    text = subtopic_text.lower()
    # Remove parenthetical content
    text = re.sub(r"\(.*?\)", "", text)
    # Remove common filler
    text = text.replace("—", "").replace("must appear", "").strip()

    keywords = []

    # Build keyword map for common subtopic patterns
    keyword_map = {
        "animal & plant cell organelles": ["organelle", "cell-structure", "cell."],
        "prokaryotic vs eukaryotic": ["prokaryotic", "eukaryotic"],
        "microscopy & magnification": ["microscop", "magnification"],
        "mitosis stages": ["mitosis"],
        "cell cycle": ["mitosis", "cell-division"],
        "stem cells": ["stem-cell"],
        "diffusion": ["diffusion"],
        "osmosis": ["osmosis"],
        "active transport": ["active-transport"],
        "sa:v ratio": ["sa-v-ratio", "surface-area"],
        "digestive system organs and order": ["digest"],
        "enzymes": ["enzyme"],
        "bile function": ["bile"],
        "heart structure": ["heart", "circulation"],
        "blood vessels": ["artery", "vein", "capillary", "blood-vessel", "circulation"],
        "double circulation": ["double", "circulation"],
        "types of pathogens": ["pathogen", "infection"],
        "how diseases spread": ["disease", "spread", "infection"],
        "non-specific defences": ["defence", "phagocyt", "non-specific"],
        "phagocytosis": ["phagocyt"],
        "antibodies & vaccination": ["antibod", "vaccin"],
        "word/symbol equation": ["equation", "photosynthesis"],
        "limiting factors": ["limiting-factor", "photosynthesis"],
        "leaf structure adaptations": ["leaf", "photosynthesis"],
        "aerobic respiration equation": ["aerobic", "respiration"],
        "anaerobic respiration": ["anaerobic"],
        "oxygen debt": ["oxygen-debt", "anaerobic", "respiration"],
        "lock-and-key": ["enzyme", "lock-and-key", "substrate"],
        "effect of temperature on enzyme activity": ["enzyme", "temperature"],
        "denaturation": ["enzyme", "denatur"],
        "lung structure": ["lung", "gas-exchange"],
        "alveoli adaptations": ["alveol", "gas-exchange"],
        "diffusion of o": ["diffusion", "gas-exchange"],
        "stomata and guard cells": ["stomata", "guard"],
        "transpiration": ["transpiration"],
        "factors affecting transpiration": ["transpiration"],
        "xylem and phloem": ["xylem", "phloem"],
        "translocation": ["translocation", "phloem"],
        "reflex arc": ["reflex"],
        "neuron types": ["neuron", "reflex"],
        "brain regions": ["brain"],
        "eye structure": ["eye"],
        "accommodation": ["accommodation", "eye", "focus"],
        "endocrine glands": ["endocrine"],
        "insulin and glucagon": ["insulin", "glucagon", "blood-glucose"],
        "negative feedback": ["negative-feedback", "feedback"],
        "blood glucose regulation": ["blood-glucose", "glucose"],
        "thermoregulation": ["thermoregulation"],
        "osmoregulation": ["osmoregulation", "adh"],
        "dna structure, genes, alleles": ["dna", "gene", "allele", "inheritance"],
        "dominant/recessive, genotype/phenotype": ["genotype", "phenotype", "dominant", "recessive"],
        "punnett square cross": ["punnett"],
        "continuous vs discontinuous variation": ["variation", "continuous", "discontinuous"],
        "mutations": ["mutation"],
        "darwin's theory of natural selection": ["darwin", "natural-selection"],
        "evidence for evolution": ["evolution", "evidence"],
        "antibiotic resistance": ["antibiotic-resistance", "antibiotic"],
        "food chains/webs and energy flow": ["food-chain", "food-web", "energy"],
        "sampling methods": ["quadrat", "transect", "sampling"],
        "biodiversity": ["biodiversity"],
    }

    # Try to match against known patterns
    for pattern, kws in keyword_map.items():
        if pattern in text:
            return kws

    # Fallback: split on spaces and use individual words > 3 chars
    words = re.split(r"[\s,/&]+", text)
    for w in words:
        w = w.strip().rstrip("s")  # crude singularize
        if len(w) > 3:
            keywords.append(w)

    return keywords if keywords else [text.strip()]


def main():
    # Load data
    scenarios = load_scenarios()
    contracts = parse_contracts(BRIEF)

    if len(scenarios) != 21:
        print(f"ERROR: Found {len(scenarios)} scenarios, expected 21")
        sys.exit(1)
    if len(contracts) != 21:
        print(f"ERROR: Parsed {len(contracts)} contracts, expected 21")
        sys.exit(1)

    # Run checks
    all_results = {}
    all_failures = {}
    for sid in sorted(contracts.keys(), key=lambda x: int(x.split("_")[1])):
        if sid not in scenarios:
            print(f"ERROR: No scenario JSON found for {sid}")
            sys.exit(1)
        results, failures = check_scenario(scenarios[sid], contracts[sid])
        all_results[sid] = results
        all_failures[sid] = failures

    # Print table
    print()
    print("=== CONTRACT COMPLIANCE QA — ALL 21 SCENARIOS ===")
    print()
    header = f"{'Scenario':<10} {'Parts':>5} {'Marks':>5} {'AO':>10} {'Types':>7} {'Misconc':>9} {'Subtopics':>9} {'Assets':>7} {'Status':>7}"
    print(header)
    print("-" * len(header))

    pass_count = 0
    fail_count = 0

    for sid in sorted(all_results.keys(), key=lambda x: int(x.split("_")[1])):
        r = all_results[sid]
        status = "PASS" if all(r.values()) else "FAIL"
        if status == "PASS":
            pass_count += 1
        else:
            fail_count += 1

        def icon(v):
            return "\u2705" if v else "\u274c"

        row = (
            f"{sid:<10} "
            f"{icon(r['parts']):>5} "
            f"{icon(r['marks']):>5} "
            f"{icon(r['ao']):>10} "
            f"{icon(r['types']):>7} "
            f"{icon(r['misconceptions']):>9} "
            f"{icon(r['subtopics']):>9} "
            f"{icon(r['assets']):>7} "
            f"{status:>7}"
        )
        print(row)

    print()

    # Print failures
    has_failures = any(len(f) > 0 for f in all_failures.values())
    if has_failures:
        print("FAILURES:")
        for sid in sorted(all_failures.keys(), key=lambda x: int(x.split("_")[1])):
            for failure in all_failures[sid]:
                print(f"  {sid}: {failure}")
        print()

    print(f"TOTAL: {pass_count}/21 PASS, {fail_count}/21 FAIL")

    sys.exit(0 if fail_count == 0 else 1)


if __name__ == "__main__":
    main()
