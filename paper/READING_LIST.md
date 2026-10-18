# Reading List — Psychological Behavioral Fidelity (October 2026)

**Research question:** Under what conditions do LLM-generated responses reproduce **human anxiety-related behavioral patterns**, rather than merely producing plausible psychological language?

This is a **bibliography / acquisition manifest**, not a record of completed downloads. Check article metadata, PDF integrity, and the *specific file's redistribution license* before committing PDFs to this public repository. An article being free to read does **not automatically** mean its publisher PDF can be publicly mirrored.

## Priority 1 — Read First

| Key | Paper | Official source | Why it matters |
| --- | --- | --- | --- |
| P01 | Cronbach & Meehl (1955), **Construct validity in psychological tests** | [DOI](https://doi.org/10.1037/h0040957) | Why a questionnaire response or a plausible simulated choice is not itself evidence of psychological construct validity |
| P02 | Würtz et al. (2026), **Interpretation biases in anxiety: A three-level meta-analysis** | [DOI](https://doi.org/10.1177/21677026251392855) | Quantitative human relationship between anxiety symptoms and interpretation bias; openly licensed article (verify PDF/version) |
| P03 | Lin (2026), **From prompts to constructs: A dual-validity framework for large language model research in psychology** | [DOI](https://doi.org/10.1146/annurev-psych-100925-034807) | Evaluation and construct-validity standards for LLM psychology; publisher version may be access/reuse restricted |
| P04 | Coda-Forno et al. (2023; revised 2024), **Inducing anxiety in large language models can induce bias** | [arXiv:2304.11111](https://arxiv.org/abs/2304.11111) | Early anxiety-prompting result; compare output shifts with true human correspondence |
| P05 | Binz et al. (2025), **A foundation model to predict and capture human cognition** (Centaur) | [DOI](https://doi.org/10.1038/s41586-025-09215-4) | Strong baseline for predicting human decisions; Nature OA paper has CC BY 4.0 notice |
| P06 | Kolluri et al. (2025), **Finetuning LLMs for human behavior prediction in social science experiments** (Socrates) | [ACL Anthology](https://aclanthology.org/2025.emnlp-main.1530/) · [PDF](https://aclanthology.org/2025.emnlp-main.1530.pdf) | Human response distributions, fine-tuning and held-out experimental generalization |
| P07 | Cui, Li & Zhou (2025), **A large-scale replication of scenario-based experiments in psychology and management using large language models** | [DOI](https://doi.org/10.1038/s43588-025-00840-7) | Effect-size inflation in LLM simulated experiments; find author preprint for accessible PDF |
| P08 | Wekenborg et al. (2026), **Large language models as experimental systems in human psychopathology: A modelling study** | [DOI](https://doi.org/10.1016/j.landig.2026.101014) · [Code](https://github.com/WekenborgLab/LLMAffect) | Affect induction and its limits as evidence for human behavioral fidelity |

## Priority 2 — Measurement, Interventions, and Pitfalls

| Key | Paper | Official source | Why it matters |
| --- | --- | --- | --- |
| P09 | Leung et al. (2022), **The combined cognitive bias hypothesis in anxiety: A systematic review and meta-analysis** | [DOI](https://doi.org/10.1016/j.janxdis.2022.102575) | Differentiates attention, interpretation and memory biases and their limited transfer |
| P10 | Sicouri et al. (2024), **Cognitive bias modification of interpretations for anxiety and depression in children and adolescents: A meta-analysis** | [DOI](https://doi.org/10.1002/jcv2.12207) · [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10933640/) | Interpretation-bias changes cannot be equated with improvements in clinical symptoms |
| P11 | Armbruster-Genç et al. (2024), **The Ambiguous Cue Task: Measurement reliability of an experimental paradigm for the assessment of interpretation bias and associations with mental health** | [DOI](https://doi.org/10.3758/s13428-024-02451-y) · [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11362423/) | Distinguishes measurement reliability from meaningful anxiety associations |
| P12 | Ashokkumar et al. (2026), **Large language models can predict the results of social science experiments** | [DOI](https://doi.org/10.1038/s41586-026-10742-x) | Compare experiment prediction and effect inflation; **publisher version not confirmed redistributable** |
| P13 | Lin et al. (2026), **The illusion of intervention: Your LLM-simulated experiment is an observational study** | [arXiv:2605.20767](https://arxiv.org/abs/2605.20767) | Persona/user drift and unwanted condition differences in simulated interventions |
| P14 | Ji et al. (2021), **Multi-session online interpretation bias training for anxiety in a community sample** | [DOI](https://doi.org/10.1016/j.brat.2021.103864) · [Cleaning and data documentation](https://github.com/TeachmanLab/MT-Data-ManagingAnxietyStudy-Cleaning) | Candidate human dataset and experimental protocol; **not selected as final benchmark** |

## Acquisition and Repository Rules

1. **Inventory existing `paper/` PDFs** before searching or downloading. Do not rename or delete pre-existing research material.
2. For each entry, verify bibliographic identity (title, first author, year and DOI/arXiv) against an authoritative source. Search the publisher, arXiv, ACL Anthology, PubMed Central or an institutional repository for **legitimate PDFs**. Do not bypass paywalls or fabricate downloads.
3. Check license **per version/file**. Commit PDFs to this **public** repository only when redistribution is expressly allowed (e.g., verified CC BY). When uncertain, retain the paper **locally** and keep only metadata + official link in GitHub.
4. Maintain `paper/PAPER_MANIFEST.csv` with key, official URL, local filename (if any), SHA-256, access source, redistribution-license evidence URL, public-commit eligibility, and retrieval status. Use `unverified` / `unavailable` rather than guessing.
5. Prefer transparent filenames such as `P05_Binz_2025_Centaur.pdf`; ensure the bytes are valid PDF and match the target title/DOI (check document metadata or first pages).
6. Do not add copyrighted full text, temporary download caches, large unrelated supplements, user account credentials, cookies or private datasets to GitHub.
7. This folder is for **reading materials**, not the human benchmark itself. Dataset selection and agent experiments remain separate decisions.

## What to Read Before Designing the Next Experiment

Read **P01 → P02 → P03 → P04 → P07 → P05 → P06 → P13**. Extract for each: **scientific claim; observable task; human baseline; analysis metric; limits; one opportunity or contradiction**.

## Acquisition status - 2026-10-17

All 14 bibliographic identities were checked against DOI, ACL Anthology or arXiv records. `PUBLIC_OK` means the *downloaded version* has a verified redistribution license and is eligible for this public repository. `LOCAL_ONLY` means a valid PDF was downloaded but cannot be publicly mirrored on the present evidence. `LINK_ONLY` means no PDF was acquired. See [PAPER_MANIFEST.csv](PAPER_MANIFEST.csv) for authors, version, source, license evidence, hashes, size and retrieval date. GitHub publication is a separate Git state; these labels describe acquisition and rights, not the success of a push.

| Key | Acquisition | PDF / official link | Finding |
| --- | --- | --- | --- |
| P01 | LOCAL_ONLY | [local PDF](_local/P01_Cronbach_Meehl_1955_ConstructValidity.pdf) | University-hosted scan; redistribution permission not established. |
| P02 | LINK_ONLY | [SAGE article](https://doi.org/10.1177/21677026251392855) | Article is CC BY 4.0, but PDF request returned HTTP 403. |
| P03 | PUBLIC_OK | [arXiv PDF](P03_Lin_2026_DualValidity_arXiv.pdf) | CC BY 4.0 arXiv version; PDF cites a 2027 print volume, DOI was published online in 2026. |
| P04 | LOCAL_ONLY | [local PDF](_local/P04_CodaForno_2023_InducingAnxiety_arXiv.pdf) | arXiv non-exclusive distribution license does not grant third-party mirroring. |
| P05 | PUBLIC_OK | [Nature PDF](P05_Binz_2025_Centaur.pdf) | Publisher version, CC BY 4.0; losslessly repacked, with original and archived hashes recorded in the manifest. |
| P06 | PUBLIC_OK | [ACL PDF](P06_Kolluri_2025_Socrates.pdf) | ACL Anthology version, CC BY 4.0. |
| P07 | PUBLIC_OK | [arXiv PDF](P07_Cui_2025_Replication_arXiv.pdf) | CC BY-NC-SA 4.0 preprint; its title differs from the journal version. |
| P08 | LINK_ONLY | [Lancet article](https://doi.org/10.1016/j.landig.2026.101014) | Article is CC BY 4.0, but publisher PDF request returned HTTP 403. |
| P09 | PUBLIC_OK | [Essex-hosted publisher PDF](P09_Leung_2022_CombinedCognitiveBias.pdf) | PDF states CC BY 4.0. |
| P10 | PUBLIC_OK | [Macquarie-hosted publisher PDF](P10_Sicouri_2024_CBMI_MetaAnalysis.pdf) | CC BY 4.0; first published online in 2023, 2024 volume. |
| P11 | PUBLIC_OK | [Springer PDF](P11_ArmbrusterGenc_2024_AmbiguousCueTask.pdf) | Publisher version, CC BY 4.0. |
| P12 | LOCAL_ONLY | [local PDF](_local/P12_Ashokkumar_2026_SocialScienceExperiments.pdf) | Author-linked Nature PDF; public redistribution license unverified. |
| P13 | PUBLIC_OK | [arXiv PDF](P13_Lin_2026_IllusionOfIntervention_arXiv.pdf) | CC BY 4.0 arXiv version; first author Victoria Lin. |
| P14 | LINK_ONLY | [journal DOI](https://doi.org/10.1016/j.brat.2021.103864) | OSF preprint endpoint returned HTTP 503; journal PDF unavailable. The old reading-list label was not the paper title. |

Links marked "local PDF" work only in a local checkout with `paper/_local/`; that folder is intentionally excluded from Git. The three PDFs that predated this acquisition remain untouched.
