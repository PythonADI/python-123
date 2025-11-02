# Homework 2

## 2.1 Review and Reflection
Summarize the key ideas you learned from Workshop 2 (assignment operator, user input, and basic conditionals). Write 3-4 bullet points in your own words and include at least one short example snippet for a conditional statement.

## Tasks
- Create a new script named `homework_2.py`. Start by copying the data collection from `homework_1.py` (name, age, prior coding experience) and add an extra question that asks the user for their favorite programming language.
- Ask the user for two numbers again, but this time store their responses as strings first. Show the user what happens if you try to compare the raw strings. Then convert the inputs to integers and print the comparison results (`>`, `<`, `==`) to explain why type conversion matters.
- Read an integer representing the number of study minutes completed today. Use integer division and modulus to convert it to hours and minutes (for example: `135 minutes -> 2 hours and 15 minutes`). Print a friendly message using f-strings.
- Extend the script with a simple conditional section:
  - Prompt the user for their current energy level on a scale of 1-5.
  - If the value is 4 or 5, print an encouraging message to continue studying.
  - If the value is 3, suggest a short break.
  - If the value is 1 or 2, suggest taking a longer rest before returning.
  - Handle unexpected inputs by showing a message that the entry is not recognized and they should try again.

## Bonus (Optional)
- Using the data from the energy level question, add a single-line conditional (inline `if` expression) that prints `"Packed study schedule!"` when the user studies more than 180 minutes and has an energy level of at least 4.

## Submission
- Commit your changes with a message such as `Add homework 2`.
- Push the commit to GitHub.
- Confirm that `homework_2.py` appears in your repository along with your written summary in `homework_2.md`.
