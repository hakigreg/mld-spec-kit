# Bad practices

## Treating a vague prompt as a specification

“Make a friendly greeting” does not settle whether an empty name is allowed or what exact output is expected. An agent may pick arbitrary defaults and tests may merely confirm those guesses. State acceptance examples and edge cases before planning. This Lab makes the output and failure cases explicit in `spec.md`. [Spec Kit SDD guidance](https://github.github.com/spec-kit/how-to/sdd.html).

## Mixing the what and how too early

If a feature spec says “use Python argparse and one file,” a later technical change looks like a requirement change even when users see no difference. Keep user-visible intent in the spec and technology choices in `plan.md`. Here, the greeting format belongs in FR-002; Python belongs in the plan. [Agentic SDD reference](https://github.github.com/spec-kit/reference/agentic-sdd.html).

## Editing only the code after intent changes

Changing `greet.py` to print `Hi` while the spec and contract still promise `Hello` creates two competing truths. The next agent or reviewer cannot tell whether this is a bug or a new requirement. Revise the spec, reconcile the dependent artifacts, and rerun acceptance checks. Spec Kit's core analysis reports inconsistencies but does not silently rewrite all files for you. [Evolving specs](https://github.github.com/spec-kit/how-to/evolving-specs.html).

## Mistaking document checks for runtime evidence

A completed requirements checklist says the spec has been reviewed for clarity; it does not show the command works. Conversely, one successful command does not cover blank input. Run scenarios with expected output and exit status. This Lab's `verify_lab.py` checks four cases and its quickstart explains them. [Quickstart](https://github.github.com/spec-kit/quickstart.html).

## Expanding the process beyond the feature's risk

A tiny greeting does not need a database, deployment service, multiple user stories, or an elaborate test stack. Extra components obscure the behavior the learner came to study. For a consequential feature, skipping clarification or contract review can be the opposite mistake. Choose the smallest process that exposes the relevant decisions, then add gates when ambiguity or impact grows. [Quickstart's short and full paths](https://github.github.com/spec-kit/quickstart.html).
