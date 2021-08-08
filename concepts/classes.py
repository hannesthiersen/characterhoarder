class Fighter():
    name = "fighter"
    hitDie = 10
    halfDie = 6
    proficiencies = [
            "armor": ["all", "shields"],
            "weapons": ["simple", "martial"],
            "saves": ["str", "con"], ]

    profSkillPool = [
            "Acrobatics", "Animal Handling", "Athletics", "History",
            "Insight", "Intimidation", "Perception", "Survival", ]
    profSkillNumber = 2

    def __init__(self, character):
        self.character = character

    def maxBaseHitPoints():
        return self.hitDie - self.halfDie\
                + self.character.level\
                *(self.halfDie + self.character.constitution)


