"""Run the feature's four acceptance examples without extra dependencies."""

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CASES = (
    (("Ada",), 0, "Hello, Ada!\n", ""),
    ((" Lin ",), 0, "Hello, Lin!\n", ""),
    ((), 2, "", "usage:"),
    (("   ",), 2, "", "Name must not be blank."),
)


def main() -> int:
    for index, (args, expected_status, expected_stdout, expected_stderr) in enumerate(CASES, 1):
        result = subprocess.run(
            (sys.executable, str(ROOT / "greet.py"), *args),
            capture_output=True,
            text=True,
            check=False,
        )
        passed = (
            result.returncode == expected_status
            and result.stdout == expected_stdout
            and (result.stderr == "" if not expected_stderr else expected_stderr in result.stderr)
        )
        print(f"Case {index}: {'PASS' if passed else 'FAIL'}")
        if not passed:
            print(f"  status={result.returncode}, stdout={result.stdout!r}, stderr={result.stderr!r}")
            return 1
    print("4/4 acceptance examples passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
