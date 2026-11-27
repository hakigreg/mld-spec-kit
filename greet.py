"""The deliberately small feature produced by the Spec Kit Lab."""

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(description="Greet one person by name.")
    parser.add_argument("name", help="name to greet")
    args = parser.parse_args()

    # Normalize the boundary input before applying the spec's blank-name rule.
    name = args.name.strip()
    if not name:
        parser.error("Name must not be blank.")

    print(f"Hello, {name}!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
