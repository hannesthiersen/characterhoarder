class OptionPool():
"""
Object/class that stores options given by choice of race, class or background
"""

    def __init__(self, *options, maxChoices):
        self.pool = options
        self.maxChoices = maxChoices
        self.resolved = False



