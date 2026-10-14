# SOS Research Plan — Phase 1 CBM-I Behavioural Fidelity

**Project:** SOS — Simulating On-campus Stress  
**Version:** Revised protocol draft, 2026-10-14  
**Status:** Ready for data audit; not yet preregistered or ready for confirmatory execution  
**Original:** RESEARCH_PLAN.md remains unchanged. This document supersedes its conceptual design for Phase 1 only.

## 1. Aim and permitted conclusions

Test whether a frozen LLM-agent configuration reproduces human interpretation-task responses and CBM-I training effects in one reproducible human experiment. Evaluate output fidelity, not experienced anxiety, clinical efficacy, or shared psychological mechanisms.

The target population is the selected study's actual sample. Adult findings cannot establish validity for Chinese boarding-school adolescents. Phase 1 validates a possible interpretation-processing component of SOS; it does not validate cumulative stress, help-seeking, institutional interventions, or a whole school simulation.

## 2. Research questions and outcome hierarchy

1. **Response fidelity:** Does the agent reproduce human item-level response probabilities and aggregate response distributions within prespecified tolerances?
2. **Training-effect fidelity (primary):** Is the difference between agent and human treatment-versus-control changes small enough to meet a prespecified equivalence margin?
3. **Generalization:** Does fidelity persist on stimulus themes withheld from configuration development and, where available, a separate task or human sample?
4. **Exploratory extension:** Can a targeted memory or decision module improve independent validation performance beyond the frozen baseline and simple statistical comparators?

Select exactly one primary interpretation task, one scoring rule, one post-training endpoint, and one randomized contrast after the audit. Anxiety questionnaires are secondary human outcomes; agent questionnaire outputs are descriptive language responses, not validated measurements of agent anxiety. Training accuracy is a manipulation/process measure, not the primary fidelity endpoint. API latency is not human reaction time.

## 3. Candidate studies and selection

