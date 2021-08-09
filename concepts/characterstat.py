class CharacterStat():

    def __init__(self):
        self.contributions = {}

    def addContribution(self, description, contrib):
        if not description in self.cumulation():
            self.cumulation[description] = contrib

    def getFullStat(self):
        value = 0
        for contrib in self.contributions.values():
            value += contrib()

    def getContributions(self):
        return self.contributions



