import json, sys
with open(sys.argv[1]) as f:
    sc = json.load(f)
sid = sc["id"]
total = sum(p["marks"] for p in sc["parts"])
print(f"{sid}: {total} marks, {len(sc['parts'])} parts")
for p in sc["parts"]:
    assert p["type"] == p["answerSchema"]["type"], f"{p['id']}: type mismatch"
    if p["type"] == "self_assessed":
        assert p["isTeacherMarkedInExam"] == True, f"{p['id']}: missing teacher mark flag"
        assert p["answerSchema"].get("marks") == p["marks"], f"{p['id']}: marks mismatch"
    if p["type"] in ("diagram_label", "graph_reading", "process_sequence", "keyword_match", "data_table"):
        assert p["answerSchema"].get("marks") == p["marks"], f"{p['id']}: marks mismatch"
    if p["type"] in ("numeric_with_unit", "calculation"):
        tol_pct = abs(p["answerSchema"]["tolerance"] / p["answerSchema"]["correct"]) * 100
        assert tol_pct <= 2.01, f"{p['id']}: tolerance {tol_pct:.1f}% exceeds 2%"
        assert isinstance(p.get("methodMarks"), list) and len(p["methodMarks"]) >= 1, f"{p['id']}: methodMarks missing or empty"
    if p["type"] == "mcq":
        assert len(p.get("options", [])) == 4, f"{p['id']}: MCQ needs 4 options"
        assert p["answerSchema"]["correct"] in [o["id"] for o in p["options"]], f"{p['id']}: correct option missing"
    if p["type"] == "graph_reading":
        for r in p["answerSchema"].get("readings", []):
            tol_pct = abs(r["tolerance"] / r["correct"]) * 100
            assert tol_pct <= 2.01, f"{p['id']}/{r['id']}: tolerance {tol_pct:.1f}% exceeds 2%"
all_tags = set()
for p in sc["parts"]:
    all_tags.update(p.get("misconceptionTags", []))
print(f"  Misconception tags used: {sorted(all_tags)}")
print(f"✅ {sid} — all checks passed")
