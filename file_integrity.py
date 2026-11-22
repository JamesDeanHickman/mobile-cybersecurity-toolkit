
import hashlib
import json
import argparse
from pathlib import Path
from datetime import datetime, timezone

BASELINE_FILE = Path(".integrity_baseline.json")


def calculate_hash(filename):
    """Calculate a file's SHA-256 hash."""
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def load_baseline():
    if not BASELINE_FILE.exists():
        return {}

    with open(BASELINE_FILE, "r") as file:
        return json.load(file)


def save_baseline(data):
    with open(BASELINE_FILE, "w") as file:
        json.dump(data, file, indent=4)


def create_baseline(files):
    baseline = load_baseline()

    for filename in files:
        path = Path(filename).resolve()

        if not path.is_file():
            print(f"[ERROR] File not found: {filename}")
            continue

        baseline[str(path)] = {
            "sha256": calculate_hash(path),
            "recorded": datetime.now(timezone.utc).isoformat()
        }

        print(f"[BASELINE CREATED] {path}")

    save_baseline(baseline)


def check_files():
    baseline = load_baseline()

    if not baseline:
        print("[ERROR] No baseline found. Create one first.")
        return

    for filename, record in baseline.items():
        path = Path(filename)

        if not path.exists():
            print(f"[MISSING] {filename}")
            continue

        current_hash = calculate_hash(path)

        if current_hash == record["sha256"]:
            print(f"[UNCHANGED] {filename}")
        else:
            print(f"[MODIFIED] {filename}")


def show_report():
    baseline = load_baseline()

    if not baseline:
        print("No baseline records found.")
        return

    print("\nFILE INTEGRITY BASELINE")
    print("-----------------------")

    for filename, record in baseline.items():
        print(f"\nFile: {filename}")
        print(f"SHA-256: {record['sha256']}")
        print(f"Recorded: {record['recorded']}")


def main():
    parser = argparse.ArgumentParser(
        description="Basic SHA-256 File Integrity Monitor"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    baseline_parser = subparsers.add_parser("baseline")
    baseline_parser.add_argument("files", nargs="+")

    subparsers.add_parser("check")
    subparsers.add_parser("report")

    args = parser.parse_args()

    if args.command == "baseline":
        create_baseline(args.files)
    elif args.command == "check":
        check_files()
    elif args.command == "report":
        show_report()


if __name__ == "__main__":
    main()
    