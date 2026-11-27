# Tutorial: follow one requirement into running code

## 1. Confirm the local tools

From the project root, run `python3 --version`; Python 3.11+ is needed for the example. If `uv` is installed, run `uvx --from specify-cli==1.4.5 specify version` and `uvx --from specify-cli==1.4.5 specify check`. The version command confirms the pinned CLI runs; `check` reports available agent tools, including Codex CLI. A fresh machine may download the CLI on the first `uvx` run. The greeting itself needs no third-party package. [Official installation guide](https://github.github.com/spec-kit/installation.html).

## 2. Read the intent before the code

Open `specs/001-greet-by-name/spec.md`. Its first story says a person supplies a name and receives one greeting. FR-002 defines the precise line; FR-003 and FR-004 define trimming and rejection. Acceptance scenarios give concrete examples. No Python decision belongs there because someone could fulfill the same behavior with another language. The checklist under `checklists/requirements.md` reviews whether the spec is clear enough to plan; checked boxes do not prove the program works.

Next read `plan.md` and `research.md`. They explain why a local Python command with no storage is enough. `data-model.md` defines the transient Name value, and `contracts/cli.md` defines how the command behaves at its boundary. `tasks.md` names the files to change and the order. This is the point of the workflow: each downstream artifact answers a more concrete question while keeping the original behavior visible. [Agentic SDD reference](https://github.github.com/spec-kit/reference/agentic-sdd.html).

## 3. Run the example

```sh
python3 greet.py Ada
python3 greet.py ' Lin '
python3 verify_lab.py
```

Expect `Hello, Ada!`, `Hello, Lin!`, and four `PASS` lines ending in `4/4 acceptance examples passed`. The quoted second name demonstrates trimming. The checker also invokes the command without a name and with a whitespace-only name; both should fail with useful stderr. You can inspect those directly with `python3 greet.py` and `python3 greet.py '   '`. There is no process to stop: each command exits.

## 4. Change, predict, and observe

Predict the output if FR-002 said `Hi, <name>!`. Edit only the *existing* `spec.md` first, changing FR-002 and the two successful acceptance scenarios from `Hello` to `Hi`. At this moment, the implementation is intentionally out of sync. Ask Codex in this project to reconcile the plan, contract, quickstart, and tasks with the revised spec, reopening or appending the work to do. Use the installed `$speckit-analyze` skill to inspect cross-artifact consistency before implementation, `$speckit-implement` to carry out the work, and `$speckit-converge` to assess remaining gaps; invoke each separately in Codex chat and review the result. Include the README and relevant guide in the implementation update. Then rerun the three commands above. The expected new greeting is `Hi, Ada!`, and the four checks should still pass after their expected output is updated.

The `Hi` workflow is a learner exercise, **not the provided or verified final state of this Lab**. Spec Kit's core does not automatically rewrite all existing artifacts after a spec edit; explicitly request reconciliation. See [the official evolving-specs guide](https://github.github.com/spec-kit/how-to/evolving-specs.html). In larger projects the same pattern applies to new endpoints, data rules, or user journeys, but those examples are illustrative here.
