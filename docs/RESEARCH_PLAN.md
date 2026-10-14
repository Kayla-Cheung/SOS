\# SOS Research Plan

\## Validating LLM Agents as Simulated Subjects in Anxiety-Related Psychological Experiments



\*\*Status:\*\* Literature Review \& Experimental Feasibility Assessment  

\*\*Last Updated:\*\* 2026-10-14  

\*\*Project:\*\* SOS — Simulating On-campus Stress



\---



\## 1. Research Background



SOS (Simulating On-campus Stress) aims to develop an agent-based simulation framework for studying academic stress, anxiety dynamics, social interactions, and potential interventions in campus environments.



The long-term objective is to investigate how psychological states emerge, evolve, and respond to environmental and social factors in populations of simulated agents.



However, before building a complex psychological simulation system, a fundamental methodological question must be addressed:



\*\*Can LLM-based agents serve as behaviorally valid simulated subjects in psychological experiments?\*\*



If LLM agents cannot reliably reproduce relevant human behavioral patterns, then conclusions drawn from large-scale simulations of anxiety, stress, or intervention effects may lack empirical validity.



Therefore, the current research focuses on establishing the scientific feasibility of psychological agent simulation, rather than implementing SOS itself.



\---



\## 2. Current Research Objective



\### Primary Research Question



\*\*To what extent can LLM agents reproduce human behavioral patterns and experimental effects in anxiety-related cognitive psychology tasks?\*\*



The immediate goal is to evaluate whether LLM agents can reproduce human anxiety-related cognitive responses under controlled experimental conditions.



We are particularly interested in whether simulated agents reproduce not only the direction of psychological effects, but also their magnitude, distribution, variability, and response to interventions.



\### Research Questions



\*\*RQ1 — Behavioral Fidelity\*\*



Can LLM agents reproduce the response distributions observed in human anxiety-related cognitive experiments?



\*\*RQ2 — Intervention Fidelity\*\*



Can LLM agents reproduce human behavioral changes following cognitive interventions, including the magnitude and direction of treatment effects?



\*\*RQ3 — Generalization\*\*



Do behavioral changes generalize to unseen stimuli and related cognitive tasks, rather than merely reflecting experimental instructions or response patterns?



\*\*RQ4 — Mechanism Improvement (Future Work)\*\*



If baseline agents exhibit systematic deviations from human behavior, can memory, cognitive-state modeling, or structured decision mechanisms reduce these deviations?



RQ1–RQ3 constitute the initial empirical validation study. RQ4 is a possible extension and should not determine the outcome of the initial study.



\---



\## 3. Scope and Scientific Position



\### What We Aim to Establish



The study investigates \*\*human behavioral fidelity\*\*, defined as the extent to which LLM-generated responses approximate empirically observed human responses under comparable psychological experimental conditions.



Potential evaluation dimensions include:



\- Response fidelity: similarity of response probabilities and distributions.

\- Effect fidelity: similarity of experimental effects and changes across conditions.

\- Generalization fidelity: stability of behavioral similarity across new stimuli or contexts.

\- Individual variability: whether simulated populations reproduce meaningful variation observed among humans.



\### What We Do Not Claim



We do not assume that LLM agents:



\- Experience anxiety, depression, or other subjective psychological states.

\- Possess the same underlying cognitive mechanisms as humans.

\- Can replace human participants in arbitrary psychological experiments.

\- Can reproduce real clinical treatment effects simply by responding to textual prompts.



A positive result would support \*\*task-specific behavioral simulation validity\*\*, not general psychological equivalence.



This distinction is especially important for future applications to SOS.



\---



\## 4. Literature Review: Current Findings



Existing research has already established that LLMs can exhibit anxiety-related responses under certain experimental manipulations.



However, the validity of using these responses as substitutes for human experimental outcomes remains uncertain.



\### 4.1 Existing Research



