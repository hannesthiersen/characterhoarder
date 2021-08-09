def containsElement(func):
    def wrapper(self, label):
        if label in self.stat:
            func(self, label)
    return wrapper

def newElement(func):
    def wrapper(self, label):
        if label not in self.stat:
            func(self, label)
    return wrapper


class SkillStat():
    """ Objects that represents a skill and it's bonuses. """

    def __init__(self, baseBonus=None):
        """
        baseBonus should be an callable object that returns a value(int).
        e.g.: a function
        """
        if not baseBonus:
            baseBonus = lambda: 0 # return

        self.stat = {
                "base": baseBonus, }

    @newElement
    def addBonus(self, label, bonus):
        """ Add a bonus(callable) and label it with a string. """
        self.stat[label] = bonus

    @containsElement
    def removeBonus(self, label):
        del(self.stat[label])

    @containsElement
    def setBonus(self, label, newBonus):
        self.stat[label] = newBonus

    def getValue(self):
        value = 0
        for bonus in self.stat.values():
            value += bonus()
        return value

