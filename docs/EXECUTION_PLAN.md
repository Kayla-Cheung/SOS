# SOS — Chinese High-School Behavioral Fidelity: Execution Plan

**Version:** 2026-10-14  
**Target:** Ordinary mainland Chinese senior-high students; academic and peer-evaluation stress contexts.  
**Status:** Preparation only; no claimed completed dataset audit or experiment.

This replaces the adult R34 intervention-first plan. There are **two independent evidence tracks**: (A) a reproducible adolescent methods pipeline using an open human dataset, and (B) Chinese high-school population validation. **Only Track B can support claims about the target population.**

## Gate 0 — Evidence and Data Audit (start now; ~3–7 working days)

**China-first search and contact:**

- [Lu et al., 2007](https://doi.org/10.1080/15374410701776301): determine whether the high-school subset of 1,004 pupils can be identified and whether per-scenario responses and stimuli are available.
- [Fu et al., 2015](https://doi.org/10.1891/0889-8391.29.3.253): request full Chinese scenarios, instructions, participant-level outcomes, age/grade distribution, intervention and control procedures.
- [Fu et al., 2013](https://doi.org/10.1016/j.dcn.2012.11.003): check the Chinese scenario materials and clinical sample restrictions.
- [Bai et al., 2025](https://doi.org/10.1002/pits.23570): inspect the test-anxiety interpretation measure and whether participant/item-level data can be requested; **mean age 12.27 means this is not a senior-high reference sample**.

**Methodological open-data track:**

- Audit [de Voogd et al., 2018](https://doi.org/10.1371/journal.pone.0194274) and its [OSF repository](https://osf.io/bx2hd/). A published OSF link is **not verification** that the original per-trial stimuli, responses, and training materials can all be retrieved.
- As needed, audit [de Voogd et al., 2017](https://doi.org/10.1371/journal.pone.0181147) and [its OSF page](https://osf.io/4gtmh/).
- Record archival provenance, files, variables, study population, trial materials, conditions, outcome timepoints, missingness, reuse restrictions and accessibility failures.
- Keep the US adult [MindTrails R34](https://github.com/TeachmanLab/MT-Data-ManagingAnxietyStudy-Cleaning) as an optional script/data-format sanity check, not a primary behavioral reference.

**Deliverable:** `experiments/high_school_fidelity/data_audit.md` with source-by-source **AVAILABLE / REQUESTED / MISSING** status and two separate GO/NO-GO decisions:

- **Gate A:** complete matching adolescent human task and response data available for pipeline reproduction?
- **Gate B:** comparable **Chinese senior-high** item-level responses and original stimuli available for target-population validation?

Do **not** run any agents just because a paper reports group means.

## Stage 1A — Build a Reproducible Adolescent Pipeline (conditional; ~1 week)

If Gate A passes, select **one** precisely documented Dutch adolescent experiment. Reproduce its human analyses and then implement one fixed LLM with exactly that study's tasks and scoring.

For de Voogd 2018, preserve **CBM-I vs neutral-placebo**, **eight sessions** and original assessment protocol. Do not substitute the adult R34 positive-vs-50/50 conditions or invent an immediate post-test. A shortened version is an **exploratory new protocol**, not a direct human intervention replication.

**Deliverables:** `prepare_human.py`, human score verification, `run_agents.py`, configuration/seed/prompt logging, minimal `evaluate.py`.

**Outcome:** tested reproducibility infrastructure, **not** evidence that Chinese high-school behaviors are faithfully simulated.

## Stage 1B — Chinese High-School Reference (primary scientific gate)

If existing Chinese senior-high item-level data and original scenarios can be obtained, use them with the required access agreements.

**If not available:** discuss a new data collection with an experimental/developmental psychology collaborator; obtain institutional ethics approval, school permission, guardian permission where required and student assent **before** recruitment. Begin with a small **item-comprehension pilot** to validate clear, age-appropriate, low-risk Chinese academic stress vignettes, not a CBM-I treatment.

Candidate vignette domains: exam outcomes, teacher feedback, class rankings, family expectations, peer comparisons. For each, write threat and non-threat interpretations without making one answer obviously correct. Blind-review ambiguity/clarity and avoid distressing or diagnostic stimuli.

**Measurement:** a fixed forced-choice or ordinal interpretation task, with demographic/grade variables kept minimal, optional validated test-anxiety instruments under an approved protocol, and separate evaluation items. A small item pilot is for readability/feasibility, **not** for proving fidelity.

**Deliverables:** approved protocol (if recruiting), scenario bank with permissions, scoring rubric, anonymized participant × item behavioral table, consent/data governance notes.

**Gate B:** matching Chinese-high-school human reference confirmed; otherwise stop at a methods pilot and report the external-validity limitation.

## Stage 2 — Human–Agent Baseline Fidelity (after Gate B; ~1 week)

- One fixed model and one standardized Chinese prompt. No anxiety role-play, explicit target distribution, memory system, GOSI, or fine-tuning.
- Present **identical Chinese vignettes** and answer formats to the humans and the LLM; do not disclose human choices to the LLM.
- Predefine analysis and held-out items. Separate person-level and item-level uncertainty; compare response distributions, negative interpretations, between-person heterogeneity and held-out generalization.
- Include a human–human split benchmark and perturbation/neutral-control checks. A few dozen LLM samples per condition are a pipeline pilot, **not** proof of equivalence or human-like individuality.

**Deliverables:** `pilot_report.md`, analysis scripts, plots and a transparent limitations section.

## Stage 3 — Intervention Fidelity (optional, later)

Only pursue if there is a **matched Chinese** CBM-I RCT dataset with verified task, treatment/control exposure and pre/post interpretation-bias outcomes, or an independently approved new intervention study.

Primary contrast: difference in pre/post changes between treatment and control for humans and agents. Test effect magnitude, distributions, generalization, attrition differences, and prompt-demand artifacts. Do not report clinical benefit from LLM results.

**Deliverable:** separate intervention protocol and preregistered analysis; *not* part of the current minimal pilot.

## Stage 4 — Model Improvements (conditional)

Only after a reliable behavioral gap is established, compare calibration, explicit cognitive-state dynamics, bounded/episodic memory, or LoRA under equal human data access and held-out evaluation.

## Planned Repository Layout

```text
SOS/
  docs/
    RESEARCH_PLAN.md
    EXECUTION_PLAN.md
  experiments/
    high_school_fidelity/
      README.md
      data_audit.md
      prepare_human.py
      run_agents.py
      evaluate.py
      config.yaml
      tests/
      results/
      data/       # local/private; never commit sensitive human data
```

## Next Session — Exact Task

1. Read and catalogue the four China-relevant studies above; create a table of age/grade, task, stimuli, response accessibility and author contact.
2. Inspect the Dutch adolescent OSF file manifest; **do not assume the stimuli are in the archive**.
3. Write a factual `data_audit.md` with data access blockers and evidence links.
4. Decide whether to proceed with Stage 1A while contacting Chinese authors, or whether existing Chinese data enable Stage 1B directly.

**Hard stop:** No claims of Chinese high-school behavioral validity without a genuine Chinese high-school human reference; no study involving minors without prior ethics and permissions.
