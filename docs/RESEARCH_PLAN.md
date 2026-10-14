# SOS Research Plan

**Project:** SOS — Simulating On-campus Stress  
**Stage:** Anxiety simulation validity (pre-experiment)  
**Updated:** 2026-10-14

## Goal

Before using SOS to study campus stress and anxiety, test a narrower prerequisite:

> **Can an LLM agent reproduce human changes in anxiety-related interpretation bias under comparable experimental conditions?**

The target is **task-specific human behavioral fidelity**, not an assertion that an LLM experiences anxiety, has human psychological mechanisms, or can replace clinical participants.

## Primary Human Reference

**MindTrails Managing Anxiety Study (R34; Ji et al., 2021)**: 807 adults with elevated anxiety in a randomized CBM-I trial. The original design included positive interpretation training (**90% positive / 10% negative**), balanced training (**50% / 50%**), and no training, crossed with anxious or neutral imagery primes.

- [Human study](https://doi.org/10.1016/j.brat.2021.103864)
- [Official reconstruction and cleaning documentation](https://github.com/TeachmanLab/MT-Data-ManagingAnxietyStudy-Cleaning)
- [Public OSF component](https://osf.io/2x3jq/)
- [Original paper's OSF project](https://osf.io/3b67v/)

The cleaning repository documents a public dataset with **item-level BBSIQ and Recognition Ratings (RR)**, time points, and randomized conditions. **We have not yet independently verified the downloadable files, original stimuli, complete trial sequences, or available matched assessment time points.** The reconstruction uses multiple historical raw-data versions, so all data and scoring discrepancies must be logged.

## Minimal Experiment

**Question:** Does a baseline LLM reproduce the human difference in *interpretation-bias change* between positive and 50/50 CBM-I training?

1. **Audit data and protocol.** Verify the participant-level tables, item-level scoring, stimulus text/materials, trial order, training procedure, assessment schedule, reuse permissions, and missing-data patterns. Confirm the exact 90/10 and 50/50 conditions and neutral-prime subset.
2. **Reproduce the human benchmark.** Recompute the original bias measures using the official scoring definitions. Choose **one primary behavioral endpoint** (RR or BBSIQ) and the earliest *verified common pre/post measurement* for both arms. Report sample sizes and missingness at each time point. Do not invent an immediate post-test if none exists.
3. **Run a minimal LLM baseline.** One fixed model, two training arms, independent agent sessions, matched instructions and available stimuli. The agent sees no withheld human responses and is scored with the same verified procedure. Start with a small smoke test, then approximately 30 simulated trajectories per arm as an exploratory pilot (not a powered equivalence study).
4. **Evaluate fidelity.** Compare the human and agent **difference-in-differences** in bias scores, plus item/response distributions, simulated-subject variability, and performance on available unseen evaluation stimuli. Report uncertainty and a human–human reference split. Do not use statistical nonsignificance as evidence of equivalence.
5. **Decide on an extension.** Only after a reproducible mismatch is observed should we test memory, calibrated sampling, cognitive-state modeling, or LoRA fine-tuning against this baseline.

## Go / No-Go Rule

**Do not run the intervention simulation** unless the human stimuli, task sequence, scoring rules, intervention arms, and comparable outcomes can be independently reconstructed. If stimulus materials are unavailable, publish an honest feasibility audit or switch to another open anxiety-related cognitive experiment; do not create substitute stimuli and describe the result as a faithful replication.

## Interpretation and Safeguards

- The human study involved real people, repeated sessions, and high attrition. Text-based LLM prompting is not the same intervention or clinical outcome.
- A matching average effect is insufficient if choice distributions, between-subject variation, or held-out behavior diverge.
- Control prompt demand effects, contamination, model settings, test leakage, and possible changes in simulated participant identity.
- Keep identifiable or restricted participant data, raw model logs with sensitive content, and API keys out of the public repository.

## Status and Immediate Next Step

**Completed:** Research question, literature reconnaissance, candidate study and experimental outline.  
**Pending:** OSF data audit, reconstruction of stimulus/protocol, human baseline, runnable agent experiment, and all analyses.

**Next:** Complete [the execution plan](EXECUTION_PLAN.md), beginning with the dataset and materials audit. No mechanism development or SOS integration is scheduled yet.