\*\*Inducing Anxiety in Large Language Models Can Induce Bias — Coda-Forno et al. (2023/2024)\*\*



Investigates anxiety-related prompting, self-reported anxiety measures, and biased model responses.



Contribution: Demonstrates that anxiety-related prompting can modify LLM outputs.



Limitation: Changes in model responses do not establish correspondence with human anxiety-related cognitive processes.



Reference: https://arxiv.org/abs/2304.11111



\*\*Large Language Models as Experimental Systems in Human Psychopathology (2026)\*\*



Investigates induced affective states, self-report measures, and related cognitive responses in LLMs.



Contribution: Provides a direct precedent for studying psychopathology-related phenomena in language models.



Limitation: LLM self-report and affective language changes do not independently establish human behavioral fidelity.



Reference: https://doi.org/10.1016/j.landig.2026.101014



\*\*Inducing State Anxiety in LLM Agents Reproduces Human-like Biases in Consumer Decision-making (2026)\*\*



Investigates changes in agent decision-making following anxiety-related narrative induction.



Contribution: Extends evaluation from questionnaire responses to behavioral choices.



Limitation: Directionally human-like behavior does not establish quantitative agreement with matched human experiments.



Reference: https://doi.org/10.1038/s44387-026-00122-1



\*\*A Large-Scale Replication of Scenario-Based Experiments in Psychology and Management Using Large Language Models (2025)\*\*



Examines replication of effects from a large collection of human experiments.



Contribution: Demonstrates that LLMs can reproduce many reported experimental effects.



Limitation: Effect-size inflation and other deviations caution against equating effect replication with valid human simulation.



Reference: https://doi.org/10.1038/s43588-025-00840-7



\*\*PsychBench: Auditing Epidemiological Fidelity in Large Language Model Mental Health Simulations (2026, preprint)\*\*



Examines the correspondence between simulated mental-health questionnaire distributions and real population data.



Contribution: Highlights the importance of population-level distribution fidelity.



Limitation: Population-level questionnaire audits do not fully evaluate longitudinal behavioral responses to controlled cognitive interventions.



Reference: https://arxiv.org/abs/2604.17359



\### 4.2 Preliminary Research Gap



The literature already addresses:



1\. Whether LLMs can generate anxiety-like questionnaire responses.

2\. Whether affective prompts can change model behavior.

3\. Whether LLMs can reproduce some psychological experimental effects.



A remaining candidate research gap is:



\*\*Whether LLM agents can quantitatively reproduce human responses to anxiety-related cognitive interventions, including effect magnitude, behavioral distributions, variability, and transfer to unseen experimental stimuli.\*\*



This gap is provisional. A comprehensive comparison with closely related studies is still required before claiming novelty.



\---



\## 5. Candidate Human Experimental Data



Rather than constructing artificial psychological tests from scratch, the research will initially use established experiments with real human participants.



\### 5.1 Primary Candidate: MindTrails / CBM-I



Human studies of \*\*Cognitive Bias Modification for Interpretation (CBM-I)\*\* are particularly relevant.



CBM-I experiments investigate how participants interpret ambiguous situations and how interpretation tendencies may change following cognitive training.



Relevant study:



\*\*Web-Based Interpretation Bias Training to Reduce Anxiety — Eberle et al. (2024)\*\*



Reference: https://doi.org/10.1037/ccp0000896



Related resources:



\- https://github.com/TeachmanLab/MT-Data-CalmThinkingStudy

\- https://osf.io/s8v3h/



Potential variables:



\- Participant identifiers and experimental groups

\- Ambiguous scenario stimuli

\- Interpretation ratings or choices

\- Training condition

\- Pre-intervention and post-intervention measurements

\- Anxiety-related questionnaire scores

\- Repeated measurements across sessions



\*\*Important:\*\* Complete access to trial-level responses, original stimuli, and experimental conditions has not yet been verified.



\### 5.2 Additional Candidate



