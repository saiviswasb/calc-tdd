# Calculator TDD Project (Ammann & Offutt)

A robust Python calculator project developed using Test-Driven Development (TDD), featuring comprehensive unit tests, randomized property-based testing, and an automated GitHub Actions CI/CD pipeline enforcing strict quality and coverage gates.

---

## Features & Operations
* **Core Arithmetic**: Addition, subtraction, multiplication, and division (with explicit float precision pinning).
* **Advanced Operations**: Modulo and exponentiation/power methods.
* **Robust Error Handling**: 
  * Division and modulo by zero handling (`ValueError`).
  * Negative operand and zero exponent management.

---

## Project Structure
* `calculator.py`: Core calculator implementation.
* `test_calculator.py`: Comprehensive unit tests and 100-iteration randomized property tests.
* `.github/workflows/ci.yml`: Automated CI/CD pipeline config.
* `.flake8`: Static analysis configuration.

---

## CI/CD & Quality Gates
The project uses **GitHub Actions** to automatically enforce code standards on every push and pull request:
1. **Static Analysis (`flake8`)**: Scans core files while respecting configured style rules.
2. **Test Coverage (`coverage`)**: Automatically executes unit and property tests, enforcing a **minimum 90% statement coverage threshold**.

---

## Extra Credit & Experimental Components
* **Q2 (CI/CD Failure & Recovery Cycle)**: Documented deliberate test/build breakages and recovery cycles captured via GitHub Actions history.
* **Q3 (Automated CI/CD)**: Fully functional green pipeline with static analysis and coverage enforcement.
* **Q7 (Property-Based Testing)**: Validated inverse (`subtract(add(a, b), b) == a`) and commutative (`multiply(a, b) == multiply(b, a)`) invariants across 100 randomized iterations (`random.randint(-100, 100)`).
