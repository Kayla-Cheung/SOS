"""Pilot 0: synthetic CBM-I-inspired interpretation-bias experiment.

NOT human-grounded fidelity validation or a replicated psychological intervention.
Requires Python >=3.10. Standard-library only for --mode mock.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
SYSTEM = (
    "Complete an interpretation-rating exercise. Think of the scenario as an "
    "everyday uncertain situation. Rate each proposed explanation independently "
    "from 0 (not at all plausible) to 4 (very plausible). "
    "No explanation is necessarily correct. Respond only in the required JSON format."
)
CONDITIONS = ("positive", "balanced")


def load_stimuli(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    assess, training = data["assessment"], data["training"]
    assert len(assess) == 12 and len(training) == 10, "Expected 12 assessment and 10 training items"
    ids = [x["id"] for x in assess + training]
    assert len(ids) == len(set(ids)), "Duplicate stimulus IDs"
    for item in assess:
        assert all(item[k] for k in ("scenario", "negative", "benign"))
    for item in training:
        assert all(item[k] for k in ("stem", "positive", "negative"))
    return data


def make_schema() -> dict[str, Any]:
    return {
        "type": "json_schema", "name": "interpretation_ratings", "strict": True,
        "schema": {
            "type": "object", "additionalProperties": False,
            "properties": {
                "ratings": {
                    "type": "array",
                    "items": {
                        "type": "object", "additionalProperties": False,
                        "properties": {"id": {"type": "string"}, "x": {"type": "integer"}, "y": {"type": "integer"}},
                        "required": ["id", "x", "y"]
                    }
                }
            },
            "required": ["ratings"]
        }
    }


def format_assessment(items: list[dict[str, Any]], rng: random.Random) -> tuple[str, dict[str, str]]:
    lines = ["Rate BOTH explanations for each independent scenario from 0 to 4. "
             "Return exactly one entry per ID as JSON: {ratings:[{id,x,y}, ...]}. "
             "Use x for Explanation X and y for Explanation Y."]
    x_valence = {}
    for item in items:
        # Keep valence labels entirely internal. Randomize explanation position.
        choices = [(item["negative"], "negative"), (item["benign"], "benign")]
        rng.shuffle(choices)
        x_valence[item["id"]] = choices[0][1]
        lines.append(f"\n{item['id']}: {item['scenario']}")
        lines.append(f"Explanation X: {choices[0][0]}")
        lines.append(f"Explanation Y: {choices[1][0]}")
    return "\n".join(lines), x_valence


def training_block(items: list[dict[str, Any]], condition: str, rng: random.Random) -> tuple[str, list[dict[str, str]]]:
    ordered = list(items)
    rng.shuffle(ordered)
    if condition == "positive":
        valences = ["positive"] * 9 + ["negative"]
    else:
        valences = ["positive"] * 5 + ["negative"] * 5
    rng.shuffle(valences)
    labeled = [{"id": item["id"], "valence": valence, "stem": item["stem"], "resolution": item[valence]}
               for item, valence in zip(ordered, valences)]
    lines = ["Read the following completed situations carefully, in order. "
             "Each starts uncertain and is followed by what actually happened. "
             "Do not rate these examples; you will answer a separate rating task afterward."]
    for n, item in enumerate(labeled, 1):
        lines.append(f"{n}. {item['stem']} Resolution: {item['resolution']}")
    return "\n".join(lines), labeled


def validate(text: str, items: list[dict[str, Any]], x_valence: dict[str, str]) -> list[dict[str, Any]]:
    parsed = json.loads(text)
    ratings = parsed["ratings"]
    if not isinstance(ratings, list) or len(ratings) != len(items):
        raise ValueError("Incorrect number of ratings")
    expected = {x["id"] for x in items}
    returned = {x["id"] for x in ratings}
    if returned != expected or len(returned) != len(ratings):
        raise ValueError("Missing, repeated or unexpected item ID")
    normalized = []
    for entry in ratings:
        for key in ("x", "y"):
            value = entry[key]
            if type(value) is not int or not 0 <= value <= 4:
                raise ValueError(f"Out-of-range rating for {entry['id']} / {key}: {value}")
        neg = entry["x"] if x_valence[entry["id"]] == "negative" else entry["y"]
        benign = entry["y"] if x_valence[entry["id"]] == "negative" else entry["x"]
        normalized.append({"id": entry["id"], "negative": neg, "benign": benign})
    return normalized


def bias_score(ratings: list[dict[str, Any]]) -> float:
    return statistics.mean(r["negative"] - r["benign"] for r in ratings)


def mock_response(items: list[dict[str, Any]], rng: random.Random) -> str:
    # Pipeline sanity check only. Never use mock responses as LLM research evidence.
    return json.dumps({"ratings": [{"id": x["id"], "x": rng.randint(0, 4), "y": rng.randint(0, 4)} for x in items]})


def api_response(client: Any, model: str, messages: list[dict[str, str]]) -> str:
    response = client.responses.create(
        model=model,
        input=messages,
        text={"format": make_schema()},
        store=False,
        max_output_tokens=1400,
    )
    if not response.output_text:
        raise ValueError(f"Empty model output; status={response.status}")
    return response.output_text


def run_one(data: dict[str, Any], condition: str, participant: int, seed: int, mode: str,
            model: str | None, client: Any) -> dict[str, Any]:
    # Two folds, counterbalanced across independent virtual participants.
    local = random.Random(seed)
    fold = participant % 2
    a, b = data["assessment"][:6], data["assessment"][6:]
    pre, post = (a, b) if fold == 0 else (b, a)
    pre_prompt, pre_map = format_assessment(pre, local)
    train_text, exposures = training_block(data["training"], condition, local)
    post_prompt, post_map = format_assessment(post, local)
    msgs_pre = [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": "Baseline assessment (no feedback):\n" + pre_prompt}
    ]
    if mode == "mock":
        pre_raw = mock_response(pre, local)
    else:
        pre_raw = api_response(client, model, msgs_pre)
    pre_ratings = validate(pre_raw, pre, pre_map)
    # Retain previous responses as session history; treatment differs ONLY in its resolved endings.
    msgs_post = msgs_pre + [
        {"role": "assistant", "content": pre_raw},
        {"role": "user", "content": train_text},
        {"role": "user", "content": "Now rate these NEW, unresolved situations independently:\n" + post_prompt},
    ]
    if mode == "mock":
        post_raw = mock_response(post, local)
    else:
        post_raw = api_response(client, model, msgs_post)
    post_ratings = validate(post_raw, post, post_map)
    return {
        "condition": condition, "participant": participant, "seed": seed, "fold": "AB" if fold == 0 else "BA",
        "train_valences": [{"id": x["id"], "valence": x["valence"]} for x in exposures],
        "pre": pre_ratings, "post": post_ratings,
        "pre_bias": bias_score(pre_ratings), "post_bias": bias_score(post_ratings),
        "change": bias_score(post_ratings) - bias_score(pre_ratings),
        "mode": mode, "model": model if mode == "api" else "mock-not-an-LLM",
    }


def summarize(records: list[dict[str, Any]]) -> dict[str, Any]:
    by_group = {}
    for condition in CONDITIONS:
        group = [r for r in records if r["condition"] == condition]
        if not group:
            raise ValueError(f"No records for {condition}")
        by_group[condition] = {
            "n": len(group),
            "mean_pre_bias": statistics.mean(x["pre_bias"] for x in group),
            "mean_post_bias": statistics.mean(x["post_bias"] for x in group),
            "mean_change": statistics.mean(x["change"] for x in group),
        }
    diff = by_group["positive"]["mean_change"] - by_group["balanced"]["mean_change"]
    return {"conditions": by_group, "difference_in_differences": diff,
            "interpretation": "Synthetic pilot only; NOT an estimate of human behavioral fidelity."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("mock", "api"), default="mock")
    parser.add_argument("--model", help="API model name; required for --mode api")
    parser.add_argument("--confirm-api-cost", action="store_true", help="Explicitly permit billable API calls")
    parser.add_argument("--per-arm", type=int, default=2)
    parser.add_argument("--seed", type=int, default=20261014)
    parser.add_argument("--output-dir", type=Path, default=HERE / "results")
    args = parser.parse_args()
    if args.per_arm < 1:
        parser.error("--per-arm must be >= 1")
    if args.mode == "api" and (not args.model or not args.confirm_api_cost):
        parser.error("--mode api requires --model and --confirm-api-cost")
    client = None
    if args.mode == "api":
        if not os.environ.get("OPENAI_API_KEY"):
            parser.error("Set OPENAI_API_KEY before using --mode api")
        try:
            from openai import OpenAI
        except ImportError:
            parser.error("Install the OpenAI SDK first: python -m pip install -r requirements.txt")
        client = OpenAI()
    source = HERE / "stimuli.json"
    data = load_stimuli(source)
    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_name = f"{now}_{args.mode}_seed{args.seed}"
    folder = args.output_dir / run_name
    if folder.exists():
        parser.error(f"Output directory already exists: {folder}; rerun later or change --output-dir")
    folder.mkdir(parents=True)
    (folder / "manifest.json").write_text(json.dumps({
        "mode": args.mode, "model": args.model, "seed": args.seed, "per_arm": args.per_arm,
        "timestamp_utc": now,
        "stimuli_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "task": "Synthetic, CBM-I-inspired pilot; no human benchmark; no clinical inference",
        "training_arms": {"positive": "9/10 benign", "balanced": "5/10 benign"},
        "assessment": "12 original scenarios in AB/BA counterbalanced pre/post folds; 0..4 plausibility ratings",
    }, indent=2), encoding="utf-8")
    records = []
    try:
        for participant in range(args.per_arm):
            for condition in CONDITIONS:
                # Block paired arms on the same stimulus/option-order randomization.
                # Sessions stay independent; only the number of benign endings differs.
                seed = args.seed + participant * 157
                record = run_one(data, condition, participant, seed, args.mode, args.model, client)
                records.append(record)
                with (folder / "responses.jsonl").open("a", encoding="utf-8") as f:
                    f.write(json.dumps(record, ensure_ascii=False) + "\n")
                print(f"{condition:8} participant={participant:03} change={record['change']:+.3f}", flush=True)
        summary = summarize(records)
        (folder / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
        print("\nSummary: " + json.dumps(summary, indent=2))
        print(f"\nResults: {folder}")
        return 0
    except Exception as exc:
        # Already-completed trials are retained for audit; failed run has no summary.
        print(f"Run stopped; completed trials retained in {folder}: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
