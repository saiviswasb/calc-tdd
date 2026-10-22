# Calculator TDD Project (Ammann & Offutt)

Python calculator project developed using Test-Driven Development (TDD), featuring unit tests, randomized property testing, and an automated GitHub Actions CI/CD pipeline.

## Assignment Coverage
- **Q1 (manual TDD, no AI):** `add`, `subtract`, `multiply`, `divide` (with float precision pinning). Narrative: `docs/q1-narrative.md`
- **Q6 (agentic TDD):** `modulo` and `power` implemented using GitHub Copilot. Narratives, rule-violation report, and decisions report: `docs/q6-report.md`
- **Q3 (CI quality gates):** `flake8` static analysis + `coverage` (≥90% threshold) in GitHub Actions. `.flake8` ignores W293, W292, E302, E305 (whitespace/blank-line style only).
- **Property tests:** Inverse (`subtract(add(a, b), b) == a`) and commutativity (`multiply(a, b) == multiply(b, a)`) checks over 100 random inputs (`random.randint(-100, 100)`).
- **Not attempted:** Q2, Q4, Q5, Q7
- **AI usage log:** `docs/ai-usage-log.md`

## Method Behaviors & Decisions
- `divide(7, 2)` returns `3.5` (float precision check).
- `divide(5, 0)` raises `ValueError`.
- `modulo(-7, 3)` returns `2` (Python modulo semantics).
- `modulo(5, 0)` raises `ValueError`.
- `power(2, 3)` returns `8`.
- `power(0, 0)` returns `1`.
- `power(2, -1)` returns `0.5`.
- `power(0, -1)` raises `ZeroDivisionError` (untested).

## Running the Tests
To execute the unit and property tests locally with verbose output:
```powershell
python -m unittest -v
