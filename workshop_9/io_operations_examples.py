"""Demonstrations of text, CSV, and JSON file operations."""

import csv
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

TEXT_FILE = DATA_DIR / "notes.txt"
CSV_FILE = DATA_DIR / "scores.csv"
JSON_FILE = DATA_DIR / "settings.json"


def write_text() -> None:
    lines = ["Shopping list:", "- Apples", "- Bread", "- Tea"]
    TEXT_FILE.write_text("\n".join(lines))


def read_text() -> str:
    return TEXT_FILE.read_text()


def write_csv() -> None:
    headers = ["name", "score"]
    rows = [
        {"name": "Ada", "score": 95},
        {"name": "Grace", "score": 88},
        {"name": "Linus", "score": 92},
    ]
    with CSV_FILE.open("w", newline="") as handle:
        # handle.write(",".join(headers) + "\n")
        # for row in rows:
        #     handle.write(f"{row["name"]},{row["score"]}\n")
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def read_csv() -> list[dict[str, str]]:
    with CSV_FILE.open() as handle:
        reader = csv.DictReader(handle)
        return list(reader)


def write_json() -> None:
    settings = {
        "theme": "dark",
        "autosave": True,
        "font_size": 14,
    }
    JSON_FILE.write_text(json.dumps(settings, indent=2))


def read_json() -> dict:
    return json.loads(JSON_FILE.read_text())


if __name__ == "__main__":
    write_text()
    print("Text content:\n", read_text())

    write_csv()
    print("CSV rows:", read_csv())

    write_json()
    print("JSON settings:", read_json())
