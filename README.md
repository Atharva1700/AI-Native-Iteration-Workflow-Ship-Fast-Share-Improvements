# AI-Native Iteration Workflow

End-to-end feature built with Claude Code, shipped in three rapid iterations, improvements documented and shared.

## Stack
- **Python**: Core feature implementation
- **Claude Code**: AI-assisted drafting & iteration
- **GitHub Actions** (simulated): Auto-run tests on each iteration

## Files
- `feature.py`: Core pipeline (parse → validate → aggregate)
- `validators.py`: Reusable validation framework (extracted in Iteration 3)
- `test_feature.py`: Test suite
- `CHANGELOG.md`: Detailed log of all three iterations + pattern extraction

## Run

```bash
python3 test_feature.py
```

## What This Shows
1. **Initial Draft** (Iteration 1): Claude Code generates working MVP
2. **Rapid Iteration** (Iterations 2 & 3): Each documented, pushed to team
3. **Pattern Extraction** (Mid-project discovery): `ValidatedPipeline` class pulled into `validators.py`, now reused across team
4. **Shared Knowledge**: CHANGELOG explains *what* improved and *why*

**Demonstrates**: 
- Shipping features fast with AI assistance
- Maintaining clarity through documented iterations
- Extracting and sharing reusable patterns across the team (stated core value)
