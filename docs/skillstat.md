# Rationale

A container class/object that keeps track of an individual character skill's
bonuses from ability score modifiers, proficiencies/expertise and other feature
bonuses.

# Data structure

Contains a dictionary where each key, value pair represents the label and
implementation (callable object that returns an integer; e.g.: a function) of a
bonus. Refer to the following pseudo example:

    self.stat = {
        "base": lambda: character.getAbilityModifier("strength"),
        "proficiency": character.getProficiencyBonus(),
        "jack of all trades": character.getProficiencyBonus() //2,
    }

## Initialization

- Initialize with ground/base bonus (ability modifier). If no bonus is given
  just initialize it as `lambda: 0`.
    `__init__(self, baseBonus=None)`

# Behaviour

- Add additional bonuses with unique labels. If bonus given already exist,
  ignore and return None.
    `addBonus(self, label, bonus)`

- Retrieve value by summing up all bonuses.
    `getValue(self)`

- Allow removal of bonuses except the base bonus (re-evaluation required if
  scenario is found where base bonus needs to be removed).
    `removeBonus(self, label)`

- Allow resetting/overwriting bonus values (re-evaluation needed; this might
  not be necessary given that the bonus values are retrieved from callable
  objects that already takes all required variables in consideration).
    `setBonus(self, label, bonus)`

