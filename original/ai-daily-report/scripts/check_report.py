#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path

from report_validator import dump_validation, validate_report


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an AI daily report markdown file.")
    parser.add_argument("report", help="Path to the markdown report file")
    parser.add_argument("--target-date", help="Target report date in YYYY-MM-DD format")
    parser.add_argument("--window-days", type=int, default=2, help="Allowed date window on each side")
    args = parser.parse_args()

    result = validate_report(Path(args.report), target_date=args.target_date, window_days=args.window_days)
    print(dump_validation(result))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