A 2026 CBM-I study by Abado et al. provides another possible source of human experimental data.



Reference: https://doi.org/10.1038/s41398-026-04122-2



Data repository:



https://osf.io/e254p/



Availability and completeness of stimulus-level data must be checked before experimental replication.



\### 5.3 Alternative Dataset



Psych-101 / Centaur provides extensive human cognitive experiment data.



Reference: https://huggingface.co/datasets/marcelbinz/Psych-101



It may support pipeline development or supplementary cognitive-task evaluation.



However, general cognitive-task performance does not by itself establish anxiety simulation validity. Therefore, Psych-101 is not the primary dataset for the current research.



\---



\## 6. Proposed Experimental Design



\### Phase A — Dataset Feasibility Audit



Before implementing agents, verify:



1\. Whether the complete human experimental instructions and stimuli are accessible.

2\. Whether individual responses can be reconstructed.

3\. Whether treatment and control groups can be identified.

4\. Whether baseline and follow-up measurements are available.

5\. Whether training materials and assessment materials can be separated.

6\. Whether the original experimental protocol can be reproduced in a text-based environment without introducing major confounds.



\*\*Deliverable:\*\* A documented, reproducible human experimental dataset with a clear data dictionary.



If these requirements cannot be met, an alternative dataset or task must be selected.



\### Phase B — Baseline LLM Simulation



Implement a minimal experimental environment that reproduces the selected human cognitive task as faithfully as possible.



Use an LLM as a simulated participant.



Each simulated participant should:



\- Begin with an independently initialized session.

\- Receive standardized instructions.

\- Encounter stimuli in a controlled sequence.

\- Produce responses in the same format used by human participants.

\- Receive only the information permitted by the experimental protocol.

\- Maintain a separate experimental history.

\- Never receive the target human participant's withheld responses.



Initially, use one fixed model and a simple prompting protocol.



Do not introduce complex memory systems, GOSI, multi-agent interaction, or additional psychological architectures during baseline evaluation.



\### Phase C — Human–Agent Fidelity Evaluation



Compare human and simulated responses using:



\*\*1. Response Distribution Fidelity\*\*



Compare response probabilities and choice distributions across the same experimental stimuli.



Candidate metrics: Jensen–Shannon divergence and trial-level probability errors.



\*\*2. Experimental Effect Fidelity\*\*



Compare treatment–control differences and pre–post changes.



The key question is not only whether the direction of the effect matches, but whether its magnitude is close to the human estimate.



\*\*3. Generalization Fidelity\*\*



Use independent assessment stimuli to determine whether apparent behavioral changes transfer beyond training examples.



\*\*4. Variability and Robustness\*\*



Investigate whether repeated simulated participants reproduce human variability, and whether findings depend heavily on sampling settings, prompts, or model versions.



Human–human comparisons will provide a reference for expected sampling variability.



The analysis should report uncertainty and prespecified tolerance thresholds rather than treating nonsignificant differences as proof of equivalence.



\### Phase D — Mechanism Study (Conditional)



Only after identifying clear and reproducible failures in baseline simulation should alternative methods be tested.



Possible methods include:



\- Episodic memory and memory retrieval

\- Limited or decaying memory

\- Explicit belief or goal representation

\- Structured cognitive-state modeling

\- GOSI-inspired decision representations



The research question would then become:



\*\*Does the proposed mechanism improve agreement with real human behavioral data on independently held-out tests?\*\*



Improved reasoning quality, task accuracy, or narrative coherence alone will not count as improved behavioral fidelity.



\---



\## 7. Key Methodological Risks



\*\*Construct Validity\*\*



A high score on an anxiety scale does not demonstrate that an LLM experiences anxiety or reproduces the corresponding human construct.



\*\*Intervention Comparability\*\*



A human experiencing repeated cognitive training or real-life stress is not necessarily equivalent to an LLM receiving analogous textual instructions.



