class CharacterAsset():

    def __init__(self):
        self.components = {}

    def addBonus(self, description, implementation):
        if description not in self.components:
            self.components[description] = implementation

    def removeBonus(self, description):
        if description in self.components:
            del(self.components[description])

    def getBonus(self, description):
        return self.components[description]

    def getBonuses(self):
        return self.components

