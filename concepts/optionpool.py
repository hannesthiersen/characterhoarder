class OptionPool():
"""
Object/class that stores options given by choice of race, class or background
"""

    def __init__(self, maxChoices, *options, mutualExclude=True):
        self.pool = options
        self.selected = []
        self.maxChoices = maxChoices
        self.mutuallyExclusive = mutualExclude

    def selectItem(self, item):
        if item not in self.pool or self.isResolved:
            return

        self.selected.append(item)
        if self.mutuallyExclusive:
            self.pool.remove(item)

    def getOptions(self):
        return self.pool

    def getSelection(self):
        return self.selected

    def isResolved():
        return self.selected >= self.maxChoices



