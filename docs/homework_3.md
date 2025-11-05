# Homework 3

## 3.1 Reflection and Planning
Summarize the study habits you used during Workshop 3. Write 3-4 bullet points covering what helped you understand loops, lists, and flow control (`break` / `continue`). End the section with one short code snippet that demonstrates a `while` loop you find useful.

## Tasks
- Create a new script named `homework_3.py` inside your repository. Begin the script with a short introduction that prints what the program does.
- Build an input loop that keeps asking the user to enter study tasks (one per line) until they submit a blank line. Store each non-empty response in a list. If the user repeats a task that is already in the list, print a message and skip adding it by using `continue`.
- After the collection loop finishes, print the total number of unique tasks and display them as a numbered checklist using a `for` loop and `enumerate` starting at 1.
- Ask the user how many tasks they plan to complete today. Use a `while` loop to validate that the answer is an integer between 1 and the total number of collected tasks. Keep prompting until the input is valid.
- Use list slicing to show only the tasks the user plans to work on today. For each of those tasks, ask for an estimated number of minutes to spend. Accumulate the total study time as you iterate. If the user enters a negative number, warn them and ask again without moving to the next task (use another loop to re-prompt).
- When all estimates are gathered, print:
  - The total minutes of planned study time.
  - The average minutes per task (rounded to one decimal place).
  - A short summary that indicates whether the plan is light (less than 60 minutes), moderate (60-149 minutes), or intensive (150 minutes or more). Use `if`/`elif`/`else` to determine the message.

## Bonus (Optional)
- Shuffle the list of planned tasks using the `random` module and print a suggested study order.
- Add an inline `if` expression that prints `"Great momentum!"` when the average minutes per task is at least 30.
- Build a number guessing mini-game where the **computer** is the one guessing. Let the user pick a secret integer in a range you define (for example, 1-100). Use a loop where the computer proposes guesses and the user responds with feedback such as `higher`, `lower`, or `correct`. Keep the computer's guesses efficient by updating the possible range on each turn until it finds the right answer, then print how many attempts it took.

## Submission
- Commit your work with a message such as `Add homework 3`.
- Push the commit to GitHub and confirm that both `homework_3.py` and `homework_3.md` are present in your repository.
