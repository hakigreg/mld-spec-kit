# Use cases

Spec Kit is useful when a coding agent must turn a goal into reviewable steps instead of making an opaque code change. The following are representative uses, not features implemented in this Lab. [Official overview](https://github.github.com/spec-kit/) · [SDD explanation](https://github.github.com/spec-kit/how-to/sdd.html).

## A new user-facing feature

A team wants customers to export invoices. A spec can define who can export, which invoices are included, file contents, failure behavior, and acceptance scenarios before choosing PDF tooling or storage. A plan then selects the technical route; tasks divide the work; implementation is checked against the contract. This fits when several decisions could otherwise be hidden in code. The limit is that the team must still validate policy and customer needs; an agent cannot infer them reliably. The greeting Lab is the smallest version of this pattern: one user action and one exact output.

## A feature in an existing codebase

A service already handles notifications and needs an opt-out preference. Existing behavior and tests are evidence, while the revised specification states the *new intended* behavior. The plan must account for current modules and migration needs. Tasks should identify files and dependencies. The trade-off is artifact maintenance: old specs can become misleading unless the team chooses a retention and update convention. This Lab keeps one feature's artifacts next to its code and asks the learner to reconcile them after a change. [Evolving existing specs](https://github.github.com/spec-kit/how-to/evolving-specs.html).

## An interface shared by teams

Two services need to agree on an event payload. A written contract and acceptance examples can expose disagreements about required fields, errors, and versioning before either side implements. Spec Kit's plan phase can produce a contract document; analysis can then catch contradictions between the spec, contract, and tasks. It does not replace compatibility testing or agreement with consumers. This Lab uses a command-line contract rather than a network API, but the principle is the same: document observable obligations before changing code. [Contract-driven development](https://github.github.com/spec-kit/how-to/contract-driven-development.html).

## A complex or regulated change

For an access-control feature, targeted clarification and requirements checklists can make assumptions visible before implementation. Reviewers can inspect the spec and quality gates rather than only the code diff. This adds time and document volume; use it where ambiguity or consequences justify the overhead. The Lab uses the built-in spec checklist but leaves optional quality gates out of its tiny implementation. [Quickstart quality-gate path](https://github.github.com/spec-kit/quickstart.html).

Spec Kit also offers separate processes for bug fixing and idea assessment through opt-in extensions. They are different entry points rather than mandatory stages of SDD, and this Lab does not install them. [Official overview](https://github.github.com/spec-kit/).
