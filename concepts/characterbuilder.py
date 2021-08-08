class CharacterBuilder():

"""
Object/class for handling building instruction of a character
"""

    def __init__(self, character, race, characterClass, background):
        self.character = character
        self.race = race
        self.characterClass = characterClass

        self.traits = []
        self.features = []
