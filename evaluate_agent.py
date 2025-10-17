import json, csv

with open("agent_data.json") as f:
    data = json.load(f)

annotations, summary_rows = [], []

for d in data:
    out = d.get("output","").strip().lower()
    exp = (d.get("expected_output") or "").strip().lower()
    if exp:
        is_correct = out == exp
        error_type = "None" if is_correct else "Incorrect factual/logic error"
    else:
        reasoning = d.get("reasoning",[])
        is_correct = len(reasoning) >= 2
        error_type = "Possible omission" if not is_correct else "None"

    annotations.append({
        "task": d.get("task"),
        "output": d.get("output"),
        "expected": d.get("expected_output"),
        "is_correct": is_correct,
        "error_type": error_type
    })
    summary_rows.append({
        "task": d.get("task"),
        "is_correct": is_correct,
        "error_type": error_type
    })

with open("annotations.json","w") as f:
    json.dump(annotations, f, indent=2)

with open("summary.csv","w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["task","is_correct","error_type"])
    writer.writeheader()
    writer.writerows(summary_rows)

print("✅ Annotation complete!  Check annotations.json and summary.csv.")
