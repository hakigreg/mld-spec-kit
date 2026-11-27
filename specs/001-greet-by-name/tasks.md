# Tasks: Greet by Name

**Input**: [spec.md](spec.md), [plan.md](plan.md), [data-model.md](data-model.md), [CLI contract](contracts/cli.md)

**Organization**: One user story is the MVP. All paths are from the project root.

## Phase 1: Setup

- [x] T001 Confirm Python 3.11+ is available and record the command in `README.md`.

## Phase 2: Foundational

No shared infrastructure is required for a single-file command.

## Phase 3: User Story 1 - Receive a personal greeting (P1)

**Independent test**: Run the four examples in `specs/001-greet-by-name/quickstart.md` and compare output and exit status with `specs/001-greet-by-name/contracts/cli.md`.

- [x] T002 [US1] Implement the `Name.value` trim and blank-name validation from `specs/001-greet-by-name/data-model.md` in `greet.py`.
- [x] T003 [US1] Implement the greeting and failure output described by `specs/001-greet-by-name/contracts/cli.md` in `greet.py`.
- [x] T004 [US1] Add the four acceptance checks from `specs/001-greet-by-name/spec.md` in `verify_lab.py`.

## Phase 4: Polish

- [x] T005 Document setup, run, exercise, and stop in `README.md` and the `mld/` learning guide.
- [x] T006 Run `python3 verify_lab.py` and compare its results with `specs/001-greet-by-name/quickstart.md`.

## Dependencies and execution order

T001 precedes T002. T002 and T003 share `greet.py`, so do them in order. T004 follows the contract; T005 follows the implementation; T006 is the completion gate. There are no safe parallel tasks in this one-file example.

## Implementation strategy

Finish US1 and stop. A later requirement change starts at `spec.md`, then flows through `plan.md`, `tasks.md`, code, and verification.

## Verification record

On 2026-11-26, Python 3.13.5 ran `verify_lab.py`: all four cases passed. `python3 greet.py Ada` printed `Hello, Ada!`; the whitespace case printed `Hello, Lin!`. Specify CLI 1.4.5 ran `specify check` and reported Codex CLI available. The learner's later `Hi` change was not run as part of this baseline.
