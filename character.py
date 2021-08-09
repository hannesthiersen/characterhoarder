from characterproficiencies import CharacterProficiencies

from gameinfo import \
        STR_SKILLS, DEX_SKILLS, INT_SKILLS, WIS_SKILLS, CHA_SKILLS

#------------------------------------------------------------------------------
class Character():

    # consider including a component system

    #--------------------------------------------------------------------------
    def __init__(self):
        self.level = 1
        self.traits = []
        self.features = []
        self.inventory = []
        self.proficiencies = CharacterProficiencies()

    #--------------------------------------------------------------------------
    def addAbilityScoreIncreases(self, increases):
        self.abilityScoreIncreases.append(increases)

    #--------------------------------------------------------------------------
    def addFeatures(self, *args):
        self.features.extend(args)

    #--------------------------------------------------------------------------
    def addItems(self, *args):
        self.inventory.extend(args)

    #--------------------------------------------------------------------------
    def addTraits(self, *args):
        self.traits.extend(args)

    #--------------------------------------------------------------------------
    def setBackground(self, background):
        self.background = background

    #--------------------------------------------------------------------------
    def setBaseAbilityScores(self, abilityscores):
        self.baseAbilityScores = abilityscores
        self.abilityScoreIncreases = []
        self.initializeSkills()

    #--------------------------------------------------------------------------
    def setClass(self, charclass):
        self.charclass = charclass

    #--------------------------------------------------------------------------
    def setHitDie(self, die):
        self.hitDie = die
        self.halfDie = self.hitDie // 2 + 1

    #--------------------------------------------------------------------------
    def setLevel(self, level):
        self.level = level
        self.proficiencyBonus = lambda: 2 + (self.level -1) // 4

    #--------------------------------------------------------------------------
    def setRace(self, race):
        self.race = race

    #--------------------------------------------------------------------------
    def getAbilityModifier(self, ability):
        return (self.getAbilityScore(ability) - 10) // 2

    #--------------------------------------------------------------------------
    def getAbilityModifiers(self):
        abmods = self.getAbilityScores()
        for ability, score in abmods.items():
            abmods[ability] = (score - 10) // 2

        return abmods

    #--------------------------------------------------------------------------
    def getAbilityScore(self, ability):
        score = self.baseAbilityScores[ability]
        for increase in self.abilityScoreIncreases:
            score += increase.get(ability, 0)

        return score

    #--------------------------------------------------------------------------
    def getAbilityScores(self):
        abscores = {}
        for ability, score in self.baseAbilityScores.items():
            abscores[ability] = score

        for increase in self.abilityScoreIncreases:
            for ability, score in increase.items():
                abscores[ability] += score

        return abscores

    #--------------------------------------------------------------------------
    def getSkill(self, skill):
        return self.skills[skill]

    #--------------------------------------------------------------------------
    def getSkills(self):
        calcSkills = {}
        for skill, calc in self.skills.items():
            bonus = 0
            for func in calc:
                bonus += func()
            calcSkills[skill] = bonus
        return calcSkills

    #--------------------------------------------------------------------------
    # TODO: consider using an object to manage skills
    def initializeSkills(self):
        self.skills = {}

        # strength skills
        self.skills["athletics"] = [
                lambda: self.getAbilityModifier("strength"), ]

        # dexterity skills
        for skill in DEX_SKILLS:
            self.skills[skill] = [
                lambda: self.getAbilityModifier("dexterity"), ]

        # intelligence skills
        for skill in INT_SKILLS:
            self.skills[skill] = [
                lambda: self.getAbilityModifier("intelligence"), ]

        # wisdom skills
        for skill in WIS_SKILLS:
            self.skills[skill] = [
                lambda: self.getAbilityModifier("wisdom"), ]

        # charisma skills
        for skill in CHA_SKILLS:
            self.skills[skill] = [
                lambda: self.getAbilityModifier("charisma"), ]

    #--------------------------------------------------------------------------
    def initializeSpellCasting(self, ability):
        self.castingAbility = ability
        profBonus = self.proficiencyBonus()
        abmod = self.getAbilityModifier(ability)
        self.spellDC = 8 + profBonus + abmod
        self.spellAttack = profBonus + abmod
        self.spells = {
                "cantrips": [],
                1: [], }

    #--------------------------------------------------------------------------
    def addProficiencies(self, **proficiencies):
        armor = proficiencies.get("armor", "")
        if armor:
            self.proficiencies.addArmors(*armor)

        saves = proficiencies.get("saves", "")
        if saves:
            self.proficiencies.addSaves(*saves)

        skills = proficiencies.get("skills", "")
        if skills:
            self.proficiencies.addSkills(*skills)

        tools = proficiencies.get("tools", "")
        if tools:
            self.proficiencies.addTools(*tools)

    #--------------------------------------------------------------------------
    def addExpertise(self, *expertise):
        self.proficiencies.addExpertise(expertise)

    #--------------------------------------------------------------------------
    def getProficiencies(self):
        proficiencies = {}
        proficiencies["armor"] = self.proficiencies.getArmors()
        proficiencies["expertise"] = self.proficiencies.getExpertise()
        proficiencies["saves"] = self.proficiencies.getSave()
        proficiencies["skills"] = self.proficiencies.getSkills()
        proficiencies["tools"] = self.proficiencies.getTools()
        return proficiencies

    #--------------------------------------------------------------------------
    def implementProficiencies(self):
        for skill in self.proficiencies.skills:
            self.skills[skill].append(
                    lambda: self.proficiencyBonus(),)

    #--------------------------------------------------------------------------
    def getTraits(self):
        return self.traits


    #--------------------------------------------------------------------------
    def getFeatures(self):
        return self.features
















