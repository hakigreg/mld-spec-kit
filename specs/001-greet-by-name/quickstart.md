# Quickstart Validation: Greet by Name

Prerequisite: Python 3.11 or newer. Run these commands from the project root.

```sh
python3 --version
python3 greet.py Ada
python3 greet.py ' Lin '
python3 greet.py
python3 greet.py '   '
```

The first greeting should be `Hello, Ada!`; the second should be `Hello, Lin!`. The final two commands should print an error to stderr and exit nonzero. For a compact repeatable check, run `python3 verify_lab.py` from the project root.

The Lab exercise in the root [README](../../README.md) changes the salutation in the spec, then reconciles the plan, tasks, implementation, and expected output with Codex.
