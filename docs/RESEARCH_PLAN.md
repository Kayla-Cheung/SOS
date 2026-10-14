# SOS Research Plan

**Project:** SOS — Simulating On-campus Stress  
**Focus:** Human behavioral fidelity in anxiety-related cognitive experiments  
**Status:** Pre-experiment design · Updated 2026-10-14

## Research Goal

**Can LLM agents quantitatively reproduce human behavioral responses and intervention effects in anxiety-related cognitive tasks?**

The first study evaluates *interpretation bias* and its response to Cognitive Bias Modification for Interpretation (CBM-I). We care about response distributions, treatment-effect magnitudes, and transfer to untrained stimuli—not whether an LLM claims to feel anxious.

This is a **task-specific validity study**. Results cannot automatically establish clinical efficacy, human-like internal mechanisms, or validity for other populations.

## Human Reference

**Primary candidate: MindTrails Managing Anxiety Study (R34; Ji et al., 2021).** The original randomized study included 807 adults with elevated anxiety in its intent-to-treat sample, positive CBM-I training, balanced 50/50 training, and a no-training condition, crossed with imagery-prime conditions.

- [Original study](https://doi.org/10.1016/j.brat.2021.103864)
- [Research team's data reconstruction and cleaning documentation](https://github.com/TeachmanLab/MT-Data-ManagingAnxietyStudy-Cleaning)
- [Public OSF data component](https://osf.io/2x3jq/)
- [Original study OSF project](https://osf.io/3b67v/)

The cleaning team describes public item-level **BBSIQ** and **Recognition Ratings (RR)** data with measurement sessions and experimental conditions. **Original training/assessment materials, exact time-point comparability, and reproducible data download have not yet been independently verified.** The original final cleaning pipeline/data version is unavailable; a later reconstruction documents residual discrepancies.

## Minimal Experiment

1. **Verify feasibility:** Confirm human response tables, original stimuli and instructions, treatment schedules, outcome time points, scoring definitions, permissions, and missing-data patterns. Stop if a comparable intervention cannot be reconstructed.
2. **Reproduce the human result:** Compare **positive (90/10)** versus **balanced (50/50)** interpretation training under one consistently selected imagery-prime condition, if subgroup sizes permit. Predefine a primary interpretation-bias outcome (preferably RR if its materials and time points are available). Retain the study's actual measurement schedule.
3. **Run a baseline LLM:** Use **one fixed model**, independent simulated participants, and the verified human task protocol. Begin with a smoke test; an exploratory pilot might use 30 trajectories per arm. Do not introduce memory, fine-tuning, cognitive states, or multi-agent interaction.
4. **Compare humans and agents:** Compute the treatment-versus-control difference in pre/post change for each population; report their discrepancy, uncertainty, per-item distributions, variation, and held-out-stimulus generalization where supported.
5. **Consider improvements only after observing reproducible errors:** Test calibration, memory, cognitive-state modeling, or fine-tuning as separate follow-up hypotheses.

**Primary comparison (only with a verified shared pre/post endpoint):**

```text
Delta_H = (post - pre)_human,positive - (post - pre)_human,50/50
Delta_A = (post - pre)_agent,positive - (post - pre)_agent,50/50
Fidelity error = abs(Delta_A - Delta_H)
```

## Validity Rules

- Do not confuse textual anxiety induction with actual human anxiety or treatment.
- Match experimental materials, arm exposure, assessment schedule and scoring; document any irreducible differences.
- Prevent prompt leakage and using human test answers in agent inputs; keep training and assessment materials distinct.
- Consider participant attrition and sampling uncertainty. Similar mean effects do not guarantee human-like individual variation.
- Do not claim equivalence from an underpowered pilot or a nonsignificant difference.

## Immediate Next Step

Complete [the execution plan](EXECUTION_PLAN.md): **audit the R34 public data and original experimental materials**, then reproduce the human baseline before any LLM runs.

**Not yet completed:** Dataset audit, human baseline reproduction, agent runs, and fidelity results. Population-specific or longitudinal SOS simulation is future work, not part of this pilot.
