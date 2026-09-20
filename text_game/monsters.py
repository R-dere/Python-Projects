import random
class Slime_monster():
    def __init__(self):
        self.hp = 50
        self.defense = 0.4
        self.dmg = random.randint(30,40)
        self.speed = 3

    def damage(self,dmg):
        self.hp -= dmg - int(dmg*self.defense)