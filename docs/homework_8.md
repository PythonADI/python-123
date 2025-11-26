# Homework 8

Workshop 8 moves from plain data structures into object-oriented design. This homework asks you to invent fresh scenarios instead of remixing class examples. Focus on encapsulating behaviour inside classes, keeping state consistent, and composing multiple objects together. Keep the solutions in a single script (for example, `homework_8.py`) so you can run everything end to end.

## Task 1: Meteorological Diary
- Create a `WeatherSnapshot` class with `temperature`, `humidity`, and `observed_at` (a `datetime.datetime`) attributes.
- Implement `__repr__` so each instance prints as a compact ISO-style summary (for example, `WeatherSnapshot(2025-02-14T08:00, 18°C, 62%)`).
- Add a method `cool_down(delta=1)` that returns a **new** `WeatherSnapshot` with a reduced temperature but identical humidity and timestamp, leaving the original untouched.
- Generate four distinct snapshots and iterate over them printing the original and cooled versions to highlight immutability.

## Task 2: Smart Garden Devices
- Design a `SmartIrrigator` class that tracks `name`, `water_reserve`, and `daily_limit`.
- Provide methods `refill(amount)`, `sprinkle(volume)`, and `status()`; ensure `sprinkle` rejects overuse via `ValueError` and always deducts from the reserve.
- Add a computed property `needs_refill` that becomes `True` when the reserve drops below 20% of capacity.
- Demonstrate two devices with different limits, run a short watering routine, and print their status along with whether they need a refill.

## Task 3: Greenhouse Coordinator
- Build a `Greenhouse` class that stores multiple `SmartIrrigator` instances in a dictionary keyed by device name.
- Provide `register_device(device)` that stores and returns the device, `get_device(name)` that retrieves a device or `None`, and `total_water_remaining()` that sums reserves across all devices.
- Implement `busiest_device()` returning the irrigator that sprinkled the most cumulative volume (track per-device usage inside `SmartIrrigator`). Return `None` when there are no devices.
- Simulate a day's schedule: register at least three devices, perform varied watering operations, then report the total remaining water and the name of the busiest device.

## Task 4: Action Log
- Write a helper `log_action(message, *, timestamp=None)` that defaults to `datetime.datetime.now()` and prints a line like `2025-01-14T21:15:00 — Sprinkled 3L from HerbGarden`.
- Integrate the logger into at least two methods from Tasks 2 or 3 so significant actions generate entries (for example, refills and sprinkling events).
- Store each log line in a list in addition to printing it, then display the complete log at the end of your script to confirm ordering.

## Optional Stretch
- Add a `SmartMister` subclass that introduces humidity boosts and customises `status()`.
- Write a small test section that asserts `Greenhouse.total_water_remaining()` matches the sum of each stored device after several operations.
