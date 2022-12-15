import random

with open('nouns.txt') as f:
    nouns = [line.rstrip() for line in f]

with open('adjectives.txt') as f:
    adjectives = [line.rstrip() for line in f]

with open('spells.txt') as f:
    spells = [line.rstrip() for line in f]

with open('monsters.txt') as f:
    monsters = [line.rstrip() for line in f]

with open('triggers.txt') as f:
    triggers = [line.rstrip() for line in f]

with open('effects.txt') as f:
    effects = [line.rstrip() for line in f]

class card:
    def __init__(self):
        self.cost = random.randrange(10)
        self.health = random.randrange(10)
        self.damage = random.randrange(10)
        self.text = random.choice(triggers) + " " + random.choice(effects)
        if self.health==0:
            self.name = random.choice(adjectives)+" "+random.choice(spells)
        else:
            self.name = random.choice(adjectives)+" "+random.choice(monsters)

    def __str__(self):
        if self.health>1:
            return f"Monster: {self.name}: {self.cost}|{self.damage}|{self.health} \"{self.text}\""
        else:
            return f"Spell: {self.name}: {self.cost} \"{self.text}\" "
