class CharacterProficiencies():

    def __init__(self):
        self.armor = []
        self.expertise = []
        self.saves = []
        self.skills = []
        self.tools = []

    def addArmors(self, *args):
        self.armor.extend(args)

    def addExpertise(self, *args):
        self.expertise.extend(args)

    def addSaves(self, *args):
        self.saves.extend(args)

    def addSkills(self, *args):
        self.skills.extend(args)

    def addTools(self, *args):
        self.tools.extend(args)

    def getArmors(self):
        return self.armor

    def getExpertise(self):
        return self.expertise

    def getSave(self):
        return self.saves

    def getSkills(self):
        return self.skills

    def getTools(self):
        return self.tools

    def hasExpertise(self):
        return bool(self.expertise)
