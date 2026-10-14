# Pilot 0 — Synthetic Interpretation Bias Experiment

**Purpose:** Start running a testable experiment now, before selecting a human dataset. **This pilot is a code/protocol feasibility test, not human behavioral fidelity evidence.** The stimuli are new, synthetic examples and do not reproduce any published CBM-I intervention.

## Design

- **Task:** Rate the plausibility (0–4) of negative and benign explanations for ambiguous everyday situations. Bias = mean(negative − benign).
- **Conditions:** Ten training examples with a benign/negative ending mix of **9/1 (positive)** versus **5/5 (balanced)**.
- **Assessment:** Twelve untouched original scenarios divided into two six-item folds. Alternate AB/BA order across independent virtual participants to counterbalance item differences.
- **Outcome:** `(post − pre)_positive − (post − pre)_balanced` on interpretation-bias ratings. Any observed effect shows **prompt/context sensitivity**, not validated anxiety, treatment response or similarity to humans.
- **Caveats:** Training is presented as text exposure, not gradual human learning. The model sees its own baseline ratings. The instruction format and separate valence labels in code are not shown as treatment names. API sampling need not produce human-like participant variability.

## Requirements

Windows CMD, Python 3.10 or newer.

## First run — no API cost

From the SOS repository root:

```cmd
cd experiments\anxiety_fidelity_pilot
python pilot.py --mode mock --per-arm 2
```

This exercises the whole pipeline with **fake random ratings**. It does not call any LLM. Results are saved to `results/<timestamp>_mock_seed.../` and are ignored by Git.

## First actual model test — may incur API charges

```cmd
python -m pip install -r requirements.txt
set OPENAI_API_KEY=YOUR_API_KEY
python pilot.py --mode api --model gpt-4.1-mini --per-arm 2 --confirm-api-cost
```

**Never commit your API key or paste it in chat.** Set the key using your own local shell or environment manager. The model string is an example; it must be available to your API account. An API subscription and ChatGPT subscription are billed separately. For larger pilots, check your usage and current model pricing first.

With 2 runs per arm, the tool makes **8 API calls** (pre + post for each independently initialized virtual participant). It saves each successful trajectory immediately. An error stops the run without fabricating a summary.

To scale up after inspecting the small run:

```cmd
python pilot.py --mode api --model gpt-4.1-mini --per-arm 30 --confirm-api-cost
```

This makes **120 API calls** if all complete; it is *not* a statistically powered equivalence test.

## Outputs

- `manifest.json`: run settings and stimulus checksum.
- `responses.jsonl`: arm, participant, shuffled training valences, pre/post item ratings, and bias change.
- `summary.json`: group-average changes and the difference-in-differences. This is **not a human fidelity score**.

## Before a real paper

Replace/validate the stimuli and protocol against an accessible human study, reproduce its measurement schedule and scoring, register the intended endpoints, and keep held-out items independent. Only then evaluate human–agent behavioral fidelity. Do not simply compare these synthetic pilot ratings to unrelated adult-scale totals.
