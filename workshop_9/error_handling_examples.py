"""Small error handling examples with try/except patterns."""

from pathlib import Path
from time import process_time_ns


def read_number(prompt: str) -> int:
    while True:
        raw_value = input(prompt)
        try:
            return int(raw_value)
        except ValueError:
            print(f"'{raw_value}' is not a valid integer. Please try again.")


def safe_divide(numerator: float, denominator: float) -> float:
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("Cannot divide by zero; returning 0 instead.")
        return 0.0
    else:
        print("Division succeeded without errors.")
    finally:
        print("safe_divide cleanup block executed.")


def load_config(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Missing config file: {path}")

    try:
        print(path.read_text())
    except SyntaxError as exc:
        raise ValueError("Config file contains invalid syntax") from exc


if __name__ == "__main__":
    # num = read_number("Give me number: ")

    # print(num, type(num))
    print("5 / 2 ->", safe_divide(5, 2))
    print("5 / 0 ->", safe_divide(5, 0))
    load_config(Path("workshop_9/error_handling_examples.py"))
    # load_config(Path("error_handling_examples.py"))