- [MindTrails Calm Thinking cleaning repository and data documentation](https://github.com/TeachmanLab/MT-Data-CalmThinkingStudy); [original candidate OSF link](https://osf.io/s8v3h/). Official documentation describes an adult sequential multiple assignment randomized trial, with public and private data components and redacted free-text fields. Do not assume the GitHub repository contains complete response data or that a simple two-arm analysis is appropriate.
- [Abado et al. (2026), multi-session CBM-I for social anxiety](https://doi.org/10.1038/s41398-026-04122-2); [full text and availability statement](https://pmc.ncbi.nlm.nih.gov/articles/PMC13197415/). The paper reports anonymized data and pipelines on OSF. Actual file access, stimulus completeness, and trial-level coverage remain to be audited.

Prefer the candidate with a clearly identifiable randomized active-versus-control contrast, recoverable assessment trials, and complete task materials. Dataset size alone is not a selection criterion. If MindTrails is selected, identify one valid randomized stage and its eligible population; do not collapse later adaptive assignments or coaching into a conventional two-arm contrast. Otherwise a design-specific analysis must be specified before execution.

## 4. Data audit: mandatory entry gate

Create an audit record with filenames, version/commit, access date, checksums, variable mapping, redaction notes, and a decision for each requirement below. Documentation claims are distinguished from inspected files.

| Requirement | Pass evidence | Consequence if unavailable |
|---|---|---|
| Access and reuse | Files readable; dataset/material permissions documented | Do not run the affected replication; request access or select another source |
| Population | Eligibility, recruitment, demographics, baseline measures and exclusions recoverable | Restrict claims to documented characteristics; unresolved eligibility blocks confirmatory use |
| Trial linkage | Stable participant ID, assessment time, item ID/text/version, response, and condition linkable | Aggregate-only data cannot support item-level fidelity |
| Experimental contrast | Randomization, control content, assignment timing, eligibility and relevant probabilities documented | No causal training-effect claim until reconstructed |
| Materials | Instructions, stimuli, answer options, feedback, scoring keys, presentation/order rules and training dose recoverable | Record adaptation; missing essential materials blocks faithful replication |
| Time and exposure | Pre/post endpoint, session order, completion and dose identifiable | Limit to recoverable endpoint/contrast; no invented exposure histories |
| Missingness | Dropout, absent trials, redacted fields and invalid records distinguishable | Specify estimand and sensitivity analyses; do not silently drop cases |
| Human reconstruction | Selected descriptive statistics and primary contrast reproduced from inspected data | Resolve discrepancies before agent evaluation |

Reconstruction passes when differences are explained by published rounding or a documented analysis choice, with matching sample counts and scoring. Record expected tolerances before checking numerical results; do not choose a tolerance to hide a discrepancy.

**Gate A:** Full trial-level replication is feasible. Proceed to protocol freeze.  
**Gate B:** Only aggregate replication is feasible. Rewrite scope and outcomes before proceeding; do not retain claims about item-level or individual fidelity.  
**Gate C:** Essential materials, assignment or scores cannot be reconstructed. Change source/task before developing agents.

Deliverables: audit table, data dictionary, participant/trial flow diagram, reconstruction report, and selected study/contrast rationale. No participant data are uploaded to an external model without documented permission for that use.

## 5. Development, validation and final test separation

Partition participants within randomized arms and split assessment items by semantic theme before agent development. Use a documented deterministic allocation and inspect whether enough participants and themes remain for estimation. Exact fractions are chosen from audit-based precision simulations and frozen before fitting agent configurations.

- **Development:** Human data and tasks may inform configuration selection and simple comparator fitting.
- **Validation:** Used for a bounded, logged selection among prespecified candidates.
- **Final test:** Human answers and reported target estimates are inaccessible to configuration development. Evaluate once after freezing. Changes after inspection constitute a new exploratory version and require a new independent test for confirmation.

Where sample size or item coverage makes simultaneous participant/theme holdout infeasible, use one prespecified holdout axis and label the other generalization claim untested. Researcher knowledge of published overall effects cannot be erased; log it as a limitation. Held-out public materials are not necessarily absent from model pretraining.

Assessment themes withheld from development need corresponding human responses. New or translated items without human data are robustness probes only, not fidelity validation. Do not remove original training content merely to create a holdout if that changes the treatment; select genuinely novel assessment themes or label overlap and the narrower transfer claim.

## 6. Experimental conditions and agent identity

### Primary arms

Reproduce the selected human study's active CBM-I and actual control condition. Match instructions, training opportunities, response options, feedback, and assessment structure where text-compatible. List every adaptation, including omitted imagery, timing, sensory or physiological components. Do not add a negative-training arm unless it exists in the selected contrast.

Each simulated participant follows: **pre-assessment → assigned training/control → post-assessment**. Participants are isolated from one another. Within each participant, preserve chronological experience under a frozen memory rule. Starting a new independent model session for every assessment trial is not the main longitudinal agent condition.

### Baseline agent

- One fixed model/version and participant-facing prompt; no browsing, retrieval, tools or access to benchmark answers.
- One chronological transcript per participant, containing only instructions, presented stimuli, that participant's outputs and supplied experimental feedback.
- Record whether earlier assessment answers remain visible. Use the original task's feedback rule; never provide scoring keys during assessment.
- Use full transcript retention only if the maximum protocol fits the context budget without truncation. Otherwise specify and freeze a retention mechanism before running; report that it changes accessible experience.
- Do not instruct the agent that it should improve, be anxious, or choose negative interpretations. Participant covariates, if used, are restricted to a documented baseline set and never include target item answers or future trajectories.
- The initial primary configuration uses no invented persona distribution. A fixed prompt with stochastic repetitions can test aggregate output fidelity, but cannot alone establish stable person-level heterogeneity. Covariate-conditioned personas are a separately specified extension.

The term **simulated participant** denotes an operational run, not a biologically independent person. Repeated runs from one persona/configuration are nested replicates. Agent pre/post observations share an identity; separate treatment arms use isolated histories. Interleave arm execution in randomized batches to reduce date or service-version confounding.

### Comparators and diagnostic conditions

Fit a pooled response-probability comparator and a simple item/covariate model using development data only. Report whether the agent improves final-test predictive fidelity over these comparators. A fresh-context/no-retained-training diagnostic may test context dependence, but is not the primary human-equivalent condition. Additional models, prompts and memory mechanisms are exploratory unless independently preregistered.

## 7. Run manifest and output handling

Freeze provider, exact model identifier/snapshot where available, system/user templates, temperature and other sampling settings, maximum output length, memory rule, item order randomization, software version, run dates and seeds where supported. Do not assume a seed guarantees determinism. Archive the manifest and full permitted trial logs.

Use structured output matching the human response scale. Allow at most one format-only repair request for an invalid response; it must not reveal a desired answer. Log the original, repair and failures. Service errors may be retried with the identical request up to two times. Refusals and task-invalid answers are outcomes to report, not silently replaced trials. Freeze these rules and report failure rates by arm/time. Detect version changes; affected batches are separated or rerun under the frozen configuration before opening final targets.

## 8. Statistical analysis

### Primary estimand and equivalence

For source s (human or agent), define on the original score scale:

`Delta_s = (post - pre)_active,s - (post - pre)_control,s`

The primary fidelity error is `E = Delta_agent - Delta_human`. For ordinal or binary outcomes, estimate analogous marginal contrasts using an appropriate model. Human and agent populations, dose policy, endpoint and missing-data policy must align; otherwise report the mismatch rather than calling the contrast equivalent.

Set an equivalence margin `delta` before final evaluation, justified by score meaning, reliability and acceptable error for the intended component use. No universal numerical margin is assumed here. Report raw-scale contrasts; standardized effects use the same prespecified human reference SD for both sources.

Use TOST at alpha .05 (equivalently, require the 90% confidence interval for E to lie wholly within `[-delta, +delta]`), alongside a 95% confidence interval for estimation. A nonsignificant difference is not equivalence. A wide interval is **inconclusive**. Passing this primary criterion is training-effect fidelity only, not full response or dynamic fidelity.

### Trial-level model and uncertainty

- Binary response: mixed-effects logistic model; ordered response: ordinal mixed model; continuous score: an appropriate continuous model with diagnostic checks.
- Include source, arm, time and their interactions. Account for participant and item clustering, with design-supported random slopes where identifiable. Compute marginal contrasts on interpretable scales rather than interpreting a logistic three-way coefficient as the raw change error.
- Account for persona/configuration clusters if present. Model settings are fixed conditions, not independent sampled humans.
- Propagate both human sampling uncertainty and agent Monte Carlo uncertainty. Use a prespecified clustered bootstrap or hierarchical model appropriate to the actual crossed design; never bootstrap all trials as independent observations.
- If an adaptive randomized stage is selected, specify its eligibility and weighting/model strategy before use. The simple contrast above applies only to the audited conventional contrast.

### Secondary fidelity measures

Report item-level probability/mean error and calibration, overall response proportions, dispersion/extreme-response rates, and pre/post association. Use Brier score for binary probabilistic predictions or an appropriate categorical/ordinal measure; compare with development-fitted simple baselines. Estimate probabilities from repeated runs while preserving their nesting.

Evaluate held-out themes separately. Human split-half comparisons matched for sample size provide a noise reference, not an automatic equivalence margin or a guarantee of validity. Prespecify secondary endpoint families and multiplicity handling; subgroup results and individual differences are exploratory unless separately powered. Do not claim stable heterogeneity from response noise alone.

### Missingness, precision and stopping

Match the original human analysis first, then state the fidelity estimand explicitly. For a randomized effect, retain eligible randomized participants where possible; justify missing-data assumptions and include sensitivity analyses for dropout. A completer analysis is labelled as such, not substituted for intention-to-treat. Do not invent outcomes for redacted trials. Report agent missing/invalid output separately and assess whether conclusions change under plausible handling choices.

Use audit-based simulations to choose agent run count and evaluate expected precision for E and item-level outcomes. More agent calls cannot reduce human uncertainty or compensate for too few stimulus themes. Freeze a run budget/stopping rule based on precision targets and resources, not whether the desired result becomes significant. Report minimum detectable discrepancies and any equivalence test too weak to be informative.

## 9. Contamination and demand-characteristic controls

| Threat | Required control | Remaining limitation |
|---|---|---|
| Prior exposure to papers/materials | Hide paper titles, researcher names, group labels and expected results; log material publication history and known model cutoff information | Closed-model training membership usually cannot be proven absent |
| Hypothesis leakage | Supply participant instructions only; audit every template and feedback message | Task structure may itself reveal contingencies |
| Training/test semantic overlap | Group items by theme; document exact/near overlap and novel assessment content | Original tasks may legitimately share content |
| Researcher tuning leakage | Separate development/validation/test; log candidates, decisions and test access | Published results may already be known |
| Scoring leakage | Freeze scoring before outputs; blind open-response coders to source/arm where feasible; keep keys outside agent context | Source can sometimes be inferred from language |
| Order/model drift | Counterbalance as the original task permits; interleave arms; freeze version and log dates | Provider snapshots may not be available |
| Selective reporting | Report all frozen conditions, failures, deviations and null/mismatch results | Exploratory follow-ups need separate interpretation |

Use original materials for reconstruction and a separate, human-benchmarked novel-material test where feasible. Paraphrasing alone does not establish contamination-free evaluation and may change ambiguity or difficulty. Never ask the model to reproduce published study results as a task instruction.

## 10. Decision rules and SOS handoff

- **Task-supported fidelity:** Prespecified primary equivalence passes and response/generalization checks meet their own frozen tolerances. Claims remain limited to the tested population, model and materials.
- **Mixed fidelity:** Training effects match but distributions or novel-item performance do not. Diagnose the specific failure; do not advance as a validated SOS student model.
- **Mismatch:** Evidence identifies errors outside acceptable bounds. Develop changes using development data and confirm on new independent data.
- **Inconclusive:** Data/material gaps or uncertainty prevent a decision. Obtain better evidence or narrow scope.

Before applying the component to SOS, obtain human benchmarks for Chinese school situations, distinguish objectively plausible threats from biased interpretations, test sequential experience and actual behaviour choices, and then validate recovery/cumulative dynamics with longitudinal data. CBM-I success does not establish that supportive teacher policies or other school interventions will have realistic simulated effects.

## 11. Execution checklist and outstanding freeze decisions

1. Inspect candidate files and complete Gate A/B/C audit.
2. Select population, randomized contrast, task, endpoint and score; reproduce human baseline.
3. Define data partitions, primary margin, secondary tolerances, missingness policy and precision targets.
4. Implement and dry-run task parsing, scoring, randomization, participant isolation and logging on development materials.
5. Freeze agent configuration, comparator models, run budget and analysis; preregister before final-test access.
6. Run interleaved conditions; perform blinded quality checks under frozen rules.
7. Evaluate final test once; publish uncertainty, failures, deviations and bounded conclusions.

**Outstanding decisions must be resolved before Step 5:** selected dataset/version; available participant and item counts; exact control and assignment stage; primary score and timepoint; delta and secondary tolerances; partition sizes; model/configuration; memory feasibility; number of runs; statistical model and bootstrap specification; reuse and external-processing permissions.

**Current next action:** Data audit, not agent optimization. No dataset has yet passed the entry gate, and no fidelity result is claimed by this revised protocol.
