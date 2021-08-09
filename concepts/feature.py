class Feature():

    def __init__(self, name):
        self.name = "name"

    def implement(self, character):
        if self.name in character.getFeatures():


class AbilityScoreImprovement(Feature):

    def __init__(self, name, increases):
        super(Feature).__init__()
        self.increases = increases


    def implement(self, character):
        character.addAbilityScoreIncreases(increases)


class KeenSenses(Feature):

    def implement(self, character):
        character.addProficiencies(skills=["perception"])
        character.skills["perception"].append(
                lambda: character.proficiencyBonus(), )
