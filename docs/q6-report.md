# Q6: Agentic TDD Report (GitHub Copilot)

## Overview
Advanced operations (`modulo` and `power`) were implemented using AI-assisted agentic TDD.

## Per-Cycle Narratives & Review Comments
- **Modulo Basic & Negative Operands**: 
  - *Agent Action*: Implemented modulo using Python's native `%` operator. 
  - *Review/Refinement*: Verified that `modulo(-7, 3)` evaluates to `2` under standard Python mathematical semantics.
- **Power & Exponents**:
  - *Agent Action*: Implemented exponentiation using `**`.
  - *Review/Refinement*: Added explicit tests for zero-to-zero (`power(0, 0) == 1`) and negative exponents (`power(2, -1) == 0.5`).

## Rule-Violations Report
The following tests passed immediately on the first attempt without going through a proper failing "Red" cycle:
1. `test_modulo_negative_operand` (handled inherently by Python's operator implementation).
2. `test_power_zero_to_zero` (handled correctly by Python's `**` operator returning `1`).
3. `test_power_negative_exponent` (handled correctly by Python's `**` operator returning `0.5`).

## Decisions Made Without Asking
During agentic TDD, the agent made the following architectural and implementation decisions silently:
- Utilized native Python operators (`%` and `**`) instead of writing custom mathematical loops or recursive multiplication algorithms.
- Raised built-in `ValueError` for division and modulo by zero exceptions rather than returning `None` or custom exception classes.