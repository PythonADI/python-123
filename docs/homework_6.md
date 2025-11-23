# Homework 6

Workshop 6 introduces modules, imports, and simple composition patterns. Complete the tasks in a new file (for example, `homework_6.py`) so you can run everything together.

## Task 1: Utility Pairing
- Create a module-level function `square(number)` that returns the number squared.
- Create another function `shift_and_square(number, offset)` that adds the offset to the number, then calls `square` and returns the result.
- Demonstrate both functions by printing at least two sample calculations.

## Task 2: Banking Flow Composition
- Reuse the idea from `workshop_6/composition.py` to model a simple payment attempt.
- Implement `check_balance()` that randomly returns `True` or `False` (use `random.choice`).
- Implement `complete_transaction()` that prints a confirmation message and returns a dictionary describing the order.
- Implement `place_order()` that only calls `complete_transaction()` when `check_balance()` returns `True`; otherwise, it returns a dictionary with a failed status. Include an `order_id` and `total` in both success and failure paths (use `None` for failed orders if needed).
- Run the `place_order()` function three times, collect the results in a list, and print a human-readable summary for each attempt.

## Task 3: Module Import Practice
- Create a separate file named `helpers.py` that contains the `square` and `shift_and_square` functions from Task 1.
- In `homework_6.py`, import `helpers` and demonstrate the functions via the module namespace (`helpers.square`, `helpers.shift_and_square`).
- Explain in a short comment why keeping helper functions in a separate module can make larger projects easier to manage.

## Task 4: Defensive Composition
- Write a function `safe_place_order(max_attempts=3)` that tries to call `place_order()` until it receives a success or exhausts `max_attempts`.
- Track and print each attempt number and outcome.
- Return the successful order or `None` if every attempt fails.

## Optional Stretch Goals
- Extend `complete_transaction()` to accept `**kwargs` for additional metadata (for example, `coupon="SAVE10"`).
- Add a simple logger function that timestamps each step using `datetime` and prints a consistent prefix.
- Write a mini-test section that imports `helpers` and asserts the output of `square()` and `shift_and_square()` for a few inputs.
