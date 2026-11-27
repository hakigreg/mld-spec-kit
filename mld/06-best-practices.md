# Best practices

## Make requirements observable

Write behavior in terms of inputs, outputs, and decisions a user can see. “Greet the user” leaves punctuation, missing input, and trimming open to interpretation; `FR-002` through `FR-004` and the acceptance scenarios remove those gaps. This matters before planning because technical choices built on ambiguity can be expensive to reverse. Keep implementation language out of the spec; put it in the plan. [Agentic SDD reference](https://github.github.com/spec-kit/reference/agentic-sdd.html).

## Use the constitution as a real gate

Project principles should constrain choices. Here, “one observable behavior” keeps a web server and database out of a greeting example. In a larger project a constitution might require accessibility checks, interface compatibility, or deployment constraints. Review the plan against it and explain any exception rather than adding boilerplate principles that nobody checks. [Quickstart](https://github.github.com/spec-kit/quickstart.html).

## Preserve traceability through the stages

For each significant requirement, be able to point to a design choice, implementation task, code path, and acceptance check. The greeting's exact line appears in `spec.md`, `contracts/cli.md`, `greet.py`, and `verify_lab.py`. When one changes, review the others. A task should say which file and behavior it covers so an agent can execute it and a reviewer can assess it. Optional `$speckit-analyze` checks for cross-artifact inconsistencies; `$speckit-converge` looks for remaining implementation gaps. [Command reference](https://github.github.com/spec-kit/reference/agentic-sdd.html).

## Add quality gates where ambiguity warrants them

Use clarification before planning when several interpretations materially change scope or user experience. Use a requirements checklist to examine the specification as a document, and analysis after tasks to catch contradictions. Do not treat checked spec-quality boxes as proof that code works; run the behavior. This Lab's four acceptance examples are small enough to verify directly. [Quickstart](https://github.github.com/spec-kit/quickstart.html).

## Reconcile changes from their source

When the desired greeting changes from `Hello` to `Hi`, update the spec first, then the plan or contract if needed, then tasks, implementation, and checks. If a code discovery reveals a missing requirement, bring that decision back into the right artifact. Core Spec Kit does not automatically propagate revisions across all files. Keep a reviewable diff and decide which artifacts the team will maintain after delivery. [Evolving specs](https://github.github.com/spec-kit/how-to/evolving-specs.html) · [Persisting specs](https://github.github.com/spec-kit/how-to/persisting-specs.html).
