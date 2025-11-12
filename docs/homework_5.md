# Homework 5

Workshop 5 introduces functions. Start with a couple of lighter challenges to get comfortable defining and calling functions, then pick up the adventure you began in Homework 4. Your goal is to turn the story code into a small toolkit of reusable helpers.

## Task 1: A Tiny Travel Calculator
Write two more small utility functions in the same file:
- `travel_time(distance_km, speed_kmh=5)` that returns the number of hours (rounded to one decimal place) it takes to walk the distance.
- `format_supplies(water_liters, snacks)` that returns a single formatted string summarising what to pack.
Demonstrate both functions with sample values. These tasks are not part of the story—they are just warm-ups so you get used to writing, returning, and printing values from functions.

# Task 2-6: Reset the Stage
Copy the key pieces from Homework 4 (hero dictionary, starting chest, goblin encounter, and reward logic) into this file. Keep the same story beats, but remove any old loop code for now so you can rebuild it with functions.

## Task 3: Build Helper Functions for Your World
Create a section in the file dedicated to helper functions that manage the data. At minimum, implement and use the following:
- `create_hero()` that constructs and returns the hero dictionary with all the default fields (gold, hp, xp, inventory, and the extra story fields you used previously).
- `create_chest()` that returns the list of weapon dictionaries ready for the player to choose from.
- `create_goblin()` that returns the goblin dictionary with nested reward information just like in Homework 4.
Document your intent with one short comment above this block (for example, 
`# Factories create the starting state for the adventure`).

## Task 4: Action Functions
Make the gameplay logic easier to read by extracting actions into separate functions. Implement at least the following and call them from your main workflow:
- `choose_weapon(chest)` that prints the available weapon names, asks the player to pick one, and returns the chosen dictionary. It should keep reprompting until it returns a valid item. Remove the selected weapon from the chest before returning it.
- `deal_damage(attacker, defender)` that subtracts the attacker's `damage` from the defender's `hp`, cannot reduce `hp` below zero, prints a short message about the hit, and returns the updated defender dictionary. Use this both when the hero strikes and when the goblin retaliates.
- `is_defeated(character)` that returns `True` when `hp` is zero or lower.

## Task 5: Orchestrate the Battle Loop
Write a `run_battle(hero, goblin, weapon)` function that contains the combat loop. On each iteration, call `deal_damage(hero_weapon, goblin)` (or similar) when the player attacks, then check defeat conditions before letting the goblin swing back with the same helper. Keep the turn order and narration clear, and stop the loop as soon as someone falls. This function should return the string "victory" or "defeat".

## Task 6: Apply Rewards with Functions
Create a function `apply_reward(hero, reward)` that adds `xp` and `gold`, transfers the reward `item` into the hero's inventory, and prints a summary. Call it only when the battle outcome is "victory". If the player loses, write a separate function `show_defeat_summary(hero, chest)` that reports what went wrong and reminds them what items remain. After calling either path, print the final hero dictionary and each inventory item using a simple loop.

## Bringing It Together
Write a `main()` function that wires everything together: set up the hero, chest, and goblin by calling your factory helpers, let the player choose a weapon, run the battle, and handle the outcome. Call `main()` inside the usual `if __name__ == "__main__":` guard so you can import these helpers later. When you run the script, you should see a clear sequence of prints showing set up, choices, combat, and the end summary. [What is if __name__ == "__main__" in Python?](https://realpython.com/if-name-main-python/)

## Bonus Side Quests (Optional)
- Add a `defend` function that halves the incoming damage for a single turn and offer the player that choice in the battle loop.
- Create a `log_event(message)` helper that appends narration strings to a list so you can dump a timeline at the end of the fight.
- Turn `deal_damage` into a reusable tool that works for multiple monsters by accepting custom damage keys or fallback values (for example, `attacker.get("damage", 0)`).
- Write simple tests (even print-based checks) to make sure each helper behaves the way you expect before wiring them into the main battle. [How to Write Tests in Python](https://realpython.com/python-testing/)
