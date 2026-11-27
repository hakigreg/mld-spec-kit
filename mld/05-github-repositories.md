# GitHub repositories

These repository URLs were checked on 2026-11-26. The first is the technology itself; the others are the local tools used with it, not examples of completed Spec Kit features.

| Repository | Why it matters | What to inspect |
| --- | --- | --- |
| [github/spec-kit](https://github.com/github/spec-kit) | Official Spec Kit source and release history. | `templates/`, `docs/`, CLI code, and release tag `v1.4.5`. Compare the installed `.specify/` and `.agents/skills/` files with the release when learning how initialization works. |
| [openai/codex](https://github.com/openai/codex) | Source for the coding agent selected by this Lab's Spec Kit integration. | Codex CLI documentation and skill support; the Lab uses the Codex chat integration, not a custom runner. |
| [astral-sh/uv](https://github.com/astral-sh/uv) | Source for `uv`, used here to run the pinned Specify CLI through `uvx`. | Tool execution and package management documentation. `uv` is only needed for CLI setup/checks, not for `greet.py`. |

For a concrete filled feature artifact, start with this repository's `specs/001-greet-by-name/`; the official Spec Kit repository chiefly supplies templates and tooling. [Official quickstart](https://github.github.com/spec-kit/quickstart.html) provides a larger illustrative workflow.
