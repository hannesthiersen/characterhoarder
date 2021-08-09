class OptionPool():
    """
    Object/class that stores options given by choice of race, class or
    background.
    """

    def __init__(self, *options, maxChoices=1, mutualExclude=True):
        self.pool = list(options)
        self.selected = []
        self.maxChoices = maxChoices
        self.mutuallyExclusive = mutualExclude

    def selectItem(self, item):
        if not item in self.pool:
            print("item missing")
            return

        if self.isResolved():
            print("already resolved")
            return

        self.selected.append(item)
        if self.mutuallyExclusive:
            self.pool.remove(item)

    def getOptions(self):
        return self.pool

    def getSelection(self):
        return self.selected

    def isResolved(self):
        return len(self.selected) >= self.maxChoices



