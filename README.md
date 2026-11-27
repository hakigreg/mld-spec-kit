# Minimum Lab Deployment: GitHub Spec Kit with Codex

This Lab shows one Spec Kit behavior: **a user-visible requirement becomes a specification, an implementation plan, a task list, and working code that can be checked against the requirement**. The example is a local greeting command. `Ada` produces `Hello, Ada!`. The exercise changes the intended salutation to `Hi`, then follows that change through the artifacts and output.

Spec Kit supplies the project structure, templates, scripts, and Codex skills in `.specify/` and `.agents/skills/`. Codex interprets the skill instructions; the skills are invoked in Codex chat, not in the shell. The active feature is `specs/001-greet-by-name/`, selected by `.specify/feature.json`. This Lab was initialized with official Spec Kit **1.4.5** and the `codex` integration. See the [official quickstart](https://github.github.com/spec-kit/quickstart.html) and [Codex integration guide](https://github.github.com/spec-kit/integrations/codex.html).

## Prerequisites and setup

- Python 3.11 or newer to run the example.
- Codex in this project directory for the AI-assisted exercise.
- `uv` for the optional Spec Kit CLI checks. The installed scaffold is already present; there is no package to install to run the greeting.

From this directory:

```sh
python3 --version
uvx --from specify-cli==1.4.5 specify version
uvx --from specify-cli==1.4.5 specify check
```

If you lack `uv`, you can still run the example with Python and inspect the checked-in Spec Kit artifacts. To initialize a *new* project with the same integration, see [installation](https://github.github.com/spec-kit/installation.html); do not rerun `specify init` here merely to run this Lab.

## Run and verify

```sh
python3 greet.py Ada
python3 greet.py ' Lin '
python3 verify_lab.py
```

Expected output is `Hello, Ada!`, then `Hello, Lin!`, then four `PASS` lines and `4/4 acceptance examples passed`. The checker also confirms that missing and blank names fail. There is no background process: each command exits immediately, so **stop** requires no command.

## Exercise: change a requirement, then observe

1. Read [the feature spec](specs/001-greet-by-name/spec.md), especially FR-002 and the acceptance scenarios. Predict what `python3 greet.py Ada` would print if the required salutation were `Hi`.
2. Edit the existing spec so its valid-name examples and FR-002 say `Hi, <name>!` instead of `Hello, <name>!`. Keep the same feature directory and user story.
3. In a Codex chat opened in this project, ask: “Reconcile the existing greeting feature after I changed its spec from Hello to Hi. Update its plan, contract, quickstart, and tasks; reopen or append the implementation work. Do not create a new feature or change code yet.” Review those artifacts. Then invoke `$speckit-analyze`, `$speckit-implement`, and `$speckit-converge` separately in Codex chat, reviewing each result. Ask Codex to update the README and relevant `mld/` guide as part of the implementation and run verification.
4. Run `python3 greet.py Ada` and `python3 verify_lab.py` again. Expected after the change: `Hi, Ada!` and `4/4 acceptance examples passed` with the checker updated to the new requirement. Inspect the spec, plan, tasks, code, and checks to see how one intended behavior flowed through them.

Spec Kit does not automatically rewrite every artifact after an existing requirement changes; reconcile the affected files and use its analysis and convergence steps to find gaps. See the [official evolving-specs guide](https://github.github.com/spec-kit/how-to/evolving-specs.html). The provided baseline remains `Hello`; the `Hi` change is for the learner to perform.

## Essential file map

| Path | Role |
| --- | --- |
| `.specify/memory/constitution.md` | Project principles for the feature workflow |
| `.specify/feature.json` | Local pointer to the active feature; machine-local in Spec Kit's normal Git setup |
| `.agents/skills/speckit-*/SKILL.md` | Official Codex skill instructions installed by Spec Kit |
| `specs/001-greet-by-name/spec.md` | What users need and the acceptance examples |
| `specs/001-greet-by-name/plan.md` | Python approach and file layout |
| `specs/001-greet-by-name/tasks.md` | Ordered implementation work and completion state |
| `specs/001-greet-by-name/quickstart.md` | Feature-level validation examples |
| `greet.py` | The local behavior |
| `verify_lab.py` | Four executable acceptance checks |
| `mld/` | Learning guide below |

## Learning guide

Read in order: [concepts](mld/01-concepts-and-fundamentals.md), [tutorial](mld/02-tutorial.md), [use cases](mld/03-use-cases.md), [essential links](mld/04-essential-links.md), [GitHub repositories](mld/05-github-repositories.md), [best practices](mld/06-best-practices.md), [bad practices](mld/07-bad-practices.md), [next iterations](mld/08-next-iterations.md).
