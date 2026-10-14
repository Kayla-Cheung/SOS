# Anxiety Simulation Pilot — Execution Plan

**Objective:** A minimal human-grounded CBM-I behavioral fidelity experiment  
**Reference:** [MindTrails Managing Anxiety Study (R34)](https://github.com/TeachmanLab/MT-Data-ManagingAnxietyStudy-Cleaning)  
**Status:** Not started · 2026-10-14

**Scope:** One human experiment, **positive (90/10) vs balanced (50/50)** training, one LLM baseline, one prespecified interpretation-bias endpoint. No multi-agent environment, memory architecture, fine-tuning, or new human recruitment.

## Stage 0 — Synthetic Pilot: Start Now

A runnable pilot lives in [experiments/anxiety_fidelity_pilot](../experiments/anxiety_fidelity_pilot/). It does not depend on choosing a human dataset.

1. Run locally: `python pilot.py --mode mock --per-arm 2`; this tests the code only (fake random responses, **no LLM**).
2. Validate the tests: `python -m unittest discover -s tests -v`.
3. If desired, configure a private API key locally, inspect API pricing, and run `python pilot.py --mode api --model gpt-4.1-mini --per-arm 2 --confirm-api-cost` with the SDK installed. This makes 8 billable calls. Never commit the API key.
4. Examine `manifest.json`, `responses.jsonl` and `summary.json`. Fix parsing/experimental design problems before scaling.
5. Only after a good smoke test, consider `--per-arm 30` as an **exploratory** model-only run. No claims about human fidelity or clinical anxiety.

**Gate to Stage 1:** Pilot 0 is a software feasibility exercise; selecting and auditing real human data is a separate research requirement and can happen afterward.

## Stage 1 — Data and Protocol Audit (first priority)

Check the [public OSF data](https://osf.io/2x3jq/), [original OSF project](https://osf.io/3b67v/), and [cleaning documentation](https://github.com/TeachmanLab/MT-Data-ManagingAnxietyStudy-Cleaning).

- Download legally accessible files; record exact versions, column definitions, permissions and provenance.
- Inspect participant IDs, CBM and imagery-prime conditions, item-level **RR/BBSIQ**, time points and missingness.
- Find the **original training stimuli, assessment stimuli, instructions, item order and scoring rules**. Verify whether an LLM can complete the same task.
- Confirm the first **genuinely comparable pre/post** measurements in both training arms. Do not invent an immediate post-test or shorten a multi-session intervention and call it a replication.
- Review the reconstructed cleaning pipeline and any differences from the original publication.

**Deliverable:** `experiments/anxiety_fidelity_pilot/data_audit.md`, field inventory, and a documented **GO/NO-GO**.

**Hard gate:** Without sufficient item-level human observations **and** original task/intervention materials, do not run the matched intervention simulation. Seek legitimate access or switch to another anxiety-related experiment.

## Stage 2 — Human Benchmark

- Select one primary outcome (RR or BBSIQ, as justified by material availability) and one verified analysis window **before** viewing agent outputs.
- Restrict to positive and 50/50 training; consider a fixed imagery-prime subgroup only after checking cell sizes and comparability.
- Reproduce per-arm pre/post outcome summaries, missingness, and treatment-minus-control change, with uncertainty. Match official scoring definitions; R34 RR items use the **0–3** response range.
- Document discrepancies with published estimates and effects of missing measurements.

**Deliverable:** `prepare_human.py` plus `human_baseline.md` and reproducible non-sensitive summary tables.

## Stage 3 — Agent Baseline Pilot

- Implement exactly the verified experimental protocol in `run_agents.py` with standardized prompts and responses.
- Fix model/version, decoding, state reset, training/assessment separation and run logs.
- Start with a small smoke test (e.g., 2 trajectories/arm). If the protocol works, run approximately **30 independent trajectories per arm** as an exploratory pilot, subject to budget.
- Keep human answer data and model API secrets out of prompts and the public repository.

**Deliverable:** reproducible task engine, `config.yaml`, tests, and anonymized output summaries.

## Stage 4 — Fidelity Evaluation and Decision

Primary statistic, for the same validated endpoint:

```text
Delta = mean(post - pre | positive) - mean(post - pre | 50/50)
Main error = abs(Delta_agent - Delta_human)
```

Also evaluate item-level response distributions, across-trajectory variation, held-out items when available, and uncertainty via suitable resampling. Report design mismatches and prompt-demand effects.

**Deliverable:** `evaluate.py`, figures and `pilot_report.md`.

**Decision:** Either extend to another model/task, test one mechanistically motivated improvement, or stop/change the dataset. **Do not infer clinical efficacy or statistical equivalence from this pilot.**

## Planned Layout

```text
SOS/
  docs/
    RESEARCH_PLAN.md
    EXECUTION_PLAN.md
  experiments/
    anxiety_fidelity_pilot/
      README.md
      data_audit.md
      prepare_human.py
      run_agents.py
      evaluate.py
      config.yaml
      tests/
      results/
      data/        # local only; git-ignored
```

## First Working Session

**Do Stage 1 only:** verify the OSF data archive, inspect the RR/BBSIQ tables and experimental conditions, locate full stimulus materials, and issue a documented GO/NO-GO. **No LLM API calls yet.**
