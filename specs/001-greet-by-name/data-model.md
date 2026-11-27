# Data Model: Greet by Name

## Name

`Name.value` is a nonempty string supplied as one command argument. Leading and trailing whitespace are removed before use. It is not stored. A whitespace-only value is invalid.

## Output

The output is a transient line built from the cleaned name: `Hello, <name>!`. There are no relationships, persistence rules, or state transitions.
