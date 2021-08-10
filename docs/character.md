# Rationale

A class/object that stores and keeps track of all character information
including ability scores, skills, physical attributes, features, bonuses, etc.
and represents the character in full.


# Data structure

## Ability Scores

Ability scores are split into the base score and all the increases applied to
the character. All scores (base score and each ability improvement separately)
are represented as a dictionary where the key, value pairs represent ability,
score. Each ability increase is stored in a list.

    ```
    self.baseAbilityScores = {
        "strength": 15,
        "dexterity": 14,
        "constitution": 13,
        "intelligence": 12,
        "wisdom": 8,
        "charisma": 10, }

    self.abilityScoreIncreases = [
        { "strength": 2, "constitution": 2, },
        { "strength": 1, "wisdom": 1, }, ]
    ```

## Skills

Skills are represented in a dictionary where key, value pairs represent a
skill's name and list of bonuses. Bonuses are represented by a callable object
that would return an integer (e.g. lambda functions).

    ```
    self.skills = {
        "athletics": lambda: self.getAbilityModifier("strength"),
        "stealth": lambda: self.getAbilityModifier("dexterity"),
        "perception": lambda: self.getAbilityModifier("wisdom"), }
    ```


# Initialization

Initialization creates the some empty character attributes (list/dicts/etc.).
To build the character further all other info is initialized separately outside
the objects `__init__()` routine.

Order of secondary initialization:
- Base Ability Score (setBaseAbilityScores(self, abilityScores))
    > Ability Score Increases (empty value)
    > Skills
- Any and all other attributes

[\*] TODO: re-evaluate initialization


# Behaviour

- Allows the ability to add any new information to the character including
  bonuses provided by racial traits, class and other features.

- Allow bonuses have an active/implemented effect.

- Calculating character attributes such as skills and ability scores/modifiers
  and accounting for all bonuses


