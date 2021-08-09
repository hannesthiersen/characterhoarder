from character import Character

def buildFighter():

    mycharacter = Character()

    # Choose ability scores
    # TODO: write a scipt to choose ability scores

    # Set ability scores
    mycharacter.setBaseAbilityScores({
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
    mycharacter.addProficiencies(**{
        "armor": [ "all", "shield" ],
        "weapon": [ "simple", "martial" ],
        "skills": [ "survival", "insight" ],
        "saves": [ "strength", "constitution" ],
        })

    # Choose background
    # TODO: write a scipt to choose background
    print("Background: Soldier")
    print()

    # Set background attributes
    # TODO: add proficiencies
    mycharacter.addProficiencies(**{
        "tools": [ "dice set", "vehicle(land)" ],
        "skills": [ "athletics", "intimidation" ],
        })

    # Set level(s)
    mycharacter.setLevel(1)

    # Add level 1 features
    mycharacter.addFeatures(
            "fighting style",
            "second wind",)

    # TODO: add starter class equipment

    # TODO: add starter background equipment

    # TODO: add additional levels' features

    # Update character to implement traits and features
    mycharacter.implementProficiencies()

    #--------------------------------------------------------------------------
    # Show character stats
    #--------------------------------------------------------------------------
    # Ability scores
    print("Ability Scores:")
    fmod = lambda mod: f"+{mod}" if not mod<0 else str(mod)
    abscores = mycharacter.getAbilityScores()
    abmods = mycharacter.getAbilityModifiers()
    for ability, score in abscores.items():
        print("\t{} [{}] {}".format(
            fmod(abmods[ability]),
            str(abscores[ability]).rjust(2),
            ability[:3].upper()))
    print()


    #--------------------------------------------------------------------------
    # Skill scores
    profs = mycharacter.getProficiencies()
    profstar = lambda skill: \
        f"*{skill}" if skill in profs["skills"] else skill
    print("Skills:")
    skillscores = mycharacter.getSkills()
    for skill, score in skillscores.items():
        print("\t{} {}".format(fmod(score), profstar(skill)))
    print()

    #--------------------------------------------------------------------------
    # All proficiencies
    print("All Proficiencies:")
    for ptype, proflist in profs.items():
        print(f"{ptype}: ", *proflist)
    print()

    #--------------------------------------------------------------------------
    print("Traits(racial)")
    for trait in mycharacter.getTraits():
        print(trait)
    print()


    print("Features")
    for feature in mycharacter.getFeatures():
        print(feature)



#------------------------------------------------------------------------------
def simpleCharacter():
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

def main():
    buildFighter()


if __name__ == "__main__":
    main()