\*\*Demand Characteristics and Prompt Leakage\*\*



LLMs may infer the intended experimental outcome from the task description and generate compliant responses.



\*\*Simulation Drift\*\*



Changing an experimental condition may unintentionally alter other simulated participant characteristics.



\*\*Effect-Size Inflation\*\*



LLMs may reproduce the direction of a human effect while substantially exaggerating its magnitude.



\*\*Population Homogeneity\*\*



Independent LLM samples do not automatically represent independent human-like individuals. Simulated diversity must be evaluated, not assumed.



\*\*Task and Data Contamination\*\*



Models may have encountered published psychological materials during pretraining. Stimulus leakage and generalization to new items require attention.



\*\*Data Limitations\*\*



Some publicly shared psychological datasets lack full stimuli, trial-level responses, or unrestricted access.



All findings must explicitly acknowledge these limitations.



\---



\## 8. Current Research Stage



As of 2026-10-14:



| Component | Status |

|---|---|

| Research objective | Defined |

| Initial literature review | Completed provisionally |

| Candidate research gap | Identified, not yet confirmed novel |

| Candidate human datasets | Identified |

| Trial-level dataset accessibility | Not yet fully verified |

| Experimental protocol | Conceptual design completed |

| Baseline Agent experiments | Not started |

| Human–Agent comparison | Not started |

| New agent architecture | Not started |



No experimental findings are currently claimed.



\---



\## 9. Immediate Goals



\### Priority 1 — Verify Human Data



Inspect the MindTrails and alternative CBM-I repositories.



Identify a human experiment with accessible stimuli, response data, experimental conditions, and a reproducible measurement protocol.



\### Priority 2 — Reconstruct the Human Experiment



Build a standardized dataset containing:



\- Subject and experimental-condition identifiers

\- Stimulus identifiers and presentation order

\- Original experimental instructions

\- Responses and scoring rules

\- Relevant pre/post measures



Reproduce the human study's primary behavioral statistics where possible.



\### Priority 3 — Implement a Minimal Agent Baseline



Allow a single LLM model to independently complete the corresponding experimental task.



Record all stimuli, responses, model configurations, random seeds where supported, and experimental histories.



\### Priority 4 — Conduct Fidelity Analysis



Measure agreement and deviation between human and Agent results.



Identify whether failures concern:



\- Response distributions

\- Intervention effects

\- Generalization

\- Variability

\- Stability across experimental settings



\### Priority 5 — Decide Whether a New Mechanism Is Needed



Based on actual simulation failures, determine whether memory or structured cognitive modeling offers a scientifically motivated improvement target.



\---



\## 10. Long-Term Research Roadmap



\*\*Stage 1 — Anxiety Simulation Validity\*\*



Establish whether LLM agents reproduce specific human anxiety-related cognitive and behavioral patterns.



\*\*Stage 2 — Mechanism Development\*\*



Investigate whether memory, cognitive-state representations, or structured decision mechanisms improve simulation validity.



\*\*Stage 3 — Dynamic Psychological Simulation\*\*



Extend validated methods to longitudinal psychological changes and interactions.



\*\*Stage 4 — SOS Integration\*\*



Apply the validated simulation methodology to academic stress dynamics, social buffering, stress propagation, and intervention studies.



Each stage depends on evidence from the previous stage. Success should not be assumed in advance.



\---



\## 11. Current Working Research Title



\*\*Do LLM Agents Faithfully Simulate Human Responses to Anxiety-Related Cognitive Interventions?\*\*



Alternative:



\*Beyond Anxiety-Like Responses: A Human-Grounded Evaluation of Behavioral Fidelity in LLM Agents\*



\### Central Principle



\*\*The objective is not to make agents appear psychologically human, but to determine whether their behavior is empirically comparable to that of human participants in clearly defined psychological experiments.\*\*



Until this validity is established, SOS should be treated as a proposed experimental framework rather than a validated substitute for human psychological research.

