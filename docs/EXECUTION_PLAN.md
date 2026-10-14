# Anxiety Simulation Pilot — Execution Plan

**Status:** Not started  
**Human reference:** MindTrails Managing Anxiety Study (R34; Ji et al., 2021)  
**Scope:** One anxiety-related interpretation-bias task, two CBM-I training arms, one baseline LLM. No SOS engine, multi-agent simulation, memory architecture, or fine-tuning in the pilot.

This is a proposed **four-stage execution sequence**, not a claim that the necessary data or stimuli have already been obtained. Approximate effort is a planning aid, not a deadline.

## Stage 1 — Dataset and Protocol Audit (first priority; ~1 week)

**Sources:** [Official cleaning repository](https://github.com/TeachmanLab/MT-Data-ManagingAnxietyStudy-Cleaning), [OSF public component](https://osf.io/2x3jq/), [Ji et al. (2021)](https://doi.org/10.1016/j.brat.2021.103864).

Tasks:

- Retrieve the official data manifest/codebook and lawful public files; record file versions, SHA-256 checksums, licensing/access restrictions, and missing files. Do not redistribute restricted data.
- Inspect participant, condition, BBSIQ and RR tables; identify participant IDs, session/timepoint identifiers, item columns, missingness, and scoring rules.
- Locate exact **training stimuli, assessment stimuli, instructions, presentation order, feedback/comprehension prompts**, and which versions are permitted to be reused.
- Confirm experimental design: positive (90/10) versus balanced (50/50) training, neutral imagery prime, number of trials per session, and timing of each outcome measure.
- Check whether a comparable pre/post pair and an adequate human sample exist within the intended comparison. Distinguish the 807-person ITT cohort from the smaller analyzable subset.
- Read the team's notes on reconstruction from raw Sets A/B and list discrepancies with the original paper's values.

**Deliverables:** `experiments/anxiety_fidelity_pilot/data_audit.md`, source inventory, data dictionary, explicit **GO / NO-GO** decision.

**Gate:** Proceed to an intervention simulation only if required materials and comparable measurements are verified. Otherwise stop, request materials through legitimate channels, or select a different open anxiety experiment.

## Stage 2 — Reproduce Human Baseline (~1 week)

- Process only the approved public files in a local, Git-ignored data directory.
- Filter conditions with clear, reproducible criteria. Verify actual sample sizes, missingness, and treatment balance before analysis.
- Use the official scoring definitions; RR ratings are coded **0–3 in this R34 study** (not 1–4 as in a separate Calm Thinking study).
- Choose the **primary outcome and measurement window before reviewing agent results**; favor a behavioral interpretation-bias measure, not a general anxiety questionnaire as the sole outcome.
- Reproduce human condition-specific means and the treatment-by-time interaction or difference-in-differences; reconcile discrepancies with the original analysis, documenting any unavoidable differences.
- Preserve original design complexity and attrition in the audit. If a neutral-prime-only subgroup is too small or incomparable, reconsider the restriction before running agents.

**Deliverables:** `prepare_human.py`, `human_baseline.md`, cleaned non-sensitive derived metrics, minimal automated tests.

**Gate:** Human outcome estimates and analytic population are understood and independently reproducible.

## Stage 3 — Minimal Agent Experiment (~1 week, only after Gates 1–2)

- Implement stimulus presentation, response validation, feedback, and logging; no answer leakage from human trials.
- Fix model/provider/version, prompt text, decoding settings and sampling configuration. Store prompt/config hashes and anonymized trajectory IDs.
- Use exactly two conditions: **POSITIVE** and **FIFTY_FIFTY**; preserve the chosen prime condition and verified measurement schedule.
- Run a tiny smoke test first (for example 2 trajectories per arm) to ensure outcome reconstruction works. Then run an exploratory pilot of roughly **30 independent trajectories per arm**, subject to a recorded API budget.
- Separate training items from held-out assessment items; log all model outputs and parsing failures. If exact original stimuli cannot be used, do not label the experiment a direct human replication.

**Deliverables:** `run_agents.py`, `config.yaml`, protocol tests, trajectory summaries and run log. Keep sensitive/raw files and secrets out of Git.

**Gate:** Agent outputs can be scored by the same measurement procedure as human outputs, with all experiment conditions and costs traceable.

## Stage 4 — Fidelity Report and Research Decision (~1 week)

**Prespecified primary quantity** (for the verified outcome `Y`):

\[
\Delta_H = (\bar Y_{post}-\bar Y_{pre})_{H,positive}-(\bar Y_{post}-\bar Y_{pre})_{H,50/50}
\]

\[
\Delta_A = (\bar Y_{post}-\bar Y_{pre})_{A,positive}-(\bar Y_{post}-\bar Y_{pre})_{A,50/50}
\]

\[
\mathrm{Fidelity\ Error}=|\Delta_A-\Delta_H|
\]

- Report uncertainty, missingness, response distributions, between-trajectory variability, and human–human reference variation.
- Document non-comparable aspects (e.g. real-life human training duration vs LLM text exposure) and demand-characteristic risks.
- Make one evidence-based decision: **extend** to another model or held-out task; **test a mechanism** targeting an observed bias; or **stop/change dataset**.
- Do not claim equivalence or clinical efficacy from this exploratory sample.

**Deliverables:** `evaluate.py`, `results/pilot_report.md`, reproducible figures/tables and a concise conclusion with limitations.

## Repository Layout (planned, not yet created)

```text
SOS/
  docs/
    RESEARCH_PLAN.md
    EXECUTION_PLAN.md
  experiments/
    anxiety_fidelity_pilot/
      README.md
      data_audit.md
      config.yaml
      prepare_human.py
      run_agents.py
      evaluate.py
      tests/
      results/
      data/          # local only; add to .gitignore before use
```

## First Working Session — Concrete Next Actions

1. Confirm the R34 official OSF `public-v1.0.0.zip` manifest can be accessed and inspected.
2. Create a field inventory for `participant`, `bbsiq`, and `rr`, including item-level and timepoint availability.
3. Locate the actual training and assessment stimulus texts or record their absence.
4. Write `data_audit.md` with evidence links and the next GO / NO-GO decision.

**Do not start LLM API calls or agent architecture work in this session.**
