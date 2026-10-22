# Q1: Manual TDD Narrative (No AI)

## Overview
The core arithmetic methods (`add`, `subtract`, `multiply`, `divide`) were developed strictly using manual Test-Driven Development (Red-Green-Refactor) without AI assistance.

## Red-Green-Refactor Cycles
1. **Addition (`add`)**: 
   - **Red**: Wrote `test_add` expecting `calc.add(2, 3) == 5` before `add` existed (test failed).
   - **Green**: Implemented basic addition in `calculator.py`.
2. **Subtraction (`subtract`)**:
   - **Red**: Wrote `test_subtract` expecting `calc.subtract(5, 3) == 2`.
   - **Green**: Implemented subtraction.
3. **Multiplication (`multiply`)**:
   - **Red**: Wrote `test_multiply` expecting `calc.multiply(4, 3) == 12`.
   - **Green**: Implemented multiplication.
4. **Division (`divide` & `divide_by_zero`)**:
   - **Red**: Wrote tests for normal division and zero division together, which initially failed.
   - **Green**: Implemented division with explicit `ValueError` checking for zero denominators.
   - **Float Precision Addition**: Added the float-precision pinning test (`divide(7, 2) == 3.5`) after the baseline divide methods were already established and passing, confirming that division correctly returns floating-point numbers in Python.