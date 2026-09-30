# SOS (Student Overload Simulator)

Agent-based simulation of academic anxiety dynamics and sociological interventions, built on [SINA](https://github.com/Kayla-Cheung/SINA).

## Mechanics

- **State Representation**: Tracks cognitive load ($L$), social buffer ($R$), internal anxiety ($A$), and burnout threshold ($B$).
- **Diffusion & ToM**: Models stress contagion and recursive belief tracking (Theory of Mind) across campus interaction graphs.
- **Intervention Benchmark**: Evaluates peer buffering and institutional pacing against unmitigated baselines.

## References (`paper/`)

- `05_Generative_Agents_Memory_Stream_2304.03442.pdf`: Generative Agents architecture
- `02_Theater_of_Mind_for_LLMs.pdf`: Recursive Theory of Mind for LLMs
- `2604.04157_Readable_Minds_Poker_ToM.pdf`: Multi-agent mental state tracking

## Structure

```text
SOS/
├── paper/      # Core literature
├── src/        # Simulation engine (WIP)
└── config/     # Campus graphs and agent profiles
```
