class Class(object):
    def __init__(self, name, Overall_level, strength, intelligence, agility):
        self.name = name
        self.Overall_level = Overall_level
        self.strength = strength
        self.intelligence = intelligence
        self.agility = agility

    inventory = {
        'gold': 150,
        'pouch': [],
        'backpack': []

    }


class Mage(Class):
    def __init__(self, name, Overall_level, strength, intelligence, agility):
        self.name = name
        self.Overall_level = Overall_level
        self.strength = strength
        self.intelligence = intelligence
        self.agility = agility

    inventory = {
        'gold': 300,
        'pouch': ['Ring of Frost', 'Staff of Wisdom'],
        'backpack': []
    }
def cls(): print("\n" * 20)