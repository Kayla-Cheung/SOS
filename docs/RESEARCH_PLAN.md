# SOS Research Plan

**Project:** SOS — Simulating On-campus Stress  
**Status:** Preliminary research / experiment design  
**Updated:** 2026-10-14

## Research Goal

Before developing SOS as a simulation of campus stress and anxiety, we need to test a fundamental assumption:

> **Can LLM agents reproduce human behavioral responses in anxiety-related psychological experiments?**

This study evaluates **human behavioral fidelity**, not whether LLMs experience anxiety. A positive result would support simulation validity for specific experimental tasks, not the general replacement of human participants.

## Research Questions

1. **Behavioral fidelity:** Do agent response distributions resemble those of human participants?
2. **Intervention fidelity:** Can agents reproduce the direction *and magnitude* of human behavioral changes after anxiety-related cognitive interventions?
3. **Generalization:** Do observed effects transfer to unseen scenarios rather than merely following task instructions?
4. **Potential extension:** If systematic gaps exist, can memory or structured cognitive mechanisms reduce them?

## Human Data Candidates

**Primary target: Cognitive Bias Modification for Interpretation (CBM-I)** — experiments measuring interpretations of ambiguous situations before and after training.

- [MindTrails / Calm Thinking data and cleaning code](https://github.com/TeachmanLab/MT-Data-CalmThinkingStudy)
- [MindTrails OSF resources](https://osf.io/s8v3h/)
- [Abado et al. (2026), CBM-I study](https://doi.org/10.1038/s41398-026-04122-2)

**Data availability is not yet confirmed.** Before implementation, verify access to original stimuli, trial-level human responses, experimental groups, scoring rules, and pre/post measurements.

## Experimental Workflow

1. **Audit data:** Select one human study whose experimental conditions, stimuli, and responses can be reproduced.
2. **Rebuild the human baseline:** Clean and reconstruct the task; verify reported behavioral measures and treatment–control differences.
3. **Run baseline agents:** Use a fixed LLM with standardized prompts and independent sessions. Replicate accessible task conditions without showing agents withheld human answers. Keep training and evaluation stimuli separate.
4. **Compare fidelity:** Measure response-distribution differences, pre/post and treatment–control effect-size errors, generalization to held-out stimuli, and variability across simulated participants. Use human–human comparisons and uncertainty intervals as reference points.
5. **Investigate failures:** Only if consistent mismatches are found, test targeted improvements such as episodic memory or structured decision-making against the same human benchmarks.

## Validity Requirements

- Text prompts are **not equivalent** to real human anxiety induction or clinical intervention.
- Similar average scores do not imply similar individual variability or psychological mechanisms.
- Control for prompt leakage, task contamination, model settings, and possible drift between simulated conditions.
- Do not interpret nonsignificant differences as proof of equivalence; define acceptable errors in advance.

## Current Status and Next Step

**Completed:** Initial literature review, research objective, candidate datasets, and a conceptual evaluation protocol.  
**Not yet completed:** Dataset verification, runnable experiment, or human–agent evaluation.

**Next step:** Verify whether MindTrails or another CBM-I dataset contains enough accessible trial-level data and experimental materials for a faithful replication. If not, choose another anxiety-related cognitive task before building agents.
