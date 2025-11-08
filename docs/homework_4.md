# Homework 4

## Warm-Up: Quick Reflection
Write 3-4 bullet points that recap what you learned in Workshop 4 about dictionaries, slicing, and combining loops with user input. Finish with a 3-5 line code snippet that creates a tiny dictionary and prints one of the values.

## Task 1: Forge Your Hero
Imagine your adventure begins at dawn. Create a dictionary that represents your hero with keys for gold, hp (health points), xp, and an empty `inventory` list. Add at least two extra fields to round out the story (for example, `class`, `race`, `level`, or a `home_town`). Feel free to ask the user for a name or simply pick one yourself. Print the finished character sheet so the player knows who they are guiding.

## Task 2: Pack the Treasure Chest
Your hero finds a wooden chest loaded with gear for the journey. Represent the chest as a list that holds exactly three dictionaries: a sword (damage 10), a bow (damage 5), and an axe (damage 12). Each item dictionary must include the `damage` number plus at least two more keys such as `description`, `rarity`, or `weight`. Let the player choose at most one item. After a valid choice, append the selected item to the hero’s inventory, remove it from the chest, and narrate what happened. Hint: print the item names first, then use `input()` and match the choice with `.strip().lower()` so even entries like " Sword " still work. If the choice is not in the chest, re-prompt the player until they pick one of the available items.

## Task 3: A Goblin Appears
Trouble stomps into the clearing! Define a `goblin` dictionary with at least the following keys: `hp`, `damage` (use 5), and `reward`. The reward itself should be a dictionary containing `xp` (10), `gold` (50), and an `item`. Make the reward item a health potion dictionary that heals up to 100 hp and includes at least one extra detail such as `name` or `rarity`. Print a short introduction so the player knows what they are facing.

## Task 4: Clash in the Clearing
Write the battle scene between your hero and the goblin. Use a loop to represent turns and keep the loop running until either the hero or the goblin falls (hp <= 0). On each turn, let the player choose to attack (you may offer other actions, but keep it simple). Reduce the goblin’s hp by the weapon’s damage value and report the result. If the goblin is still standing, it swings back for 5 damage. End the loop as soon as one combatant runs out of hp, and print a dramatic message for defeat or victory. Remember to guard against negative hp values so your summary looks tidy.

## Task 5: Treasure Time
If the player wins, apply the goblin’s reward by adding xp and gold to the hero’s dictionary and transferring the potion into the hero’s inventory. If the player falls, explain what went wrong and remind them what is left in the chest. Finish by printing the hero’s final stats and everything currently stored in their inventory (listing the keys of each item is enough). If you decide to use the `.get()` method to read values from a dictionary, remember it returns a default value if the key is missing — handy when your data is still growing.

## Bonus Side Quests (Optional)
- Allow the player to drink the potion post-battle and cap their hp at the maximum value.
- Add a `defend` action that halves the goblin’s damage for one turn.
- Sort the remaining chest items alphabetically by name using `sorted()` and slicing to show just the first one as a teaser for the next adventure.
- Add a randomness twist to attacks: when either side swings, subtract a random amount between 0 and the attacker’s maximum damage from the hit. If the reduction equals the max damage, treat it as a miss; if it is 0, announce a clean hit.
- Expand the encounter list: store multiple monsters in a list, each with its own stats and reward dictionary. Loop over the list so the hero fights each foe in turn, collecting rewards along the way.
