# SOS Research Plan

**Project:** SOS — Simulating On-campus Stress  
**Target population:** Students in mainland Chinese senior high schools (roughly ages 15–18; grades 10–12)  
**Stage:** Human-grounded behavioral validation, before SOS implementation  
**Updated:** 2026-10-14

## Research Goal

**When can LLM agents reproduce Chinese high-school students' behavioral responses to ambiguous academic and interpersonal stressors?**

Begin with *threat-related interpretation bias* in situations involving examinations, teacher feedback, grades, parents' expectations, and peer comparison. Evaluate agreement with real students' response distributions and between-student variation. Study cognitive-bias-modification (CBM-I) intervention effects **only when a matched human intervention dataset and complete protocol are available**.

We are validating **task-specific behavioral fidelity**, not claiming that models experience anxiety, reproduce human mental mechanisms, or predict clinical treatment outcomes.

## Human Evidence: Revised Priorities

| Evidence source | Why relevant | Data status and limitations |
| --- | --- | --- |
| [Lu et al. (2007), Chinese pupils' threat perception](https://doi.org/10.1080/15374410701776301) | 1,004 Chinese students aged 9–19, including high-school students; ambiguous stories and behavioral responses | High-school subgroup and item-level data **not yet verified as accessible** |
| [Fu et al. (2015), Chinese adolescent CBM-I](https://doi.org/10.1891/0889-8391.29.3.253) | 77 Chinese adolescents, positive vs control interpretation training | Full stimuli, response-level data and participant age/grade breakdown **not yet confirmed** |
| [Fu et al. (2013), Chinese adolescent CBM-I](https://doi.org/10.1016/j.dcn.2012.11.003) | 28 Chinese adolescents with anxiety disorders; 60 ambiguous scenarios, including school/social contexts | Small clinical sample, not representative of ordinary high-school students; raw data access unverified |
| [Bai et al. (2025), test anxiety and interpretation bias](https://doi.org/10.1002/pits.23570) | 1,210 Chinese adolescents; relevant construct and school-stress scenarios | Mean age 12.27, generally younger than target; item data access unverified |
| [de Voogd et al. (2018), adolescent CBM-I RCT](https://doi.org/10.1371/journal.pone.0194274) | 173 Dutch adolescents, mean age 14.35; eight training sessions, active vs placebo conditions | [OSF data referenced by paper](https://osf.io/bx2hd/); file contents and exact stimulus availability **not independently audited** |
| [MindTrails Managing Anxiety (R34)](https://github.com/TeachmanLab/MT-Data-ManagingAnxietyStudy-Cleaning) | Existing data-processing benchmark | US adults with elevated anxiety; **not the main population-validity benchmark** |

**Decision:** Prioritize existing Chinese adolescent evidence and request stimulus-level data from study teams. In parallel, audit the accessible Dutch adolescent dataset **only to establish the experimental/analysis pipeline**. Do not treat Dutch adolescent results as evidence about Chinese senior-high students.

## Minimal Research Sequence

### Experiment A — Replication Pipeline (non-Chinese adolescents)

**Only if original stimuli and human item-level outcomes are obtainable:** Reconstruct the 2018 adolescent interpretation-bias task, including its **positive training versus neutral-placebo** conditions, full intervention schedule, recognition assessment, and human baseline. Compare one fixed LLM with human results using identical verified scoring.

This is a reproducibility/methods pilot, **not the SOS target-population validation**. Do not import the adult R34 90/10-vs-50/50 design into this different study.

### Experiment B — Primary SOS Behavioral Fidelity Test (Chinese high-school students)

**Primary task:** Chinese-language academic/social ambiguous scenarios with two or more defensible interpretations and a prespecified choice/rating format.

1. Obtain a Chinese high-school participant dataset with original stimuli and individual responses (existing dataset preferred; ethics-approved new data only if necessary).
2. Verify age/grade, context relevance, language, item comprehension and scoring. Avoid assuming that translated Dutch/English items are culturally equivalent.
3. Run a fixed baseline LLM on the **same Chinese items**. Simulated participants are independently initialized; prompts must not explicitly instruct them to choose threatening interpretations.
4. Compare **per-item choice distributions, negative-interpretation rate, variation, and held-out-item generalization** with Chinese human reference data. Keep calibration/training data and evaluation items separate. Report uncertainty and a human–human split benchmark.

**Go/no-go:** Without verified Chinese participant responses on comparable stimuli, any result is an exploratory demonstration, **not validation for Chinese high-school students**.

### Experiment C — Conditional Intervention Fidelity

Only if an existing Chinese adolescent/high-school intervention dataset has matching pre/post outcomes and materials, or after a separately ethics-approved study, compare human and LLM **treatment-minus-control change**. Match treatment, control, exposure, measurement timing, attrition and scoring. Do not infer an anxiety treatment effect merely from a change in model-generated language.

## Follow-up Mechanisms (not in first baseline)

If Experiment B exposes robust and interpretable errors, compare probability calibration, cognitive-state modeling, episodic memory and/or LoRA fine-tuning **on held-out data**, with matched human-data budgets. Do not build a complex SOS architecture before validation.

## Ethical and Methodological Guardrails

- Ordinary senior-high pupils ≠ younger middle-school children ≠ clinically diagnosed adolescent patients; record subgroup differences explicitly.
- Recruitment of minors requires institutional ethics approval, school coordination, appropriate guardian permission and student assent; data should be minimized, de-identified, access-controlled and not published as raw sensitive responses.
- Prefer low-risk, non-diagnostic interpretation tasks before any intervention. Avoid inducing acute distress, high-stakes labeling, or unreviewed clinical claims.
- LLM trajectories are not automatically independent human-like individuals. Report prompt sensitivity, sampling settings and contamination risk.
- A fit to one group or task does not validate longitudinal anxiety dynamics, peer effects or the whole SOS framework.

## Current Status

**Verified from publications:** Relevant Chinese adolescent studies exist; the 2018 Dutch adolescent RCT reports an OSF repository; the earlier R34 data are adult data.  
**Unverified:** Chinese participant-level data access, complete original stimuli, adolescent OSF archive contents, and any matched Chinese high-school intervention dataset.  
**No experiments have yet been run.**

**Next action:** Follow [EXECUTION_PLAN.md](EXECUTION_PLAN.md): first audit data availability and contact the Chinese study teams, while inspecting adolescent OSF materials for an independent pipeline pilot.
