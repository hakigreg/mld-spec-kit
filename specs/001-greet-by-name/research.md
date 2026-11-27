# Research: Greet by Name

## Decision: local Python command

Use Python 3.11+ and its standard library. It is already present locally and makes the acceptance examples executable without an application framework. A shell-only script would require different command variants on Windows; a web app would add an irrelevant server.

## Decision: one argument and one output line

Accept the name as a positional argument, trim its outer whitespace, and print the greeting. Use a failing exit status and stderr for blank input. This is easy to inspect from a terminal and maps directly to FR-001 through FR-004.

## Decision: no persisted state

The Name entity exists only during an invocation. A database, configuration file, or API would not help demonstrate the feature.
