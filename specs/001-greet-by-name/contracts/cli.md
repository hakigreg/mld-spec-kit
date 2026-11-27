# Command Line Contract

Run `python3 greet.py NAME` from the project root. On Windows, use `py -3 greet.py NAME` if that is how Python is installed.

| Input | Standard output | Standard error | Exit status |
| --- | --- | --- | --- |
| `Ada` | `Hello, Ada!` and newline | Empty | 0 |
| `" Lin "` | `Hello, Lin!` and newline | Empty | 0 |
| Missing name | Empty | Usage message | Nonzero |
| `"   "` | Empty | `Name must not be blank.` | Nonzero |

Only one positional name is accepted. A name with spaces must be quoted by the shell.
