from character import Character

def buildFighter():

    mycharacter = Character()

    # Choose ability scores
    # TODO: write a scipt to choose ability scores

    # Set ability scores
    myFighter.setBaseAbilityScores({
        "strength": 15,
        "dexterity": 13,
        "constitution": 14,
        "intelligence": 12,
        "wisdom": 8,
        "charisma": 10, })

    # Choose race
    # TODO: write a scipt to choose race
    print("Race: Mountain Dwarf")

    # Set race attributes
    mycharacter.setRace = "mountain dwarf"
    mycharacter.addAbilityScoreIncreases({
        "constitution": 2,
        "strength": 2,})
    # TODO: set age
    # TODO: set alignment
    # TODO: set size
    # TODO: set speed
    # TODO: set darkvision
    mycharacter.addTraits(
            "dwarven resilience",
            "dwarven combat training",
            "dwarven tool proficiency",
            "stonecunning",
            "dwarven armor training",)

    # Choose class
    # TODO: write a scipt to choose class
    print("Class: Fighter")

    # Set class attributes
    mycharacter.setHitDie(10)
    # TODO: add proficiencies

    # Choose background
    # TODO: write a scipt to choose background
    print("Class: Soldier")

    # Set background attributes
    # TODO: add proficiencies

    # Set level(s)

    # Add level 1 features
    mycharacter.addFeatures(
            "fighting style",
            "second wind",)

    # TODO: add starter class equipment

    # TODO: add starter background equipment

    # TODO: add additional levels' features

    # Update character to implement traits and features


def main():
    mycharacter = Character()

    mycharacter.setBaseAbilityScores({
        "strength": 10,
        "dexterity": 20,
        "constitution": 16,
        "intelligence": 11,
        "wisdom": 10,
        "charisma": 14,
        })

    testab = "dexterity"
    print(testab[:3].upper(), mycharacter.getAbilityScore(testab))
    print(testab[:3].upper(), mycharacter.getAbilityModifier(testab))
    print(mycharacter.getAbilityScores())
    print(mycharacter.getAbilityModifiers())
    print(mycharacter.getSkills())


if __name__ == "__main__":
    main()
