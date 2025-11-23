# Homework 7

Workshop 7 focuses on three themes: working with imports, designing flexible function signatures, and building introductory classes. Keep your solutions in a single file (for example, `homework_7.py`) so you can run them end to end.

## Task 1: Import Playbook
- Create a module-level constant `PI_TWO_DECIMALS` using `math.pi` rounded to two decimal places.
- Import `datetime` as `dt` and write a `current_utc()` helper that returns the current UTC timestamp using `dt.datetime.now(dt.timezone.utc)`.
- From `random`, import `randint` as `roll` and implement a `roll_die(sides=6)` function that returns a random integer between 1 and `sides`.
- Print a short summary showing the constant, current time, and the result of two dice rolls.

## Task 2: Flexible Arguments
- Write `announce(event, *audiences, prefix="[INFO]")` that formats a message similar to the example in `workshop_7/arguments_examples.py`.
- Implement `average_score(*scores)` that raises a `ValueError` when called without scores, otherwise returns the mean rounded to one decimal place.
- Create `build_connection(host, *, port=5432, **credentials)` that merges the required `host`, keyword-only `port`, and any extra credentials into a dictionary.
- Demonstrate each function with at least two sample calls covering different argument combinations.

## Task 3: Keyword-Only Practice
- Define `enroll_student(name, /, *, course, level="beginner", **meta)`.
- Call the function three times showing how positional-only, keyword-only, and extra metadata arguments behave. Print the returned dictionaries so the structure is clear.
- Add one comment explaining why the positional-only marker (`/`) is useful in this context.

## Task 4: Intro to Classes
- Create a `Course` class that stores `title`, `capacity`, and a list of students. Add an `enroll(student)` method that raises `ValueError` if the course is full and a `roster()` method that returns the names joined by commas or `"No students yet"` when empty.
- Subclass it into `OnlineCourse` that adds a `platform` attribute and an `info()` method returning a string like `"Python Foundations on Zoom (2/25 students)"`.
- Instantiate both classes, enroll a handful of students, and print `repr(course)`, the roster, and the info message to verify everything works.

## Optional Stretch
- Combine the pieces by writing `course_report(*courses, **filters)` that uses the earlier helpers (such as `announce`) to format a summary. Keep it simple: filtering by platform or minimum capacity is enough.
